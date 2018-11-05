package main

import (
    "fmt"
    "time"
)

func say(s string) {
    for i := 0; i < 5; i++ {
        time.Sleep(100 * time.Millisecond)
        fmt.Println(s)
    }
}

/*
    Goroutines run in the same address space, so access 
    to shared memory must be synchronized. The sync package 
    provides useful primitives, although you won't need 
    them much in Go as there are other primitives. (See the next slide.)
*/
func main() {
    go say("world")
    go say("hello")
}