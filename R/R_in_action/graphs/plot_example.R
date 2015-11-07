dose  <- c(20, 30, 40, 45, 60)
drugA <- c(16, 20, 27, 40, 60)
drugB <- c(15, 18, 25, 31, 40)

# par(lty=2, pch=17)
# plot(dose, drugA, type="b", col="blue")


# n <- 10
# mycolors <- rainbow(n)
# pie(rep(1, n), labels=mycolors, col=mycolors)



# opar <- par(no.readonly=TRUE)
# par(pin=c(2, 3))
# par(lwd=2, cex=1.5)
# par(cex.axis=.75, font.axis=3)
# plot(dose, drugA, type="b", pch=19, lty=2, col="red")
# plot(dose, drugB, type="b", pch=23, lty=6, col="blue", bg="green")
# par(opar)


plot(dose, drugA, type="b",
     col="red", lty=2, pch=2, lwd=2,
     main="Clinical Trials for Drug A",
     sub="This is hypothetical data",
     xlab="Dosage", ylab="Drug Response",
     xlim=c(0, 60), ylim=c(0, 70))