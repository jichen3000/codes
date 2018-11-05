package main

import (
    "fmt"
    "strings"
)

func printSlice(s []int) {
    fmt.Printf("len=%d cap=%d %v\n", len(s), cap(s), s)
}

func printSliceWithName(s string, x []int) {
    fmt.Printf("%s len=%d cap=%d %v\n",
        s, len(x), cap(x), x)
}

func makeSlices() {
    a := make([]int, 5)
    printSliceWithName("a", a)

    b := make([]int, 0, 5)
    printSliceWithName("b", b)

    c := b[:2]
    printSliceWithName("c", c)

    d := c[2:5]
    printSliceWithName("d", d)
}

func sliceOfSlice() {
    // Create a tic-tac-toe board.
    board := [][]string{
        []string{"_", "_", "_"},
        []string{"_", "_", "_"},
        []string{"_", "_", "_"},
    }

    // The players take turns.
    board[0][0] = "X"
    board[2][2] = "O"
    board[1][2] = "X"
    board[1][0] = "O"
    board[0][2] = "X"

    for i := 0; i < len(board); i++ {
        fmt.Printf("%s\n", strings.Join(board[i], " "))
    }
}

func appendSlice() {
    var s []int
    printSlice(s)

    // append works on nil slices.
    s = append(s, 0)
    printSlice(s)

    // The slice grows as needed.
    s = append(s, 1)
    printSlice(s)

    // We can add more than one element at a time.
    s = append(s, 2, 3, 4)
    printSlice(s)
}

func main() {
    var aa [2]string
    aa[0] = "Hello"
    aa[1] = "World"
    fmt.Printf("%T \n", aa)    
    fmt.Println(aa[0], aa[1])
    fmt.Println(aa)

    primes := [6]int{2, 3, 5, 7, 11, 13}
    fmt.Println(primes)

    var ss []int = primes[1:4]
    fmt.Println(ss)

    names := [4]string{
        "John",
        "Paul",
        "George",
        "Ringo",
    }
    fmt.Println(names)

    // slices
    a := names[0:2]
    b := names[1:3]
    fmt.Println(a, b)

    b[0] = "XXX"
    fmt.Println(a, b)
    fmt.Println(names) 

    // q is slice, not array, no length
    q := []int{2, 3, 5, 7, 11, 13}
    fmt.Println(q)

    r := []bool{true, false, true, true, false, true}
    fmt.Printf("%T \n", r)
    fmt.Println(r)

    s1 := []struct {
        i int
        b bool
    }{
        {2, true},
        {3, false},
        {5, true},
        {7, true},
        {11, false},
        {13, true},
    }
    fmt.Printf("%T \n", s1)
    fmt.Println(s1)   

    s := []int{2, 3, 5, 7, 11, 13}

    s = s[1:4]
    printSlice(s)

    s = s[:2]
    printSlice(s)

    s = s[1:]
    printSlice(s) 

    var nilArr []int
    fmt.Println(nilArr, len(nilArr), cap(nilArr))
    if nilArr == nil {
        fmt.Println("nil!")
    }        

    makeSlices() 

    sliceOfSlice()  

    appendSlice()    
}

