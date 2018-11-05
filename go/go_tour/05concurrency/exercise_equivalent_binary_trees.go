package main



import (
    "fmt"
)


type Tree struct {
    Left  *Tree
    Value int
    Right *Tree
}
/*
           3                             8
      /         \                       / \
     1           8                     3  13
    / \         / \                   / \
   1   2       5   13                1   5
                                    / \    
                                   1   2
*/
// Walk walks the tree t sending all values
// from the tree to the channel ch.
func Walk(t *Tree, ch chan int) {
    walkTree(t, ch)
    close(ch)
}

func walkTree(t *Tree, ch chan int) {
    if t == nil {
        return
    }
    walkTree(t.Left, ch)
    ch <- t.Value
    walkTree(t.Right, ch)
}

// Same determines whether the trees
// t1 and t2 contain the same values.
func Same(t1, t2 *Tree) bool {
    ch1 := make(chan int)
    ch2 := make(chan int)
    go Walk(t1, ch1)
    go Walk(t2, ch2)
    for i := range ch1 {
        if i != <- ch2 {
            return false
        }
    }
    return true
}

func main() {
    tree1 := Tree{nil, 3, nil}
    tree1.Left = &Tree{nil, 1, nil}
    tree1.Left.Left = &Tree{nil, 1, nil}
    tree1.Left.Right = &Tree{nil, 2, nil}
    tree1.Right = &Tree{nil, 13, nil}
    tree1.Right.Left = &Tree{nil, 5, nil}
    tree1.Right.Left.Right = &Tree{nil, 8, nil}
    // ch1 := make(chan int)
    // go Walk(&tree1, ch1)
    // for i := range ch1 {
    //     fmt.Println(i)
    // }
    tree2 := Tree{nil, 8, nil}
    tree2.Right = &Tree{nil, 13, nil}
    tree2.Left = &Tree{nil, 3, nil}
    tree2.Left.Right = &Tree{nil, 5, nil}
    tree2.Left.Left = &Tree{nil, 1, nil}
    tree2.Left.Left.Right = &Tree{nil, 2, nil}
    tree2.Left.Left.Left = &Tree{nil, 1, nil}
    // ch2 := make(chan int)
    // go Walk(&tree2, ch2)
    // for i := range ch2 {
    //     fmt.Println(i)
    // }
    fmt.Println(Same(&tree1, &tree2))
    fmt.Println("end")

}
