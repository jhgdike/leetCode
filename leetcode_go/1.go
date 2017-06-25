func twoSum(nums []int, target int) []int {
    m := map[int]int{}
    for i, n := range nums {
        if j, ok := m[target - n]; ok {
            return []int{j, i}
        }
        m[n] = i
    }
    panic("aaa")
}
