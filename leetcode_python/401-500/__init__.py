f = open('events')

out1 = open('pid1', 'w')
out2 = open('pid2', 'w')

import json
while True:
    line = f.readline()
    if not line:
        line = f.readline()
        if not line:
            break
    try:
        dic = json.loads(line)
    except Exception as e:
        print(line, e)
        continue
    if 'censor_result' in line:
        out2.write(str(dic.get('oid', ''))+'\n')
    else:
        out1.write(str(dic.get('oid', '')) + '\n')
