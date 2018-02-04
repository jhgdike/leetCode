package leetcode_go

import (
	"fmt"
	"testing"
)

func Test2Search(t *testing.T) {
	nums := []int{1, 2, 3, 4, 7, 8, 9, 10}
	res := binSearch(nums, 8)
	if res != 5 {
		t.Error("binsearch error", res)
	}
}

func TestTwoSum(t *testing.T) {
	nums := []int{1, 2, 3, 4, 7, 8, 9, 10}
	fmt.Println(twoSum(nums, 13))
}
