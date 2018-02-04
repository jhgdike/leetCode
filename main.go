package main

import (
	"fmt"
)

func twoSum(numbers []int, target int) []int {
	left, right := 0, len(numbers)-1
	for sum := numbers[left] + numbers[right]; sum != target; {
		if sum > target {
			right--
		} else {
			left++
		}
		sum = numbers[left] + numbers[right]
	}
	return []int{left + 1, right + 1}
}
func main() {
	twoSum([]int{0, 0, 3, 4}, 0)
}
