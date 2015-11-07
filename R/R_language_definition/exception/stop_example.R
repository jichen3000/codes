show.stop <- function(x) {
    print(1)
    stop()
    print(2)
}

show.stop()
print("ok")