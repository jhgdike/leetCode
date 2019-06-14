package leetcode

func minDeletionSize(A []string) int {
	var count int
	if A == nil || len(A) == 0 {
		return count
	}
	for i := 0; i < len(A[0]); i++ {
		ok := true
		for j := 1; j < len(A); j++ {
			if A[j-1][i] > A[j][i] {
				ok = false
				break
			}
		}
		if !ok {
			count++
		}
	}
	return count
}
