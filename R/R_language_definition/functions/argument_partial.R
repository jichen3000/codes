# show the arguments partial matching
foo <- function(fumble, fooey){
    print("ok")
}

# wrong, cannot match the first one
# foo(f=1, fo=2)
foo(fum=1, fo=2)