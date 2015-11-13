



# perdict_with_bagging <- function(){
#     library(ipred)
#     set.seed(2)
#     reg_bagging <- bagging(Sales~DayOfWeek+Promo, data=train_set_83, coob=T)
#     # train_set_83$bagging_fitted <- reg_bagging$y
#     perdict_bagging <- predict(reg_bagging, newdata=test_set_83,
#         type="class")
#     test_set_83$perdict_bagging <- perdict_bagging
#     residuals_bagging <- abs(test_set_83$Sales - test_set_83$perdict_bagging)
#     # it is better than simple_regression
#     summary(residuals_bagging)
#     # t.test(residuals_bagging, residuals_simple)
#     ## cross-validation, cannot find the example.
#     # cv(Sales, Sales~DayOfWeek+Promo, data=train_set_83)

#     # with(test_set_83, plot(Date,Sales, col='black'))
#     # with(test_set_83, points(Date,perdict_simple, col='red'))
#     # with(test_set_83, points(Date,perdict_bagging, col='blue'))
#     # with(test_set_83, abline(h=0, v=Date, col='black'))

# }

    # reg_boosting1 <- boosting(Sales~DayOfWeek+Promo,
    #     data=train_set_83)


# perdict_with_boosting <- function(){
#     library(gbm)
#     set.seed(2)
#     # use the columns which only use in the formula.
#     reg_boosting <- gbm(Sales~DayOfWeek+Promo,
#         data=train_set_83,
#         distribution="gaussian",
#         n.trees = 1000,interaction.depth = 3,shrinkage = 0.1)
#     train_set_83_s = train_set_83[,names(train_set_83) %in%
#         c('Sales','DayOfWeek','Promo')]
#     reg_boosting <- gbm(Sales~DayOfWeek+Promo,
#         data=train_set_83_s,
#         distribution="gaussian",
#         n.trees = 1000,interaction.depth = 7,shrinkage = 0.01,
#         cv.folds = 3)
#     summary(reg_boosting)
#     # reg_boosting_iter = gbm.perf(reg_boosting,method="cv")
#     reg_boosting_iter = gbm.perf(reg_boosting)
#     perdict_boosting <- predict(reg_boosting, newdata=test_set_83,
#         n.trees = 100)
# #     test_set_83$perdict_boosting <- perdict_boosting
#     residuals_boosting <- abs(test_set_83$Sales - perdict_boosting)
#     summary(residuals_boosting)

#     with(test_set_83, plot(Date,Sales, col='black'))
#     with(test_set_83, points(Date,perdict_simple, col='red'))
#     with(test_set_83, points(Date,perdict_boosting, col='blue'))
#     with(test_set_83, points(Date,perdict_bagging, col='green'))
#     with(test_set_83, abline(h=0, v=Date, col='black'))

#     # not useful for regression
#     library(pROC)
#     reg_boosting_roc = roc(test_set_83$Sales, perdict_boosting)
#     plot(reg_boosting_roc)
#     coords(reg_boosting_roc, "best")
#     # churn.predict.class = ifelse(churn.predict > coords(churn.roc,
#     #     "best")["threshold"], "yes", "no")
# }

# perdict_with_randomforest<- function(){
#     library(randomForest)
#     set.seed(2)
#     # use the columns which only use in the formula.
#     reg_randomforest <- randomForest(Sales~DayOfWeek+Promo,
#         data=train_set_83,
#         importance = T)

#     perdict_randomforest <- predict(reg_randomforest, newdata=test_set_83)
#     test_set_83$perdict_randomforest <- perdict_randomforest
#     residuals_randomforest <- abs(test_set_83$Sales - test_set_83$perdict_randomforest)
#     summary(residuals_randomforest)

#     with(test_set_83, plot(Date,Sales, col='black'))
#     with(test_set_83, points(Date,perdict_simple, col='red'))
#     with(test_set_83, points(Date,perdict_randomforest, col='blue'))
#     # with(test_set_83, points(Date,perdict_bagging, col='green'))
#     with(test_set_83, abline(h=0, v=Date, col='black'))

#     importance(reg_randomforest)

#     # margins_randomforest=margin(reg_randomforest,train_set_83)
#     # plot(margins_randomforest)
#     # errorevol(reg_randomforest,train_set_83)
# }

# perdict_with_svm <- function(formula, train_dataset, test_dataset){
#     library(e1071)
#     reg_svm <- svm(Sales~DayOfWeek+Promo, data=train_set_83, type='eps-regression')
#     perdict_svm <- predict(reg_svm, newdata=test_set_83)
#     test_set_83$perdict_svm <- perdict_svm
#     residuals_svm <- abs(test_set_83$Sales - test_set_83$perdict_svm)
#     summary(residuals_svm)

