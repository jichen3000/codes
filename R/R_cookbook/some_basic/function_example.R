cv <- function(x) sd(x)/mean(x)
cv(1:10)

cv2 <- function(x) {
    sd(x)/mean(x)
}
cv2(1:10)

lapply(list(1:10, 2:11), cv)
lapply(list(1:10, 2:11), function(x) sd(x)/mean(x))