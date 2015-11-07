f <- function(x) {
    print(x)
}

body(f)
formals(f)
environment(f)
# body<-(f)
# formals<-(f)
# environment<-(f)
as.list(f)
as.function(as.list(f))