package main

import "fmt"

func main() {
    i, j := 42, 2701
    f := false

    p:= &i
    fmt.Printf("%T, %v \n", p, p)
    fmt.Println(*p)

    // cannot 
    // p = &f

    p = &j
    fmt.Println(*p)

    *p = 8
    fmt.Println(*p, j)

    fmt.Println(f)
}