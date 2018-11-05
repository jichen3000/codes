package main

import (
    "fmt"
    "math"
)

func pow(x, n, lim float64) float64 {
    if v := math.Pow(x, n); v < lim {
        return v
    }
    return lim
}

func main() {
    sum := 1
    for ; sum < 1000; {
        sum += sum
    }
    fmt.Println(sum)

    sum1 := 1
    for sum1 < 1000 {
        sum1 += sum1
    }
    fmt.Println(sum1)
    // forever
    // for {
    // }

    fmt.Println(
        pow(3, 2, 10),
        pow(3, 3, 20),
    ) 
    if sum1 < 1000 {
        fmt.Println("1")
    } else if sum1 > 2000{
        fmt.Println("2")
    } else {
        fmt.Println("3")
    }
}