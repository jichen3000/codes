# k-fold cross-validation
ind = cut(1:nrow(churnTrain), breaks=10, labels=F)
require(e1071)
accuracies = c()
for (i in 1:10) {
    fit = svm(churn ~., churnTrain[ind != i,])
    predictions = predict(fit, churnTrain[ind == i, ! names(churnTrain)
        %in% c("churn")])
    correct_count = sum(predictions == churnTrain[ind == i,c("churn")])
    accuracies = append(correct_count / nrow(churnTrain[ind == i,]), accuracies)
}

accuracies
mean(accuracies)


## also can use tune.svm: others tune.nnet, tune.randomForest, tune.rpart, and tune.knn
library(C50)
set.seed(2)
ind = sample(2, nrow(churnTrain), replace = TRUE, prob=c(0.7, 0.3))
trainset = churnTrain[ind == 1,]
testset = churnTrain[ind == 2,]
dim(trainset)
dim(testset)
tuned = tune.svm(churn~., data = trainset, gamma = 10^-2, cost =
    10^2, tunecontrol=tune.control(cross=10))
summary(tuned)
tuned$performances

svmfit = tuned$best.model
table(trainset[,c("churn")], predict(svmfit))

# ?e1071::tune

## library caret
library(caret)
control = trainControl(method="repeatedcv", number=10, repeats=3)
model = train(churn~., data=trainset, method="rpart",
    preProcess="scale", trControl=control)
model

## Ranking the variable importance
importance = varImp(model, scale=FALSE)
importance
# plot(importance)

library(rpart)
model.rp = rpart(churn~., data=trainset)
model.rp$variable.importance

install.packages("rminer")
library(rminer)
model=fit(churn~.,trainset,model="svm")
VariableImportance=Importance(model,trainset,method="sensv")
L=list(runs=1,sen=t(VariableImportance$imp),sresponses=VariableImportance$sresponses)
mgraph(L,graph="IMP",leg=names(trainset),col="gray",Grid=10)

## Finding highly correlated features
library(caret)
new_train = trainset[,! names(churnTrain) %in% c("churn",
    "international_plan", "voice_mail_plan", "area_code", "state")]
cor_mat = cor(new_train)
highlyCorrelated = findCorrelation(cor_mat, cutoff=0.75)
names(new_train)[highlyCorrelated]

# select features
intl_plan = model.matrix(~ trainset.international_plan - 1,
    data=data.frame(trainset$international_plan))
colnames(intl_plan) = c("trainset.international_planno"="intl_no",
    "trainset.international_planyes"= "intl_yes")
voice_plan = model.matrix(~ trainset.voice_mail_plan - 1,
    data=data.frame(trainset$voice_mail_plan))
colnames(voice_plan) = c("trainset.voice_mail_planno" ="voice_no",
    "trainset.voice_mail_planyes"="voidce_yes")
trainset$international_plan = NULL
trainset$voice_mail_plan = NULL
trainset = cbind(intl_plan,voice_plan, trainset)
intl_plan = model.matrix(~ testset.international_plan - 1,
    data=data.frame(testset$international_plan))
colnames(intl_plan) = c("testset.international_planno"="intl_no",
    "testset.international_planyes"= "intl_yes")
voice_plan = model.matrix(~ testset.voice_mail_plan - 1,
    data=data.frame(testset$voice_mail_plan))
colnames(voice_plan) = c("testset.voice_mail_planno" ="voice_no",
"testset.voice_mail_planyes"="voidce_yes")
testset$international_plan = NULL
testset$voice_mail_plan = NULL
testset = cbind(intl_plan,voice_plan, testset)

trainset$area_code = NULL
testset$area_code = NULL
trainset$state = NULL
testset$state = NULL

ldaControl = rfeControl(functions = ldaFuncs, method = "cv")
install.packages("pROC")
ldaProfile = rfe(trainset[, !names(trainset) %in% c("churn")],
    trainset[,c("churn")],sizes = c(1:18), rfeControl = ldaControl)
ldaProfile

