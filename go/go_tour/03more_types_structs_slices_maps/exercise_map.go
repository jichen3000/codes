package main

import (
    "golang.org/x/tour/wc"
    "strings"
)

func WordCount(s string) map[string]int {
    counter := make(map[string]int)
    for _, v := range strings.Fields(s) {
        counter[v] += 1
    }
    return counter
}

func main() {
    wc.Test(WordCount)
}