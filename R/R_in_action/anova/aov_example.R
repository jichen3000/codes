library(multcomp)
attach(cholesterol)
table(trt)

aggregate(response, by=list(trt), FUN=mean)
aggregate(response, by=list(trt), FUN=sd)


fit <- aov(response ~ trt)
summary(fit)

library(gplots)

# The ANOVA F test for treatment (trt) is significant (p < .0001), providing evidence that the five treatments aren’t all equally effective
# plotmeans(response ~ trt, xlab="Treatment", ylab="Response",
#      main="Mean Plot\nwith 95% CI")

TukeyHSD(fit)

par(las=2)
par(mar=c(5,8,4,2))
plot(TukeyHSD(fit))