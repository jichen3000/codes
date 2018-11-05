package main

import (
    "fmt"
    "math"
)

func compute(fn func(float64, float64) float64) float64 {
    return fn(3, 4)
}

func another(x, y float64) float64 {
    return math.Sqrt(x*x + y*y)
}
func asValues() {
    hypot := func(x, y float64) float64 {
        return math.Sqrt(x*x + y*y)
    }
    // cannot declare like this one
    // func nested(x, y float64) float64 {
    //     return math.Sqrt(x*x + y*y)
    // }
    fmt.Println(hypot(5, 12))

    fmt.Println(compute(hypot))
    fmt.Println(compute(another))
    fmt.Println(compute(math.Pow))
}

func adder() func(int) int {
    sum := 0
    return func(x int) int {
        sum += x
        return sum
    }
}

func closure() {
    pos, neg := adder(), adder()
    for i := 0; i < 10; i++ {
        fmt.Println(
            pos(i),
            neg(-2*i),
        )
    }
}

func main() {
    asValues()
    closure()
}

