find_why_high <- function() {
    source("evaluate_helper.R")
    high_train_raw <- read.csv("data/high_score_train.csv", header=TRUE)
    train_clean <- train_raw[train_raw$Open==1,]

    # 54 rows, cause log_regression wrong
    train_clean <- train_clean[train_clean$Sales!=0,]

    train_clean <- train_clean[train_clean$Store>=from_store_id,]
    train_clean <- train_clean[train_clean$Store<=to_store_id,]

    train_clean$Date <- as.Date(train_clean$Date)
    train_clean$Month <- as.integer(format(train_clean$Date, "%m"))
    train_clean$Week <- as.integer(format(train_clean$Date, "%U"))
    train_clean$DateInt <- as.integer(train_clean$Date)
    train_clean$Year <- as.integer(format(train_clean$Date, "%Y"))



    all_set = split_by_column(train_clean, 'Date', 50)
    train_set = all_set$train
    test_set = all_set$test

    method_names <- c("log_regression")
    method_names <- c("simple_regression","rubost_regression","log_regression",
            "bagging","boosting","boosting_cv","randomforest","svm")

    store_ids <- c(183,909)
    store_ids <- c(183,192,274,530,732,909)
    the_vector<-c('DayOfWeek','Month','Week','Promo','SchoolHoliday','DateInt')
    # the_vector<-c('DayOfWeek','Month','Week','DateInt','Year')
    all_combinations <- get_all_combinations(the_vector)
    formula_strs <- sapply(all_combinations,function(x){
        paste0("Sales~",paste(x,collapse="+"))
        })
    for(i in 1:length(formula_strs)){
        x <- formula_strs[i]
        cat(paste0("nohup Rscript choose_methods.R -b best_choices",100+i,".csv -f \"",
            formula_strs[i],"\" >log",100+i,".log 2>&1 & \n"))
    }
    aa <- sapply(formula_strs, function(x){
        nohup Rscript choose_methods.R -b best_choices7.csv -f "Sales ~ DayOfWeek + Promo" >log7.log 2>&1 &

    formula_strs <- c("Sales ~ DateInt")
    formula_strs <- c("Sales ~ sin(2*pi*DateInt) + cos(2*pi*DateInt)")
    formulas<- c(
        Sales ~ DayOfWeek,
        Sales ~ Month,
        Sales ~ Week,
        Sales ~ Promo,
        Sales ~ SchoolHoliday,
        Sales ~ Week + Month,
        Sales ~ DayOfWeek + Month,
        Sales ~ DayOfWeek + Week,
        Sales ~ DayOfWeek + Month + Week,
        )

"Sales~DayOfWeek+Week+DateInt+Year"

    bs<-list()
    for(i in 5:14){
        file_path <- paste0('result_5_14/best_choices',i,'.csv')
        bs[[i]] <- read.csv(file_path, header=TRUE)
    }
    for(i in 5:14){
        print(sort(table(bs[[i]]$method1),decreasing=T))
    }

    small_best_choices(train_set, test_set, store_ids, method_names, formula_strs)
}

get_all_combinations <- function(the_vector){
    result <- list()
    for(cur_length in 1:length(the_vector)){
        cur_combination <- combn(the_vector, cur_length)
        for(i in 1:dim(cur_combination)[2]){
            result[[length(result)+1]] <- cur_combination[,i]
        }
    }
    result
}

get_store_row <- function(df, store_id){
    df[df$Store==store_id,]
}
get_all_store_row <- function(df_list,store_id){
    sapply(df_list, function(df){
        get_store_row(df, store_id)
        })
}

start <- function(){

}


small_best_choices <- function(train_set, test_set, store_ids, method_names, formula_strs){
    cat("store count: ")
    print(length(store_ids))
    for(store_id in store_ids){
        cat("store: ")
        print(store_id)
        train_set_by_store <- train_set[train_set$Store==store_id,]
        # train_set_by_store <- remove_outlies(train_set_by_store, 'Sales')
        test_set_by_store  <- test_set[test_set$Store==store_id,]
        # test_set_by_store <- remove_outlies(test_set_by_store, 'Sales')
        for(formula_str in formula_strs){
            print(formula_str)
            formula <- as.formula(formula_str)
            limited_method_names <- method_names
            if(length(all.vars(formula))<=2){
                limited_method_names <- method_names[!method_names %in% c("boosting_cv")]
            }else if("Year" %in% all.vars(formula)){
                limited_method_names <- method_names[!method_names %in% c("rubost_regression","log_regression")]
            }
            score_matrix <- sapply(limited_method_names, function(method_name){
                # print(method_name)
                perdicts <- round(do.call(paste0("perdict_with_",
                        method_name),list(formula,
                        train_set_by_store, test_set_by_store)),0)
                # root mean square percentage
                # cur_summary <- cal_summary_residuals(
                #          test_set_by_store$Sales, perdicts)
                cur_score <- cal_score(perdicts,
                         test_set_by_store$Sales)
            })
            # sorted_mean_row <- sort(summary_matrix["Mean",])
            sorted_mean_row <- sort(score_matrix)
            print(sorted_mean_row[1:3])
        }
    }
}


store count: [1] 6
store: [1] 183
[1] "not cv"
    boosting  boosting_cv randomforest
     0.57523      0.57523      0.57541
 boosting_cv     boosting randomforest
     0.48439      0.48484      0.49140
     bagging          svm randomforest
     0.55596      0.56044      0.56923
randomforest      bagging          svm
     0.54737      0.55596      0.58716
[1] "not cv"
    boosting  boosting_cv randomforest
     0.50056      0.50056      0.50681
[1] "not cv"
simple_regression    glm_regression    gam_regression
          0.60033           0.60033           0.60033
store: [1] 192
[1] "not cv"
    boosting  boosting_cv randomforest
     0.61734      0.61734      0.61847
simple_regression    glm_regression    gam_regression
          0.65145           0.65145           0.65145
simple_regression    glm_regression    gam_regression
          0.65389           0.65389           0.65389
simple_regression    glm_regression    gam_regression
          0.65286           0.65286           0.65286
[1] "not cv"
simple_regression    glm_regression    gam_regression
          0.63066           0.63066           0.63066
[1] "not cv"
simple_regression    glm_regression    gam_regression
          0.63398           0.63398           0.63398
store: [1] 274
[1] "not cv"
    bagging    boosting boosting_cv
    0.54325     0.54550     0.54550
     bagging randomforest     boosting
     0.53717      0.55322      0.55863
     randomforest           bagging simple_regression
          0.56872           0.57227           0.57341
simple_regression    glm_regression    gam_regression
          0.55021           0.55021           0.55021
[1] "not cv"
simple_regression    glm_regression    gam_regression
          0.52906           0.52906           0.52906
[1] "not cv"
simple_regression    glm_regression    gam_regression
          0.52601           0.52601           0.52601
store: [1] 530
[1] "not cv"
simple_regression    glm_regression    gam_regression
          0.57845           0.57845           0.57845
   boosting boosting_cv     bagging
    0.15175     0.15933     0.17209
   boosting boosting_cv     bagging
    0.12826     0.13537     0.15003
    boosting  boosting_cv randomforest
     0.13211      0.13747      0.14437
[1] "not cv"
randomforest     boosting  boosting_cv
     0.18635      0.18842      0.18842
[1] "not cv"
randomforest     boosting  boosting_cv
     0.16409      0.16969      0.16969
store: [1] 732
[1] "not cv"
simple_regression    glm_regression    gam_regression
          0.52305           0.52305           0.52305
    boosting  boosting_cv randomforest
     0.16129      0.16916      0.20602
    boosting  boosting_cv randomforest
     0.13319      0.13653      0.19087
    boosting  boosting_cv randomforest
     0.13249      0.14044      0.14631
[1] "not cv"
    boosting  boosting_cv randomforest
     0.28766      0.28766      0.29011
[1] "not cv"
randomforest     boosting  boosting_cv
     0.26675      0.26950      0.26950
store: [1] 909
[1] "not cv"
        svm    boosting boosting_cv
    0.72552     0.74090     0.74090
              svm simple_regression    glm_regression
          0.72555           0.74095           0.74095
simple_regression    glm_regression    gam_regression
          0.74122           0.74122           0.74122
simple_regression    glm_regression    gam_regression
          0.76087           0.76087           0.76087
[1] "not cv"
simple_regression    glm_regression    gam_regression
          0.79989           0.79989           0.79989
[1] "not cv"
simple_regression    glm_regression    gam_regression
          0.79878           0.79878           0.79878

          [1] "Sales~DayOfWeek+Month+Week+Year"
          randomforest     boosting      bagging
               0.35991      0.38376      0.38725
               [1] "Sales~DayOfWeek+Month+DateInt"
                             svm simple_regression    glm_regression
                         0.60666           0.66162           0.66162
               [1] "Sales~DayOfWeek+Month+Year"
                             svm simple_regression    glm_regression
                         0.60014           0.66112           0.66112
