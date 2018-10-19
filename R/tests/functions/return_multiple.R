# http://stackoverflow.com/questions/1826519/function-returning-more-than-one-value
return_seq <- function(){
    return(c(1,2))
}

return_list <- function(){
    return(list(a=1,b=2))
}

list <- structure(NA,class="result")
"[<-.result" <- function(x,...,value) {
   args <- as.list(match.call())
   args <- args[-c(1:2,length(args))]
   length(value) <- length(args)
   for(i in seq(along=args)) {
     a <- args[[i]]
     if(!missing(a)) eval.parent(substitute(a <- v,list(a=a,v=value[[i]])))
   }
   x
}

if (is.null(sys.frames())){
    suppressPackageStartupMessages(require(minitest))
    # only_test("")
    test("return_seq", {
        return_seq() %equal% c(1,2)

        r_seq <- return_seq()
        r_seq %equal% c(1,2)
        r_seq[1] %equal% 1
    })

    test("return_seq with list", {
        list[a,b] <- return_seq()
        a %equal% 1
        b %equal% 2
    })

    test("return_list",{
        return_list() %equal% list(a=1,b=2)

        r_list <- return_list()
        r_list$a %equal% 1

        list[a,b] <- return_list()
    })

    test("return_seq with list", {
        list[a,b] <- return_seq()
        a %equal% 1
        b %equal% 2
    })
}