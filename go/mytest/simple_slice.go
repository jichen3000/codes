package main

import (
    "fmt"
    // "strings"
)

func printSlice(s []int) {
    fmt.Printf("len=%d cap=%d %v\n", len(s), cap(s), s)
}

func main() {
    s := []int{2, 3, 5, 7, 11, 13}
    s2 := []int{2, 3, 5, 7, 11, 13}
    s3 := append(s, s2...)
    printSlice(s3)
}