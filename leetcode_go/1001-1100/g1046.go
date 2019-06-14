package main

import (
	"container/heap"
)

func lastStoneWeight(stones []int) int {
	if stones == nil || len(stones) == 0 {
		return 0
	}

	stoneHeap := IntHeap(stones)
	s := &stoneHeap
	heap.Init(s)
	for ; s.Len() > 1; {
		a := heap.Pop(s)
		b := heap.Pop(s)
		if a != b {
			heap.Push(s, a.(int) - b.(int))
		}
	}
	if s.Len() == 0 {
		return 0
	}
	return heap.Pop(s).(int)
}

type IntHeap []int

func (h IntHeap) Len() int           { return len(h) }
func (h IntHeap) Less(i, j int) bool { return h[i] > h[j] }
func (h IntHeap) Swap(i, j int)      { h[i], h[j] = h[j], h[i] }

func (h *IntHeap) Push(x interface{}) {
	// Push and Pop use pointer receivers because they modify the slice's length,
	// not just its contents.
	*h = append(*h, x.(int))
}

func (h *IntHeap) Pop() interface{} {
	old := *h
	n := len(old)
	x := old[n-1]
	*h = old[0 : n-1]
	return x
}

func main() {
	//res := lastStoneWeight([]int{2, 7, 4, 1, 8, 1})
	res := lastStoneWeight([]int{2, 2})
	println(res)
}
