package main

import (
    "fmt"
)

type SqrtError struct{
    Msg string
}

func (se *SqrtError) Error() string {
    return se.Msg
}

func Sqrt(x float64) (float64, error) {
    if x < 0 {
        return -1, &SqrtError{"not support negative one"}
    }
    return 0, nil
}
// cannot do like this
// func Sqrt(x float64) (float64, error) {
//     if x < 0 {
//         return -1, &Error{"not support negative one"}
//     }
//     return 0, nil
// }

func main() {
    fmt.Println(Sqrt(2))
    fmt.Println(Sqrt(-2))
}

