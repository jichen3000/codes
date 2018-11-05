package main

import (
    "fmt"
    "math"
)

type Vertex struct {
    X, Y float64
}

// for type Vertex
func (v Vertex) Abs() float64 {
    return math.Sqrt(v.X * v.X + v.Y * v.Y)
}

func Abs(v Vertex) float64 {
    return math.Sqrt(v.X*v.X + v.Y*v.Y)
}

type MyFloat float64

// You can only declare a method with a receiver whose type is defined in the same package as the method. 
// You cannot declare a method with a receiver whose type is defined in another package (which includes the built-in types such as int).
func (f MyFloat) Abs() float64 {
    if f < 0 {
        return float64(-f)
    }
    return float64(f)
}

// see difference, using point, would impact the origin ore
// using normal var, would not impact the origin ore
func (v *Vertex) Scale(f float64) {
    v.X = v.X * f
    v.Y = v.Y * f
}

func main() {
    v := Vertex{3, 4}
    fmt.Println(v.Abs())
    fmt.Println(Abs(v))
    fmt.Println(MyFloat(10).Abs())

    v.Scale(10)
    fmt.Println(v.Abs())
}

