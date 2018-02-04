# class Solution(object):
#     def exist(self, board, word):
#         """
#         :type board: List[List[str]]
#         :type word: str
#         :rtype: bool
#         """

#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import logging
import sys
import os
import re
import json
import commands
import urllib2
from datetime import datetime, timedelta
from optparse import OptionParser
from werkzeug.utils import cached_property
from sqlalchemy import create_engine, text

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


BINLOG_FORMAT = 'mysql-bin\.(\d{6})'
DIR_BINLOG = None
HOST_INSTANCE_ID = None
MYSQL_HOST = None
MYSQL_USER = None
MYSQL_PORT = None
MYSQL_PASSWORD = None
conn = None


def get_id_from_binlog_name(log_name):
    pattern = re.compile(BINLOG_FORMAT)
    result = pattern.findall(log_name)
    return int(result[0]) if result else 0


def log(text):
    print text


def err(message):
    sentry.captureMessage(message)
    raise Exception(message)


class BinlogSync(object):
    ALIYUNCLI = ('aliyuncli rds DescribeBinlogFiles '
                 '--DBInstanceId "rm-2zel05i34d9r9e3x3" '
                 '--StartTime {}T00:00:00Z --EndTime {}T00:00:00Z ')

    def __init__(self, start_time, end_time):
        self.start_time = start_time
        self.end_time = end_time

    def run(self):
        if self.is_exception:
            message = 'Local exists unhandled tar file'
            err(message)
        aliyun_command = self.ALIYUNCLI.format(self.start_time, self.end_time)
        log(aliyun_command)
        output = commands.getstatusoutput(aliyun_command)
        if output[0] != 0:
            message = 'DescribeBinlogFiles failed {}'.format(str(output))
            err(message)

        data = json.loads(output[1])
        while True:
            log('\nLast file: {}'.format(self.last_file))

            is_matched = False
            for item in data['Items']['BinLogFile']:
                if item['HostInstanceID'] != HOST_INSTANCE_ID:
                    continue

                log_time = datetime.strptime(
                    item['LogEndTime'], '%Y-%m-%dT%H:%M:%SZ'
                ) + timedelta(hours=8)
                binlog = BinlogFile(item['DownloadLink'], log_time)
                if get_id_from_binlog_name(binlog.current_file) == \
                        get_id_from_binlog_name(self.last_file) + 1:
                    is_matched = True
                    binlog.flow()
                    self.last_file = binlog.current_file
                    break

            if not is_matched:
                break

    @cached_property
    def last_file(self):
        sql = 'SELECT log_name FROM update_log ORDER BY log_name DESC LIMIT 1'
        result = conn.execute(sql).fetchall()
        return result[0][0] if result else 'tar'

    @property
    def is_exception(self):
        """是否异常中断"""
        return self.last_file[-3:] == 'tar'


class BinlogFile(object):

    def __init__(self, download_url, log_time):
        self.download_url = download_url
        self.log_time = log_time
        pattern = re.compile(BINLOG_FORMAT)
        result = pattern.findall(self.download_url)
        if not result:
            Exception('URL illegal {}'.format(self.download_url))
        self.current_file = 'mysql-bin.{}'.format(result[0])
        self.tar_file = self.current_file + '.tar'

    def download(self):
        log('Downloading {} ...'.format(self.current_file))
        try:
            f = urllib2.urlopen(self.download_url)
            with open(self.tar_file, "wb") as w_file:
                w_file.write(f.read())
        except Exception as e:
            sentry.captureException()
            raise e

    def unpack_file(self):
        log('Unpack tar file...')
        result = commands.getstatusoutput('tar -xvf {}'.format(self.tar_file))
        if result[0] != 0:
            message = 'unpack tar file failed {}'.format(self.tar_file)
            err(message)

    def mysqlbinlog(self):
        log('mysqlbinlog...')
        mysqlbinlog_command = (
            'mysqlbinlog --no-defaults {} | mysql -h{} -P{} -u{} -p{} -f'
        ).format(
            self.current_file,
            MYSQL_HOST, MYSQL_PORT, MYSQL_USER, MYSQL_PASSWORD)
        log(mysqlbinlog_command)
        result = commands.getstatusoutput(mysqlbinlog_command)
        log(result)
        if result[0] != 0:
            err(result[1])

    def rm_tar_file(self):
        log('Remove tar file...')
        result = commands.getstatusoutput('rm -f {}'.format(self.tar_file))
        if result[0] != 0:
            err(result[1])

    def start_log(self):
        sql = text('INSERT INTO update_log (log_name, log_time)'
                   ' VALUES (:log_name, :log_time)')
        conn.execute(sql, log_name=self.tar_file, log_time=self.log_time)

    def finish_log(self):
        sql = text('UPDATE update_log SET log_name=:new_log_name'
                   ' WHERE log_name=:old_log_name')
        conn.execute(sql, new_log_name=self.current_file,
                     old_log_name=self.tar_file)

    def flow(self):
        self.start_log()
        self.download()
        self.unpack_file()
        self.rm_tar_file()
        self.mysqlbinlog()
        self.finish_log()


if __name__ == '__main__':

    parser = OptionParser(add_help_option=False)
    parser.add_option('-h', default='127.0.0.1')
    parser.add_option('-P', default='3306')
    parser.add_option('-u', default='jijindou')
    parser.add_option('-p', default='Wealthworks')
    parser.add_option('-d', default='/data/mysql/jijindou-bak/bak-binlogs/')
    parser.add_option('-i', type='int', default=1493995)
    options, args = parser.parse_args()
    MYSQL_HOST = options.h
    MYSQL_PORT = options.P
    MYSQL_USER = options.u
    MYSQL_PASSWORD = options.p
    DIR_BINLOG = options.d
    HOST_INSTANCE_ID = options.i

    engine = create_engine('mysql+pymysql://{}:{}@{}:{}/jijindoulog'.format(
        MYSQL_USER, MYSQL_PASSWORD, MYSQL_HOST, MYSQL_PORT), echo=True)
    conn = engine.connect()

    os.chdir(DIR_BINLOG)

    now = datetime.now()
    start_time = (now + timedelta(days=-2)).strftime('%Y-%m-%d')
    end_time = (now + timedelta(days=1)).strftime('%Y-%m-%d')

    BinlogSync(start_time, end_time).run()
    log('done')
