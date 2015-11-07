print("step 2: data collection")
print("load data from csv, and notice the null value")
train.data = read.csv("train.csv", na.strings=c("NA", ""))
print(str(train.data))

train.data$Survived = factor(train.data$Survived)
train.data$Pclass = factor(train.data$Pclass)

print(str(train.data))

# train.data$Survived[train.data$Survived==1] = "Y"
# train.data$Survived[train.data$Survived==0] = "N"
# train.data$Survived = factor(train.data$Survived)

# print(str(train.data))

print("step 3: data wrangling")
print("impute the values")
# missing value
# is.na(train.data$Age)
sum(is.na(train.data$Age) == TRUE)
sum(is.na(train.data$Age) == TRUE) / length(train.data$Age)
options(digits=2)

sapply(train.data, function(df){
        sum(is.na(df)==TRUE)/length(df)
    })

# require(Amelia)
# missmap(train.data, main="Missing Map")

# see na
print("impute Embarked")
sum(is.na(train.data$Embarked))
train.data[which(is.na(train.data$Embarked)),]
table(train.data$Embarked, useNA="always")
# since the most people embarked at S, so we choose the S
train.data$Embarked[which(is.na(train.data$Embarked))] = 'S';
table(train.data$Embarked, useNA = "always")

print("find indexes which of the name including .")
train.data$Name = as.character(train.data$Name)
# train.data$Name

table_words = table(unlist(strsplit(train.data$Name, "\\s+")))
# table_words
# unlist(strsplit(train.data$Name, "\\s+"))
# grep('\\.', names(table_words))
# names(table_words)
# sort(table_words [grep('\\.',names(table_words))], decreasing=TRUE)

require(stringr)
# str_match(train.data$Name, " [a-zA-Z]+\\.")
# train.data[671,]
# train.data$Name[671]

tb = cbind(train.data$Age, str_match(train.data$Name, " [a-zA-Z]+\\."))

print("impute Age with the mean group by title")
mean.mr = mean(train.data$Age[grepl(" Mr\\.", train.data$Name) &
!is.na(train.data$Age)])
mean.mrs = mean(train.data$Age[grepl(" Mrs\\.", train.data$Name) &
!is.na(train.data$Age)])
mean.dr = mean(train.data$Age[grepl(" Dr\\.", train.data$Name) &
!is.na(train.data$Age)])
mean.miss = mean(train.data$Age[grepl(" Miss\\.", train.data$Name) &
!is.na(train.data$Age)])
mean.master =  mean(train.data$Age[grepl(" Master\\.",
train.data$Name) & !is.na(train.data$Age)])

train.data$Age[grepl(" Mr\\.", train.data$Name) &
is.na(train.data$Age)] = mean.mr
train.data$Age[grepl(" Mrs\\.", train.data$Name) &
is.na(train.data$Age)] = mean.mrs
train.data$Age[grepl(" Dr\\.", train.data$Name) &
is.na(train.data$Age)] = mean.dr
train.data$Age[grepl(" Miss\\.", train.data$Name) &
is.na(train.data$Age)] = mean.miss
train.data$Age[grepl(" Master\\.", train.data$Name) &
is.na(train.data$Age)] = mean.master

sum(is.na(train.data$Age)==TRUE)

print("step 4: basic")
# barplot(table(train.data$Survived), main="Passenger Survival",
#     names= c("Perished", "Survived"))
# barplot(table(train.data$Pclass), main="Passenger Class",  names=
#    c("first", "second", "third"))
# barplot(table(train.data$Sex), main="Passenger Gender")
# hist(train.data$Age, main="Passenger Age", xlab = "Age")
# # second as colomns, first as rows
# counts = table( train.data$Survived, train.data$Pclass)
# counts
# # columns is the bar
# barplot(counts,  col=c("darkblue","red"), legend =c("Perished",
#     "Survived"), main= "Titanic Class Bar Plot" )

# hist(train.data$Age[which(train.data$Survived == "0")], main=
#     "Passenger Age Histogram", xlab="Age", ylab="Count", col ="blue",
#     breaks=seq(0,80,by=2))
# hist(train.data$Age[which(train.data$Survived == "1")], col ="red",
#     add = T, breaks=seq(0,80,by=2))

# boxplot(train.data$Age ~ train.data$Survived,
#         main="Passenger Survival by Age",
#         xlab="Survived", ylab="Age")

print("step 5: advanced")
# train.child = train.data$Survived[train.data$Age < 13]
# length(train.child[which(train.child == 1)] ) / length(train.child)
# train.youth = train.data$Survived[train.data$Age >= 15 &
# train.data$Age < 25]
# length(train.youth[which(train.youth == 1)] ) / length(train.youth)
# train.adult  = train.data$Survived[train.data$Age >= 20 &
# train.data$Age < 65]
# length(train.adult[which(train.adult == 1)] ) / length(train.adult)
# train.senior  = train.data$Survived[train.data$Age >= 65]
# length(train.senior[which(train.senior == 1)] ) /
# length(train.senior)

# mosaicplot(train.data$Pclass ~ train.data$Survived,
#             main="Passenger Survival Class", color=TRUE,
#             xlab="Pclass", ylab="Survived")


print("step 6: model assessment")
split.data = function(data, p=0.7, seed=666){
    set.seed(seed)
    row_count = dim(data)[1]
    index = sample(1:row_count)
    train_count = floor(row_count * p)
    train = data[index[1:train_count], ]
    test = data[index[(train_count+1):row_count], ]
    return (list(train=train, test=test))
}
allset= split.data(train.data, p = 0.7)
trainset = allset$train
testset = allset$test

#install.packages('party')
require('party')
train.ctree = ctree(Survived ~ Pclass + Sex + Age + SibSp + Fare +
        Parch + Embarked, data=trainset)
train.ctree
# plot(train.ctree, main="Conditional inference tree of Titanic
#         Dataset")

ctree.predict = predict(train.ctree, testset)
ctree.predict

# install.packages("caret")
require(caret)
confusionMatrix(ctree.predict, testset$Survived)

# install.packages('e1071')
require('e1071')
svm.model = svm(Survived ~ Pclass + Sex + Age + SibSp + Fare + Parch +
        Embarked, data = trainset, probability = TRUE)
svm.model

svm.predict = predict(svm.model, testset)
svm.predict

confusionMatrix(svm.predict, testset$Survived)




