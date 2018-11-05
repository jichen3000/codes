package main

import "fmt"

type Vertex struct {
    Lat, Long float64
}

func mapSimple() {
    var m map[string]Vertex
    m = make(map[string]Vertex)
    m["Bell Labs"] = Vertex{
        40.68433, -74.39967,
    }
    fmt.Println(m["Bell Labs"])
}
func mapLiterals() {
    var m = map[string]Vertex{
        "Bell Labs": Vertex{
            40.68433, -74.39967,
        },
        "Google": Vertex{
            37.42202, -122.08408,
        },
    }    
    fmt.Println(m)
}

func mapOmitStruct() {
    var m = map[string]Vertex{
        "Bell Labs": {40.68433, -74.39967},
        "Google":    {37.42202, -122.08408},
    }
    fmt.Println(m)
}

func operate() {
    m := make(map[string]int)

    m["Answer"] += 1
    fmt.Println("The value:", m["Answer"])

    m["Answer"] = 48
    fmt.Println("The value:", m["Answer"])

    delete(m, "Answer")
    fmt.Println("The value:", m["Answer"])

    v, ok := m["Answer"]
    fmt.Println("The value:", v, "Present?", ok)
}

func main() {
    mapSimple()
    mapLiterals()
    mapOmitStruct()
    operate()
}