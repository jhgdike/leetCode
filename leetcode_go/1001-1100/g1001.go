
func gridIllumination(n int, lamps [][]int, queries [][]int) []int {
	x := make(map[int]int)
	y := make(map[int]int)
	l := make(map[int]int)
	r := make(map[int]int)
	d := make(map[point]bool)
	for _, v := range lamps {
		x_, y_ := v[0], v[1]
		if d[point{x_, y_}] {continue}
		x[x_]++
		y[y_]++
		l[x_+y_]++
		r[x_-y_]++
		d[point{x_, y_}] = true
	}

	ans := make([]int, len(queries))
	for i := 0; i < len(queries); i++ {
		x_, y_ := queries[i][0], queries[i][1]
		if x[x_] > 0 || y[y_] > 0 || l[x_+y_] > 0 || r[x_-y_] > 0 {
			ans[i] = 1
		} else {
			ans[i] = 0
		}

		for k := -1; k <= 1; k++ {
			n_x := x_ + k
			for j := -1; j <= 1; j++ {
				n_y := y_ + j
				if d[point{n_x, n_y}] {
					d[point{n_x, n_y}] = false
					x[n_x]--
					y[n_y]--
					l[n_x+n_y]--
					r[n_x-n_y]--
				}
			}
		}
	}
	return ans
}

type point struct {
	x, y int
}