#     # with(test_set_83, plot(Date,Sales, col='black'))
#     # with(test_set_83, points(Date,perdict_simple, col='red'))
#     # with(test_set_83, points(Date,perdict_svm, col='blue'))
#     # # with(test_set_83, points(Date,perdict_bagging, col='green'))
#     # with(test_set_83, abline(h=0, v=Date, col='black'))

#     # tune
#     # reg_svm_tune <- tune.svm(Sales~DayOfWeek+Promo, data=train_set_83,
#     #         gamma = 10^(-6:-1),cost=10^(0:2),tunecontrol=tune.control(cross=10))
#     # summary(reg_svm_tune)
#     # # - best parameters:
#     # #      gamma cost
#     # #        0.1  100
#     # reg_svm <- svm(Sales~DayOfWeek+Promo, data=train_set_83,
#     #         gamma=0.1, cost=100)
#     # perdict_svm <- predict(reg_svm, newdata=test_set_83)
#     # test_set_83$perdict_svm <- perdict_svm
#     # residuals_svm <- abs(test_set_83$Sales - test_set_83$perdict_svm)
#     # summary(residuals_svm)

# }

# perdict_with_neuralnet <- function(formula, train_dataset, test_dataset){
#     # the perdict result are same
#     library(neuralnet)
#     reg_neuralnet <- neuralnet(Sales~DayOfWeek+Promo, data=train_set_83,
#             hidden=3)
#     perdict_neuralnet <- compute(reg_neuralnet,
#             test_set_83[, names(test_set_83) %in% c("DayOfWeek","Promo")])$net.result
#     test_set_83$perdict_neuralnet <- perdict_neuralnet
#     residuals_neuralnet <- abs(test_set_83$Sales - test_set_83$perdict_neuralnet)
#     summary(residuals_neuralnet)

#     with(test_set_83, plot(Date,Sales, col='black'))
#     with(test_set_83, points(Date,perdict_simple, col='red'))
#     with(test_set_83, points(Date,perdict_neuralnet, col='blue'))
#     # with(test_set_83, points(Date,perdict_bagging, col='green'))
#     with(test_set_83, abline(h=0, v=Date, col='black'))
# }

# perdict_with_simple_regression <- function(formula, train_dataset, test_dataset){
#     reg_simple = lm(formula, train_dataset)
#     perdict_simple = predict(reg_simple, test_dataset, interval="predict")
#     column_len = length(perdict_simple)/3
#     # test_dataset$perdict_simple <- perdict_simple[1:column_len]
#     residuals_simple <- abs(test_dataset$Sales - test_dataset$perdict_simple)
#     summary(residuals_simple)

#     #
#     # library(caret)
#     # control = trainControl(method="repeatedcv", number=10, repeats=3)
#     # model = train(Sales~DayOfWeek+Promo, data=train_dataset, method="lm",
#     #     trControl=control)
#     # perdict_simple = predict(model$finalModel, test_dataset, interval="predict")
# }



