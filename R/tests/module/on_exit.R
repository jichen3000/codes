## https://stat.ethz.ch/R-manual/R-devel/library/base/html/quit.html

invisible(reg.finalizer(environment(),
        function(e) cat("at last\n"),
        onexit=TRUE))
    # .Last <- function() {
    #   cat("at last\n")
    # }
    print("ok")
