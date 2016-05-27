vari <- 1
tryCatch(print("passes"), 
    error = function(e) print(vari), 
    finally=print("finished")) 
tryCatch(stop("fails"), 
    error = function(e) {
        print(vari);print(e)
    }, 
    finally=print("finished"))

cause_error <- function(){
    tryCatch(ppp(), 
        error = show_error, 
        finally=print("finished"))    
}
show_error <- function(e){
    print(vari);print(e)

}