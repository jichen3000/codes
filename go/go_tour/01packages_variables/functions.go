package main

import "fmt"

func add(x, y int) int {
    return x + y
}

func swap(x, y string) (string, string) {
    return y, x
}
// named return values
func split(sum int) (x, y int) {
    x = sum * 4 / 9
    y = sum - x
    return
}
func main() {
    fmt.Println(add(1,3))    
    a, b := swap("h", "w")
    fmt.Println(a, b)
    fmt.Println(split(17))
}