plot(ldaProfile, type = c("o", "g"))
ldaProfile$optVariables

ldaProfile$fit

postResample(predict(ldaProfile, testset[, !names(testset) %in%
    c("churn")]), testset[,c("churn")])

## measuring the performance
library(car)
data(Quartet)
plot(Quartet$x, Quartet$y3)
lmfit = lm(Quartet$y3~Quartet$x)
abline(lmfit, col="red")

### root mean square
predicted= predict(lmfit, newdata=Quartet[c("x")])
actual = Quartet$y3
rmse = (mean((predicted - actual)^2))^0.5
rmse

### relative square error
mu = mean(actual)
rse = mean((predicted - actual)^2) / mean((mu - actual)^2)
rse

### R-Square
rsquare = 1 - rse
rsquare

### rlm
library(MASS)
plot(Quartet$x, Quartet$y3)
rlmfit = rlm(Quartet$y3~Quartet$x)
abline(rlmfit, col="red")
predicted = predict(rlmfit, newdata=Quartet[c("x")])
actual = Quartet$y3
rmse = (mean((predicted - actual)^2))^0.5
rmse
mu = mean(actual)
rse =mean((predicted - actual)^2) / mean((mu - actual)^2)
rse
rsquare = 1 - rse
rsquare

svm.model=train(churn ~ .,
                data = trainset,
                method = "svmRadial")
svm.pred = predict(svm.model, testset[,! names(testset) %in% c("churn")])

table(svm.pred, testset[,c("churn")])
confusionMatrix(svm.pred, testset[,c("churn")])

## Measuring prediction performance
install.packages("ROCR")
library(ROCR)
svmfit=svm(churn~ ., data=trainset, prob=TRUE)
pred=predict(svmfit,testset[, !names(testset) %in% c("churn")],
    probability=TRUE)
pred.prob = attr(pred, "probabilities")
pred.to.roc = pred.prob[, 2]
pred.rocr = prediction(pred.to.roc, testset$churn)
perf.rocr = performance(pred.rocr, measure = "auc", x.measure =
    "cutoff")
perf.tpr.rocr = performance(pred.rocr, "tpr","fpr")

plot(perf.tpr.rocr, colorize=T,main=paste("AUC:",
    (perf.rocr@y.values)))

## choose the fittest model
install.packages("pROC")
library("pROC")
control = trainControl(method = "repeatedcv",
    number = 10,
    repeats = 3,
    classProbs = TRUE,
    summaryFunction = twoClassSummary)
glm.model= train(churn ~ .,
                    data = trainset,
                    method = "glm",
                    metric = "ROC",
                    trControl = control)
svm.model= train(churn ~ .,
                  data = trainset,
                  method = "svmRadial",
                  metric = "ROC",
                  trControl = control)
rpart.model= train(churn ~ .,
                  data = trainset,
                  method = "rpart",
                  metric = "ROC",
                  trControl = control)
glm.probs = predict(glm.model, testset[,! names(testset) %in%
    c("churn")], type = "prob")
svm.probs = predict(svm.model, testset[,! names(testset) %in%
    c("churn")], type = "prob")
rpart.probs = predict(rpart.model, testset[,! names(testset) %in%
    c("churn")], type = "prob")

glm.ROC = roc(response = testset[,c("churn")],
               predictor =glm.probs$yes,
               levels = levels(testset[,c("churn")]))
plot(glm.ROC, type="S", col="red")
svm.ROC = roc(response = testset[,c("churn")],
               predictor =svm.probs$yes,
               levels = levels(testset[,c("churn")]))
plot(svm.ROC, add=TRUE, col="green")
rpart.ROC = roc(response = testset[,c("churn")],
               predictor =rpart.probs$yes,
               levels = levels(testset[,c("churn")]))
plot(rpart.ROC, add=TRUE, col="blue")

### Measuring performance
cv.values = resamples(list(glm = glm.model, svm=svm.model, rpart =
    rpart.model))
summary(cv.values)
dotplot(cv.values, metric = "ROC")
bwplot(cv.values, layout = c(3, 1))