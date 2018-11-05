package main

import (
    "fmt"
    "math"
)

type Abser interface {
    Abs() float64
}

type MyFloat float64

func (f MyFloat) Abs() float64 {
    if f < 0 {
        return float64(-f)
    }
    return float64(f)
}

type Vertex struct {
    X, Y float64
}

func (v *Vertex) Abs() float64 {
    if v == nil {
        return -1
    }
    return math.Sqrt(v.X*v.X + v.Y*v.Y)
}

func (v *Vertex) Abs2() float64 {
    return math.Sqrt(v.X*v.X + v.Y*v.Y)
}

// func describe(i Abser) {
//     fmt.Printf("(%v, %T)\n", i, i)
// }

func describe(i interface{}) {
    fmt.Printf("(%v, %T)\n", i, i)
}

func main() {
    var a Abser
    f := MyFloat(-math.Sqrt2)
    v := Vertex{3, 4}

    a = f  // a MyFloat implements Abser
    describe(a)
    a = &v // a *Vertex implements Abser

    // In the following line, v is a Vertex (not *Vertex)
    // and does NOT implement Abser.
    //a = v

    fmt.Println(a.Abs())
    // cannot do this
    // fmt.Println(a.Abs2())

    describe(a)

    var theNil Abser
    describe(theNil)

    var t *Vertex
    theNil = t
    fmt.Println(theNil.Abs())

    var nilInterface interface{}
    describe(nilInterface)
}

