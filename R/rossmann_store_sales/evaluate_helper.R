remove_columns <- function(the_data, drop_names){
    return(the_data[,!(names(the_data) %in% drop_names)])
}
sample_by_column <- function(the_data, column_name, count, seed=NULL){
    if(!is.null(seed)){
        set.seed(seed)
    }
    all_values <- unique(the_data[,column_name])
    sample_values <- sort(sample(all_values, count))
    return(the_data[the_data[,column_name] %in% sample_values,])
}

split_by_column <- function(the_data, column_name, test_count){
    all_values <- unique(the_data[,column_name])
    test_values <- head(all_values, test_count)
    in_tests <- (the_data[,column_name] %in% test_values)
    return(list(train = the_data[!in_tests,], 
            test = the_data[in_tests,]))
}

add_dayofyear <- function(the_data, date_column, 
        dayofyear_column_name="DayOfYear"){
    the_data[, dayofyear_column_name] <- as.numeric(
            strftime(the_data[, date_column], format = "%j"))
    return(the_data)
}

perdict_with_simple_regression <- function(formula, train_dataset, test_dataset){
    reg_simple <- lm(formula, train_dataset)
    perdict_simple <- predict(reg_simple, test_dataset)
    rasiduals_simple <- abs(test_dataset$Sales - perdict_simple)
    summary(rasiduals_simple)
}

perdict_with_rubost_regression <- function(formula, train_dataset, test_dataset){
    require(MASS)
    reg_rubost <- rlm(formula, train_dataset)
    perdict_rubost <- predict(reg_rubost, test_dataset)
    rasiduals_rubost <- abs(test_dataset$Sales - perdict_rubost)
    summary(rasiduals_rubost)
}

perdict_with_log_regression <- function(formula, train_dataset, test_dataset){
    require(MASS)
    # change from Sales ~ DayOfWeek + Promo 
    # to log(Sales) ~ DayOfWeek + Promo
    reg_log <- rlm(update(formula, log(.) ~ .), train_dataset)
    perdict_log <- predict(reg_log, test_dataset)
    rasiduals_log <- abs(test_dataset$Sales - exp(perdict_log))
    summary(rasiduals_log)
}

# Generalized linear model
perdict_with_glm_regression <- function(formula, train_dataset, test_dataset){
    reg_glm <- glm(formula, train_dataset,
            family=gaussian)
    perdict_glm <- predict(reg_glm, test_dataset)
    rasiduals_glm <- abs(test_dataset$Sales - perdict_glm)
    summary(rasiduals_glm)
}

# Generalized additive model
perdict_with_gam_regression <- function(formula, train_dataset, test_dataset){
    require(mgcv)
    reg_gam <- gam(formula, data = train_dataset)
    perdict_gam <- predict(reg_gam, test_dataset)
    rasiduals_gam <- abs(test_dataset$Sales - perdict_gam)
    summary(rasiduals_gam)
}

perdict_with_bagging <- function(formula, train_dataset, test_dataset){
    require(ipred)
    set.seed(2)
    reg_bagging <- bagging(formula, data=train_dataset, coob=T)
    perdict_bagging <- predict(reg_bagging, newdata=test_dataset)
    rasiduals_bagging <- abs(test_dataset$Sales - perdict_bagging)
    summary(rasiduals_bagging)
}

perdict_with_boosting <- function(formula, train_dataset, test_dataset){
    require(gbm)
    set.seed(2)
    # use the columns which only use in the formula.
    reg_boosting <- gbm(formula, 
        data=train_dataset,
        distribution="gaussian",
        n.trees = 1000,interaction.depth = 3,shrinkage = 0.1)
    perdict_boosting <- predict(reg_boosting, newdata=test_dataset, n.trees = 100)
    rasiduals_boosting <- abs(test_dataset$Sales - perdict_boosting)
    summary(rasiduals_boosting)

}

perdict_with_boosting_cv <- function(formula, train_dataset, test_dataset){
    require(gbm)
    set.seed(2)
    train_dataset_s = train_dataset[,names(train_dataset) %in% 
        c('Sales','DayOfWeek','Promo')]           
    reg_boosting_cv <- gbm(Sales~DayOfWeek+Promo, 
        data=train_dataset_s,
        distribution="gaussian",
        n.trees = 1000,interaction.depth = 7,shrinkage = 0.01,
        cv.folds = 3) 
    reg_boosting_cv_iter = gbm.perf(reg_boosting_cv, 
        method="cv", plot.it=FALSE)
    perdict_boosting_cv <- predict(reg_boosting_cv, 
            newdata=test_dataset, n.trees = reg_boosting_cv_iter)
    rasiduals_boosting_cv <- abs(test_dataset$Sales - perdict_boosting_cv)
    summary(rasiduals_boosting_cv)

}

perdict_with_randomforest<- function(formula, train_dataset, test_dataset){
    require(randomForest)
    set.seed(2)
    # use the columns which only use in the formula.
    reg_randomforest <- randomForest(formula, 
        data=train_dataset,
        importance = T)

    perdict_randomforest <- predict(reg_randomforest, newdata=test_dataset)
    rasiduals_randomforest <- abs(test_dataset$Sales - perdict_randomforest)
    summary(rasiduals_randomforest)

}

perdict_with_svm <- function(formula, train_dataset, test_dataset){
    require(e1071)
    reg_svm <- svm(formula, data=train_dataset, type='eps-regression')
    perdict_svm <- predict(reg_svm, newdata=test_dataset)
    rasiduals_svm <- abs(test_dataset$Sales - perdict_svm)
    summary(rasiduals_svm)
}

