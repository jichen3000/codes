# install.packages("car")
require(car)

str(Quartet)

# plot(Quartet$x, Quartet$y1)
lmfit = lm(y1~x, Quartet)
# abline(lmfit, col="red")

lmfit

newdata = data.frame(x = c(3,6,15))
predict(lmfit, newdata, interval="confidence", level=0.95)
predict(lmfit, newdata, interval="predict")

# Diagnostic plots of the regression model, P324
# par(mfrow=c(2,2))
# plot(lmfit)

# polynomial, x's square
lmfit = lm(Quartet$y2~poly(Quartet$x,2))
lines(sort(Quartet$x), lmfit$fit[order(Quartet$x)], col = "red")

# plot(Quartet$x, Quartet$y2)
lmfit = lm(Quartet$y2~ I(Quartet$x)+I(Quartet$x^2))

# plot(Quartet$x, Quartet$y3)

library(MASS)
lmfit = rlm(Quartet$y3~Quartet$x)
# abline(lmfit, col="red")

# the Survey of Labor and Income Dynamics (SLID) dataset.


lmfit = lm(wages ~ ., data = SLID)
summary(lmfit)

lmfit = lm(wages ~ age + sex + education, data = SLID)
summary(lmfit)
# par(mfrow=c(2,2))
# plot(lmfit)

lmfit = lm(log(wages) ~ age + sex + education, data = SLID)
summary(lmfit)
# par(mfrow=c(2,2))
# plot(lmfit)

# detect multi-colinearity, 
# if a variable square root is larger than 2, it is colinearity.
vif(lmfit)
sqrt(vif(lmfit)) > 2

# heteroscedasticity
# install.packages("lmtest")
library(lmtest)
bptest(lmfit)

# Generalized linear model(GLM)
lmfit1 = glm(wages ~ age + sex + education, data = SLID,
    family=gaussian)
summary(lmfit1)

lmfit2 = lm(wages ~ age + sex + education, data = SLID)
summary(lmfit2)