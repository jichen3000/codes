# Load vcd package
library(vcd)

# Get cell counts for improved variable
counts <- table(Arthritis$Improved)
counts

# simple bar plot
barplot(counts, main = "Simple Bar Plot", xlab = "Improvement", 
    ylab = "Frequency")

plot(Arthritis$Improved, horiz=TRUE, main="Horizontal Bar Plot",
               xlab="Frequency", ylab="Improved")    


counts <- table(Arthritis$Improved, Arthritis$Treatment)
counts

# stacked barplot
barplot(counts, main = "Stacked Bar Plot", xlab = "Treatment", 
    ylab = "Frequency", col = c("red", "yellow", "green"), 
    legend = rownames(counts))

# grouped barplot
barplot(counts, main = "Grouped Bar Plot", xlab = "Treatment", 
    ylab = "Frequency", col = c("red", "yellow", "green"), 
    legend = rownames(counts), 
    beside = TRUE)

states <- data.frame(state.region, state.x77)
means <- aggregate(states$Illiteracy, by=list(state.region), FUN=mean)
means <- means[order(means$x),]
barplot(means$x, names.arg=means$Group.1)

# change the graphs
par(mar=c(5,8,4,2))
par(las=2)
counts <- table(Arthritis$Improved)
barplot(counts,
           main="Treatment Outcome",
           horiz=TRUE, cex.names=0.8,
        names.arg=c("No Improvement", "Some Improvement",
                    "Marked Improvement"))


library(vcd)
attach(Arthritis)
counts <- table(Treatment, Improved)
spine(counts, main="Spinogram Example")
detach(Arthritis)



par(mfrow = c(2, 2))
slices <- c(10, 12, 4, 16, 8)
lbls <- c("US", "UK", "Australia", "Germany", "France")

pie(slices, labels = lbls, main = "Simple Pie Chart")

pct <- round(slices/sum(slices) * 100)
lbls2 <- paste(lbls, " ", pct, "%", sep = "")
pie(slices, labels = lbls2, col = rainbow(length(lbls)), 
    main = "Pie Chart with Percentages")

library(plotrix)
pie3D(slices, labels = lbls, explode = 0.1, main = "3D Pie Chart ")

mytable <- table(state.region)
lbls <- paste(names(mytable), "\n", mytable, sep = "")
pie(mytable, labels = lbls, 
    main = "Pie Chart from a Table\n (with sample sizes)")
