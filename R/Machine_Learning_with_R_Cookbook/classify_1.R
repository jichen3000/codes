# install.packages("C50")
library(C50)
data(churn)

str(churnTrain)
churnTrain = churnTrain[,! names(churnTrain) %in% c("state",
    "area_code", "account_length") ]

set.seed(2)
ind = sample(2, nrow(churnTrain), replace = TRUE, prob=c(0.7, 0.3))
trainset = churnTrain[ind == 1,]
testset = churnTrain[ind == 2,]
dim(trainset)
dim(testset)

split.data = function(data, p=0.7, seed=666){
    set.seed(seed)
    row_count = dim(data)[1]
    index = sample(1:row_count)
    train_count = floor(row_count * p)
    train = data[index[1:train_count], ]
    test = data[index[(train_count+1):row_count], ]
    return (list(train=train, test=test))
}

# decision tree
library(rpart)
churn.rp = rpart(churn ~ ., data=trainset)
churn.rp
printcp(churn.rp)
# plotcp(churn.rp)

# plot(churn.rp, margin= 0.1)
# text(churn.rp, all=TRUE, use.n = TRUE)

# plot(churn.rp, uniform=TRUE, branch=0.6, margin=0.1)
# text(churn.rp, all=TRUE, use.n = TRUE)

predictions = predict(churn.rp, testset, type="class")

# Measuring the prediction performance of
# a recursive partitioning tree
table(testset$churn, predictions)

# library(caret)
# confusionMatrix(table(predictions, testset$churn))

# Pruning a recursive partitioning tree

min(churn.rp$cptable[,"xerror"])
which.min(churn.rp$cptable[,"xerror"])
churn.cp = churn.rp$cptable[7,"CP"]
churn.cp
prune.tree = prune(churn.rp, cp= churn.cp)

library(party)
ctree.model = ctree(churn ~ . , data = trainset)
ctree.model

# plot(ctree.model)

ctree.predict = predict(ctree.model ,testset)
table(ctree.predict, testset$churn)
library(caret)
confusionMatrix(table(ctree.predict, testset$churn))

# k-nearest neighbor classifier
# install.packages("class")
library(class)

levels(trainset$international_plan) = list("0"="no", "1"="yes")
levels(trainset$voice_mail_plan) = list("0"="no", "1"="yes")
levels(testset$international_plan) = list("0"="no", "1"="yes")
levels(testset$voice_mail_plan) = list("0"="no", "1"="yes")
churn.knn = knn(trainset[,! names(trainset) %in% c("churn")],
    testset[,! names(testset) %in% c("churn")], trainset$churn, k=3)
summary(churn.knn)
table(testset$churn, churn.knn)
confusionMatrix(table(testset$churn, churn.knn))

# logistic regression
fit = glm(churn ~ ., data = trainset, family=binomial)
summary(fit)

fit = glm(churn ~ international_plan +
    voice_mail_plan+total_intl_calls+number_customer_service_calls, data =
    trainset, family=binomial)
summary(fit)

pred = predict(fit,testset, type="response")
Class = pred > .5
summary(Class)

table(testset$churn,Class)

churn.mod = ifelse(testset$churn == "yes", 1, 0)
pred_class = churn.mod
pred_class[pred<=.5] = 1- pred_class[pred<=.5]
ctb = table(churn.mod, pred_class)
ctb
confusionMatrix(ctb)

# naive bayes
library(e1071)
classifier=naiveBayes(trainset[, !names(trainset) %in% c("churn")],
    trainset$churn)
classifier
bayes.table = table(predict(classifier, testset[, !names(testset)
    %in% c("churn")]), testset$churn)
bayes.table
confusionMatrix(bayes.table)


