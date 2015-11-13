clear_file <- function(file_path){
    # clear file
    cat(c(""), file=file_path)
}

get_append_file_function <- function(file_path){
    function(...) {
        write.table(t(matrix(c(...))), file=file_path,
                row.names=FALSE, append=TRUE, col.names=FALSE, sep=",")
    }
}

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
    perdict_simple
}

perdict_with_rubost_regression <- function(formula, train_dataset, test_dataset){
    require(MASS)
    reg_rubost <- rlm(formula, train_dataset)
    perdict_rubost <- predict(reg_rubost, test_dataset)
    perdict_rubost
}

perdict_with_log_regression <- function(formula, train_dataset, test_dataset){
    require(MASS)
    # change from Sales ~ DayOfWeek + Promo
    # to log(Sales) ~ DayOfWeek + Promo
    reg_log <- rlm(update(formula, log(.) ~ .), train_dataset)
    perdict_log <- predict(reg_log, test_dataset)
    perdict_log
}

# Generalized linear model
perdict_with_glm_regression <- function(formula, train_dataset, test_dataset){
    reg_glm <- glm(formula, train_dataset,
            family=gaussian)
    perdict_glm <- predict(reg_glm, test_dataset)
    perdict_glm
}

# Generalized additive model
perdict_with_gam_regression <- function(formula, train_dataset, test_dataset){
    require(mgcv)
    reg_gam <- gam(formula, data = train_dataset)
    perdict_gam <- predict(reg_gam, test_dataset)
    perdict_gam
}

perdict_with_bagging <- function(formula, train_dataset, test_dataset){
    require(ipred)
    set.seed(2)
    reg_bagging <- bagging(formula, data=train_dataset, coob=T)
    perdict_bagging <- predict(reg_bagging, newdata=test_dataset)
    perdict_bagging
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
    perdict_boosting

}

perdict_with_boosting_cv <- function(formula, train_dataset, test_dataset){
    require(gbm)
    set.seed(2)
    train_dataset_s <- train_dataset[,names(train_dataset) %in%
        c('Sales','DayOfWeek','Promo')]
    reg_boosting_cv <- gbm(Sales~DayOfWeek+Promo,
        data=train_dataset_s,
        distribution="gaussian",
        n.trees = 1000,interaction.depth = 7,shrinkage = 0.01,
        cv.folds = 3)
    reg_boosting_cv_iter <- gbm.perf(reg_boosting_cv,
        method="cv", plot.it=FALSE)
    perdict_boosting_cv <- predict(reg_boosting_cv,
            newdata=test_dataset, n.trees = reg_boosting_cv_iter)
    perdict_boosting_cv

}

perdict_with_randomforest<- function(formula, train_dataset, test_dataset){
    require(randomForest)
    set.seed(2)
    # use the columns which only use in the formula.
    reg_randomforest <- randomForest(formula,
        data=train_dataset,
        importance = T)

    perdict_randomforest <- predict(reg_randomforest, newdata=test_dataset)
    perdict_randomforest
}

perdict_with_svm <- function(formula, train_dataset, test_dataset){
    require(e1071)
    reg_svm <- svm(formula, data=train_dataset, type='eps-regression')
    perdict_svm <- predict(reg_svm, newdata=test_dataset)
    perdict_svm
}

perdict_with_svm_tune <- function(formula, train_dataset, test_dataset){
    require(e1071)
    tuned <- tune.svm(formula, data=train_dataset,
            gamma = 10^(-6:-1),cost=10^(0:2))
    reg_svm_tune <- svm(formula, data=train_dataset,
            gamma = tuned$best.parameters$gamma, cost=tuned$best.parameters$cost)
    # reg_svm_tune <- tune.svm(formula, data=train_dataset,
    #         gamma = 10^(-6:-1),cost=10^(0:2),tunecontrol=tune.control(cross=10))
    perdict_svm <- predict(reg_svm_tune, newdata=test_dataset)
    perdict_svm
}

cal_summary_residuals <- function(actuals, perdicts){
    residuals <- abs(actuals - perdicts)
    summary(residuals)
}

cal_summary_residuals_with_perdict <- function(method_name, formula, train_dataset, test_dataset){
    perdicts <- do.call(paste0("perdict_with_",
            method_name),list(formula,
            train_dataset, test_dataset))
    cal_summary_residuals(test_dataset$Sales, perdicts)
}

evaluate_to_file <- function(train_set, test_set, method_names, append_file){
    formula <- Sales~DayOfWeek+Promo
    perdict_matrix <- sapply(unique(train_set$Store), function(store_id){
        train_set_by_store <- train_set[train_set$Store==store_id,]
        # train_set_by_store <- remove_outlies(train_set_by_store, 'Sales')
        test_set_by_store  <- test_set[test_set$Store==store_id,]
        cat("store: ")
        print(store_id)
        result <- sapply(method_names, function(method_name){
            print(method_name)
            perdicts <- do.call(paste0("perdict_with_",
                    method_name),list(formula,
                    train_set_by_store, test_set_by_store))
            cur_summary <- cal_summary_residuals(
                     test_set_by_store$Sales, perdicts)
            append_file(as.numeric(store_id),method_name,as.numeric(cur_summary[4]))
            list(perdicts)
        })
    })
    colnames(perdict_matrix)<-unique(train_set$Store)
    # result_dataframe <- as.data.frame(perdict_matrix)
    perdict_matrix
}

