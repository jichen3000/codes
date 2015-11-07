manager <- c(1, 2, 3, 4, 5)
date <- c("10/24/08", "10/28/08", "10/1/08", "10/12/08", "5/1/09")
country <- c("US", "US", "UK", "UK", "UK")
gender <- c("M", "F", "F", "M", "F")
age <- c(32, 45, 25, 39, 99)
q1 <- c(5, 3, 3, 3, 2)
q2 <- c(4, 5, 5, 3, 2)
q3 <- c(5, 2, 5, 4, 1)
q4 <- c(5, 5, 5, NA, 2)
q5 <- c(5, 5, 2, NA, 1)
leadership <- data.frame(manager, date, country, gender, age, 
        q1, q2, q3, q4, q5, stringsAsFactors=FALSE)
leadership

# recoding
leadership$age[leadership$age == 99] <- NA

leadership <- within(leadership, {
    agecat <- NA
    agecat[age > 75] <- "Elder"
    agecat[age >= 55 & age <= 75] <- "Middle Aged"
    agecat[age < 55] <- "Young"
    })
leadership

# chooseCRANmirror(ind=89)
# install.packages("reshape")
# fix(leadership)
library(reshape)
newL <- rename(leadership,
                     c(manager="managerID", date="testDate")
)
newL

is.na(leadership[,6:10])

na.omit(leadership)

leadership[order(leadership$gender, -leadership$age),]

myvars <- c("q1", "q2", "q3", "q4", "q5")
leadership[myvars]

myvars <- names(leadership) %in% c("q3", "q4")
myvars
leadership[!myvars]

leadership[c(-8,-9)]

leadership[1:3,]
leadership[which(leadership$gender=="M" & leadership$age > 30),]

leadership$date <- as.Date(leadership$date, "%m/%d/%y")
startdate <- as.Date("2009-01-01")
enddate   <- as.Date("2009-10-31")
leadership[which(leadership$date >= startdate &
leadership$date <= enddate),]


subset(leadership, age >= 35 | age < 24,
                          select=c(q1, q2, q3, q4))
subset(leadership, gender=="M" & age > 25,
                          select=gender:q4)

leadership[sample(1:nrow(leadership), 3, replace=FALSE),]                                                    