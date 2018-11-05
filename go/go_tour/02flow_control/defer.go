package main

import "fmt"

func main() {
    defer fmt.Println("world")
    defer fmt.Println("world1")

    fmt.Println("hello")

    defer fmt.Println("aaa")
}

