package leetcode_go

import "math"


func containsNearbyAlmostDuplicate(nums []int, k int, t int) bool {
    if t < 0 || k < 1 {
        return false
    }
    d := make(map[int]int)
    w := t + 1
    var m int
    for i, v := range nums {
        if v >= 0 {
			m = v / w
		}else {
			m = (v-t)/w
		}
        if _, ok := d[m]; ok {
            return true
        }
        if m_1, ok := d[m-1]; ok && v-m_1 <w {
            return true
        }
        if m_1, ok := d[m+1]; ok && m_1-v < w{
            return true
        }
        d[m] = v
        if i >= k {
            delete(d, nums[i-k]/w)
        }
    }
    return false
}

func abs(x int) int {
    if x < 0 {
        return  -x
    }
    return x
}