main_test <- function(){
    train_raw <- read.csv('data/train.csv', header=TRUE)
    # head(train_raw)
    # str(train_raw)

    # store_count <- 1115
    # set.seed(2)
    # sample_store_ids <- sort(sample(1:store_count, 20))
    source("evaluate_helper.R")
    # train_20_raw <- sample_by_column(train_raw, 'Store', 20, 2)
    train_20_raw <- read.csv('data/train_20.csv', header=TRUE)

    # train_20 <- remove_columns(train_20_raw,c("Date","Customers"))
    train_20 <- remove_columns(train_20_raw,c("Customers","X"))

    train_20 <- train_20[train_20$Open==1,]

    # train_20$St <- as.character(train_20$StateHoliday)
    # train_20$St[train_20$St %in% c("a","b","c")] <- "1"
    # train_20$StateHoliday <- as.integer(train_20$St)
    # train_20 <- remove_columns(train_20,c("St"))
    # str(train_20)

    train_20$Date <- as.Date(train_20$Date)
    train_20 <- add_dayofyear(train_20, "Date")
    train_20$DateInt <- as.integer(train_20$Date)
    train_2 <- train_20[train_20$Store %in% c(83,144),]

    file_dir <- "."
    file_path <- file.path(file_dir, "result_2.csv")
    clear_file(file_path)
    append_file<-get_append_file_function(file_path)
    append_file("store_id","method","mean")

    all_set = split_by_column(train_2, 'Date', 50)
    # all_set = split_by_column(train_20, 'Date', 50)
    train_set = all_set$train
    test_set = all_set$test
    method_names <- c("svm","svm_tune")
    # method_names <- c("simple_regression","rubost_regression","log_regression")
    method_names <- c("simple_regression","rubost_regression",
            "log_regression","glm_regression","gam_regression",
            "bagging","boosting","boosting_cv","randomforest","svm")
    # perdict_matrix <-evaluate_all_by_store(train_set,test_set,method_names)
    perdict_matrix <-evaluate_to_file(train_set,test_set,method_names,append_file)
    best_choices <- organize_best_chcoices_by_store(perdict_matrix,test_set,method_names)
    range_differences = get_range_difference(train_set)
    best_choices$range <- range_differences
    best_choices$mean2range <- round(best_choices[2] / range_differences, 3)
    # colnames(best_choices)[13] <- "mean2range"
    best_choices <- subset(best_choices,select=c(1:2, 13:14, 3:12))

    all_store_residuals <- cal_all_store_residuals(perdict_matrix, best_choices, test_set)

# 839
    # train_set_83=train_set[(train_set$Store==83 && train_set$Open==1),]
    train_set_83=train_set[train_set$Store==83,]
    test_set_83=test_set[test_set$Store==83,]
    train_set_839=train_set[train_set$Store==839,]
    test_set_839=test_set[test_set$Store==839,]
    train_set_839_1 <- train_set_839[train_set_839$Sales<10050,]

    boxplot.stats(test_set_839$Sales)

    train_set_839_removed <- remove_outlies(train_set_839, "Sales")
    cal_summary_residuals_with_perdict('rubost_regression', formula,
            train_set_839, test_set_839)
    cal_summary_residuals_with_perdict('rubost_regression', formula,
            train_set_839_removed, test_set_839)
    cal_summary_residuals_with_perdict('svm', formula,
            train_set_839, test_set_839)
    cal_summary_residuals_with_perdict('svm', formula,
            train_set_839_removed, test_set_839)

    train_dataset <- train_set_83
    test_dataset <- test_set_83
    formula = Sales~DayOfWeek+Promo
    # formula = Sales~DayOfWeek+Promo+DayOfYear+DateInt
    perdict_with_simple_regression(formula, train_dataset, test_dataset)
    # do.call("perdict_with_simple_regression",list(formula, train_dataset, test_dataset))

    train_set_25=train_set[train_set$Store==25,]
    test_set_25=test_set[test_set$Store==25,]

    perdict_matrix <-evaluate_all_by_store(train_set_25,test_set_25,method_names)
    best_choices <- organize_best_chcoices_by_store(perdict_matrix,test_set_25,method_names)


#     lmfit = lm(Sales~DayOfWeek+Open+Promo+StateHoliday+SchoolHoliday, train_set_83)
#     lmfit = lm(Sales~DayOfWeek+Promo, train_set_83)
#     lmfit3 = lm(Sales~DayOfWeek+Promo+DayOfYear+DateInt, train_set_83)
#     lm_predict = predict(lmfit, test_set_83, interval="confidence", level=0.95)
#     lm_predict = predict(lmfit, test_set_83, interval="predict")
#     # lmfit = lm(Quartet$y2~poly(Quartet$x,2))
#     lm_predict
#     test_set_83$Sales
#     test_raw <- read.csv('data/test.csv', header=TRUE)


#     # predict values
#     fitted(lmfit)
#     residuals(lmfit)
#     train_set_83$fitted <- fitted(lmfit)
#     train_set_83$residuals <- residuals(lmfit)

#     # rubost, will delete outlier
#     # library(MASS)
#     rlmfit = rlm(Sales~DayOfWeek+Promo, train_set_83)
#     train_set_83$rfitted <- fitted(rlmfit)
#     # pass the bptest, p-value = 8.978e-05
#     bptest(rlmfit)

#     # P324
#     par(mfrow=c(2,2))
#     plot(lmfit)
#     # see which point are way from perdict value, maybe they can be deleted
#     plot(cooks.distance(lmfit))

#     # log
#     llmfit = lm(log(Sales)~DayOfWeek+Promo, train_set_83)
#     train_set_83$lfitted <-exp(fitted(llmfit))
#     vif(llmfit)
#     library(lmtest)
#     bptest(llmfit)
#     # youcaninstallandloadthermspackage.Then,youcancorrectstandard errors with robcov:
#     install.packages("rms")
#     library(rms)
#     olsfit = ols(log(Sales)~DayOfWeek+Promo, data= train_set_83, x= TRUE,
#     y= TRUE)
#     robcov(olsfit)
#     train_set_83$ofitted <-exp(fitted(olsfit))

#     # Generalized linear model(GLM)
#     lmfit1 = glm(Sales~DayOfWeek+Promo, data = train_set_83,
#         family=gaussian)
#     summary(lmfit1)
#     train_set_83$fitted3 <- fitted(lmfit3)

#     ## Generalized linear model, poisson model
#     pglmfit = glm(Sales~DayOfWeek+Promo, data = train_set_83,
#         family=poisson)
#     summary(pglmfit)
#     train_set_83$pgfitted <- fitted(pglmfit)

#     ## Generalized additive model (GAM)
#     library(mgcv)
#     gamfit = gam(Sales~DayOfWeek+Promo, data = train_set_83)
#     summary(gamfit)
#     train_set_83$gamfitted <- fitted(gamfit)

#     # plot(train_set_83$Date,train_set_83$Sales)
#     t50 <- head(train_set_83,50)
#     with(t50, plot(Date,Sales, col='green'))
#     with(t50, points(Date,fitted, col='red'))
#     with(t50, points(Date,bagging_fitted, col='blue'))
#     with(t50, abline(h=0, v=Date, col='black'))

# library(ipred)
# set.seed(2)
# sales.bagging = bagging(Sales~DayOfWeek+Promo, data=train_set_83, coob=T)
# train_set_83$bagging_fitted <- sales.bagging$y
# perdict_bagging = predict(sales.bagging, newdata=test_set_83,
#     type="class")
# test_set_83$perdict_bagging <- perdict_bagging
#     with(test_set_83, plot(Date,Sales, col='black'))
#     # with(test_set_83, points(Date,fitted, col='red'))
#     with(test_set_83, points(Date,perdict_bagging, col='blue'))
#     with(test_set_83, abline(h=0, v=Date, col='black'))


# > par(mfrow=c(2,2))
#     > plot(SLID$wages ~ SLID$language)
#     > plot(SLID$wages ~ SLID$age)
#     > plot(SLID$wages ~ SLID$education)
#     > plot(SLID$wages ~ SLID$sex)

#     # Next,youcandiagnosethemulti-colinearityoftheregressionmodelusingthevif function:
#     library(car)
#     vif(lmfit)
#     # If multi-colinearity exists, it will large than 2
#     sqrt(vif(lmfit)) > 2

#     library(lmtest)
#     # bptest(Breusch-Pagan test) for heteroscedasticity
#     # shows 2.206e-06 (<0.5), which rejects the null hypothesis of homoscedasticity
#     # in my case, it is heteroscedasticity
#     bptest(lmfit)

#     > install.packages("rms")
#     > library(rms)
#     > olsfit = ols(log(wages) ~ age + sex + education, data= SLID, x= TRUE,
#     y= TRUE)
#     > robcov(olsfit)
}

