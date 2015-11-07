ex <- expression(2 + 2, 3 + 4)
mode(ex)
ex[[1]]
mode(ex[[1]])
eval(ex)