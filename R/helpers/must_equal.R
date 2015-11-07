
must.equal <- function(actual, expect){
}

show.report <- function(){
    print("show.report:")
}


if (is.null(sys.frames())){
    must.equal("","")
    on.exit(print("in "))
    # exit()
    print("done")
}

