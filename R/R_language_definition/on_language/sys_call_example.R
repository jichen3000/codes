f <- function(x, y, ...) sys.call()
f(y = 1, 2, z = 3, 4)

f <- function(x, y, ...) match.call(expand.dots = FALSE)
f(y = 1, 2, z = 3, 4)

# extras <- match.call(expand.dots = FALSE)$...
#      if (length(extras) > 0) {
#          existing <- !is.na(match(names(extras), names(call)))
#          for (a in names(extras)[existing]) call[[a]] <- extras[[a]]
#          if (any(!existing)) {
#              call <- c(as.list(call), extras[!existing])
#              call <- as.call(call)
#          }
# }