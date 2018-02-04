package leetcode_go

func twoSumBinsearch(numbers []int, target int) []int {
	for index, v := range numbers {
		j := binSearch(numbers[index+1:], target-v)
		if j >= 0 {
			return []int{index + 1, index + j + 2}
		}
	}
	return []int{}
}

func twoSum(numbers []int, target int) []int {
	left, right := 0, len(numbers)-1
	for sum := numbers[left] + numbers[right]; sum != target; {
		if sum > target {
			right--
		} else {
			left++
		}
	}
	return []int{left + 1, right + 1}
}
