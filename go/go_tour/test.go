// package main

// import (
// 	"fmt"
// )

// func main() {
// 	fmt.Println("Hello, playground")
// }


package main

import "fmt"

type Car struct{
    year int
    make string
}

func (c *Car)String() string{
    return fmt.Sprintf("{make:%s, year:%d}", c.make, c.year)
}

func main() {
    myCar := Car{year:1996, make:"Toyota"}
    fmt.Println(&myCar)
}