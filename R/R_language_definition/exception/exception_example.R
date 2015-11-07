vari <- 1
tryCatch(print("passes"), 
    error = function(e) print(vari), 
    finally=print("finished")) 
tryCatch(stop("fails"), 
    error = function(e) {print(vari);print(e)}, 
    finally=print("finished"))