## page
https://www.kaggle.com/c/rossmann-store-sales/data

## facts
### open
in stateholiday, it will not open at all.
just remove all the day, it will not open
StateHoliday has "a", "b", "c", but in the final test, it only has "a". so I can set "a", "b", "c" to 1

### too little of one store sales data

### which model best
lmfit = lm(Sales~DayOfWeek+Promo, train_set_83)
lmfit is normal regression, but it is heteroscedasticity(P349)
bptest(lmfit)
BP = 0.84503, df = 2, p-value = 0.6554

rlmfit = rlm(Sales~DayOfWeek+Promo, train_set_83)
bptest(rlmfit)
BP = 18.636, df = 2, p-value = 8.978e-05

for now rlmfit is best, since it is not heteroscedasticity.
but for the perdict, it is almost like lmfit

glm(Generalized linear model, Gaussian model) is almost like rlm, they have same bptest value


pglmfit(Generalized linear model, poisson model) is the best, since it has same bptest value, and smallest Deviance Residuals. However, the perdict value almost same. actually, why the Deviance Residuals is smallest, because it just use log(Sales). so meanless.
pglmfit = glm(Sales~DayOfWeek+Promo, data = train_set_83,
        family=poisson)



simple regression
   Min. 1st Qu.  Median    Mean 3rd Qu.    Max.
   11.4   154.8   377.8   418.8   620.6  1059.0

rubost regression
    Min.  1st Qu.   Median     Mean  3rd Qu.     Max.
   3.729  157.600  350.300  433.600  705.300 1144.000

log rubost regression
   Min. 1st Qu.  Median    Mean 3rd Qu.    Max.
  2.718 148.200 378.200 415.000 591.600 982.800

Generalized linear model regression
   Min. 1st Qu.  Median    Mean 3rd Qu.    Max.
   11.4   154.8   377.8   418.8   620.6  1059.0

Generalized additive model regression
   Min. 1st Qu.  Median    Mean 3rd Qu.    Max.
   11.4   154.8   377.8   418.8   620.6  1059.0

bagging is the best for now, since summary(rasiduals_bagging)
   Min. 1st Qu.  Median    Mean 3rd Qu.    Max.
  36.45  170.50  388.30  395.10  573.80  934.70

boosting
since summary(rasiduals_boosting)
   Min. 1st Qu.  Median    Mean 3rd Qu.    Max.
  46.64  176.40  338.70  385.00  581.40  923.90
   Min. 1st Qu.  Median    Mean 3rd Qu.    Max.
  26.59  174.10  332.80  382.30  570.70  929.40

random forest
   Min. 1st Qu.  Median    Mean 3rd Qu.    Max.
  28.31  125.80  311.50  395.70  603.00  964.70

svm
   Min. 1st Qu.  Median    Mean 3rd Qu.    Max.
  39.89  154.50  316.10  391.70  605.60  979.90
tuned svm
   Min. 1st Qu.  Median    Mean 3rd Qu.    Max.
  36.11  159.10  317.50  394.60  623.90  967.10

neuralnet
       V1           
 Min.   :  27.5548  
 1st Qu.: 179.5548  
 Median : 506.5548  
 Mean   : 663.9227  
 3rd Qu.:1011.5548  
 Max.   :1861.4452    

 > all_store_residuals
    Min.  1st Qu.   Median     Mean  3rd Qu.     Max.
   0.133  193.900  421.300  554.700  731.600 6497.000

   all together $svm
   $boosting
       Min.  1st Qu.   Median     Mean  3rd Qu.     Max.
      4.064  300.000  620.500  755.700 1043.000 7178.000

839  rubost_regression 1358.0  9889 0.137               svm 1396.0
1107.0 1361.0 1358.0  1642.0 2216.0  


# different formula
Sales ~ DayOfWeek + Promo + SchoolHoliday
method1 mean1  method2 mean2     method3 mean3  Min. 1st Qu. Median  Mean
8 bagging 917.2 boosting 926.6 boosting_cv 927.3    


## high score
183   183 Sales ~ DayOfWeek + Promo       boosting_cv 0.54904
192   192 Sales ~ DayOfWeek + Promo      randomforest 0.53731
274   274 Sales ~ DayOfWeek + Promo      randomforest 0.51710
292   292 Sales ~ DayOfWeek + Promo    log_regression 0.75800 not in
530   530 Sales ~ DayOfWeek + Promo      randomforest 0.56797
732   732 Sales ~ DayOfWeek + Promo      randomforest 0.50381
876   876 Sales ~ DayOfWeek + Promo simple_regression 0.81242 not in
909   909 Sales ~ DayOfWeek + Promo      randomforest 1.00279

183   183 Sales ~ DayOfWeek + Promo + SchoolHoliday  boosting_cv 0.54904
192   192 Sales ~ DayOfWeek + Promo + SchoolHoliday  boosting_cv 0.54487
274   274 Sales ~ DayOfWeek + Promo + SchoolHoliday randomforest 0.50860
292   292 Sales ~ DayOfWeek + Promo + SchoolHoliday     boosting 0.75788
530   530 Sales ~ DayOfWeek + Promo + SchoolHoliday randomforest 0.52419
732   732 Sales ~ DayOfWeek + Promo + SchoolHoliday randomforest 0.47311
876   876 Sales ~ DayOfWeek + Promo + SchoolHoliday randomforest 0.80820
909   909 Sales ~ DayOfWeek + Promo + SchoolHoliday randomforest 0.96229

c(183,192,274,530,732,909)