test_split_promo <- function(){
    'dont have any significant difference'
    train_set_83 <- train_set[train_set$Store==83,]
    test_set_83 <- test_set[test_set$Store==83,]

    formula <- Sales ~ DayOfWeek + Promo
    residuals_with_promo <- cal_summary_residuals_with_perdict("boosting", formula, train_set_83, test_set_83)

    train_set_83_promo0 <- train_set_83[train_set_83$Promo==0,]
    train_set_83_promo1 <- train_set_83[train_set_83$Promo==1,]
    test_set_83_promo0 <- test_set_83[test_set_83$Promo==0,]
    test_set_83_promo1 <- test_set_83[test_set_83$Promo==1,]
    formula_without_promo <- Sales ~ DayOfWeek
    residuals_promo0 <- cal_summary_residuals_with_perdict("boosting",
            formula_without_promo, train_set_83_promo0, test_set_83_promo0)
    residuals_promo1 <- cal_summary_residuals_with_perdict("boosting",
            formula_without_promo, train_set_83_promo1, test_set_83_promo1)
    perdicts_promo0 <- perdict_with_boosting(
            formula_without_promo, train_set_83_promo0, test_set_83_promo0)
    perdicts_promo1 <- perdict_with_boosting(
            formula_without_promo, train_set_83_promo1, test_set_83_promo1)
    perdicts_83 <- append(perdicts_promo0, perdicts_promo1)
    actual_83 <- append(test_set_83_promo0$Sales, test_set_83_promo1$Sales)
    cal_summary_residuals(actual_83, perdicts_83)
}

if (is.null(sys.frames())){
    main()
    print("done")
}



