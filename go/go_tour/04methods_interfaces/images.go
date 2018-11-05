package main

import (
    "fmt"
    "image"
)

// func (img *image.Image) some() {
//     fmt.Println("some")
// }
func main() {
    m := image.NewRGBA(image.Rect(0, 0, 100, 100))
    fmt.Printf("m type %T, \n", m) 
    fmt.Println(m.Bounds())
    fmt.Println(m.At(0, 0).RGBA())
}