evaluate_all_by_store <- function(train_set, test_set, method_names){
    formula <- Sales~DayOfWeek+Promo
    perdict_matrix <- sapply(unique(train_set$Store), function(store_id){
        train_set_by_store <- train_set[train_set$Store==store_id,]
        # train_set_by_store <- remove_outlies(train_set_by_store, 'Sales')
        test_set_by_store  <- test_set[test_set$Store==store_id,]
        cat("store: ")
        print(store_id)
        result <- sapply(method_names, function(method_name){
            print(method_name)
            perdicts <- do.call(paste0("perdict_with_",
                    method_name),list(formula,
                    train_set_by_store, test_set_by_store))
            list(perdicts)
            # list(cal_summary_residuals(
            #         test_set_by_store$Sales, perdicts))
        })
    })
    colnames(perdict_matrix)<-unique(train_set$Store)
    # result_dataframe <- as.data.frame(perdict_matrix)
    perdict_matrix
}

evaluate_all_ignoring_store <- function(train_set, test_set, method_names){
    formula <- Sales~Store+DayOfWeek+Promo
    perdict_list <- sapply(method_names, function(method_name){
        # print(method_name)
        perdicts <- do.call(paste0("perdict_with_",
                method_name),list(formula,
                train_set, test_set))
        list(perdicts)
        # list(cal_summary_residuals(
        #         test_set_by_store$Sales, perdicts))
    })
    perdict_list
}

organize_best_chcoices_ignoring_store <- function(perdict_list, test_set){
    method_names <- names(perdict_list)
    summarie_list <- lapply(perdict_list, function(x){cal_summary_residuals(
                test_set$Sales, x)})
}

organize_best_chcoices_by_store <- function(perdict_matrix, test_set, method_names){
    all_stores <- colnames(perdict_matrix)
    store_count <- length(all_stores)
    choosed_count <- 3
    if(length(method_names) < choosed_count){
        choosed_count <- length(method_names)
    }
    summary_length <- 6
    best_choices <- data.frame(matrix(NA, nrow = store_count, ncol = choosed_count*2+summary_length))
    rownames(best_choices) <- all_stores
    colnames(best_choices) <- append(as.vector(sapply(1:choosed_count,function(x){c(paste0("method",x), paste0("mean",x))})),
        c("Min.","1st Qu.","Median","Mean","3rd Qu.","Max."))
    for(row_index in 1:store_count){
        test_set_by_store  <- test_set[test_set$Store==all_stores[row_index],]
        perdicts <- perdict_matrix[,row_index]
        summaries <- lapply(perdicts, function(x){cal_summary_residuals(
                    test_set_by_store$Sales, x)})
        means <- sapply(summaries, function(x){x[4]})
        sorted_means <- sort(means)
        for(summary_index in 1:choosed_count){
            cur_name <- names(sorted_means)[summary_index]
            best_choices[row_index,(summary_index-1)*2+1] <- unlist(strsplit(cur_name,"[.]"))[1]
            best_choices[row_index,(summary_index-1)*2+2] <- sorted_means[summary_index]
        }
        # min_mean <- min(means)
        # mean_indexs <- which(means==min_mean)
        # names(mean_indexs) <- sapply(names(mean_indexs), function(x){unlist(strsplit(x,"[.]"))[1]})
        # best_choices[row_index,1] <- paste(names(mean_indexs),collapse=",")
        # best_choices[row_index,2] <- min_mean

        best_method_name <- names(sorted_means)[1]
        best_method_name <- unlist(strsplit(best_method_name,"[.]"))[1]
        best_index <- which(method_names==best_method_name)
        best_summary <- summaries[[best_index]]
        for(col_index in 1:summary_length){
            best_choices[row_index,col_index+2*choosed_count] <- best_summary[col_index]
        }
    }
    best_choices
}

cal_all_residuals_by_store <- function(perdict_matrix, best_choices, test_set){
    all_stores <- colnames(perdict_matrix)
    store_count <- length(all_stores)
    method_names <- rownames(perdict_matrix)
    test_set$best_perdict<-0
    for(row_index in 1:store_count){
        test_set_by_store  <- test_set[test_set$Store==all_stores[row_index],]
        best_method <- best_choices[row_index, 1]
        method_index <- which(method_names==best_method)
        test_set[test_set$Store==all_stores[row_index],]$best_perdict <- perdict_matrix[method_index,row_index][[1]]
    }
    cal_summary_residuals(test_set$Sales, test_set$best_perdict)
}

get_range_difference <- function(train_set){
    sapply(unique(train_set$Store), function(store_id){
        train_set_by_store <- train_set[train_set$Store==store_id,]
        cur_range <- range(train_set_by_store$Sales)
        cur_range[2]-cur_range[1]
    })
}

remove_outlies <- function(train_set, column_name){
    train_set[!train_set[,c(column_name)] %in%
            boxplot.stats(train_set[,c(column_name)])$out,]
}


main <- function(){
    source("evaluate_helper.R")
    train_raw <- read.csv('data/train.csv', header=TRUE)
    train_clean <- train_raw[train_raw$Open==1,]

    # 54 rows, cause log_regression wrong
    train_clean <- train_clean[train_clean$Sales!=0,]

    train_clean$Date <- as.Date(train_clean$Date)

    all_set = split_by_column(train_clean, 'Date', 50)
    train_set = all_set$train
    test_set = all_set$test

    formula = Sales~DayOfWeek+Promo

    method_names <- c("simple_regression","rubost_regression",
            "log_regression","glm_regression","gam_regression",
            "bagging","boosting","boosting_cv","randomforest","svm")
    perdict_matrix <-evaluate_all_by_store(train_set,test_set,method_names)
    best_choices <- organize_best_chcoices_by_store(perdict_matrix,test_set,method_names)
    range_differences = get_range_difference(train_set)
    best_choices$range <- range_differences
    best_choices$mean2range <- round(best_choices[2] / range_differences, 3)


}
