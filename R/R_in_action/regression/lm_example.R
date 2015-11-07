fit <- lm(weight ~ height, data = women)
summary(fit)
women
# according the equation, give the value
# for example, for the height=58, weight=112.5833
fitted(fit)

# the calculated value from equation - the real value
residuals(fit)

plot(women$height,women$weight,
    xlab="Height (in inches)",
    ylab="Weight (in pounds)")
abline(fit)


fit2 <- lm(weight ~ height + I(height^2), data=women)    