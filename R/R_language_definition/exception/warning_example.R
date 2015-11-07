show.warning <- function(warn_value) {
    options(warn = warn_value)
    print(options("warn"))
    print(1)
    warning("warning")
    print(2)
}
show.warning(-1)
show.warning(0)
show.warning(1)
show.warning(10)

print("ok")