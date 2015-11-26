## result_1
Sales ~ DayOfWeek + Promo
no remove outlines
0.13536

## result_2
Sales ~ DayOfWeek + Promo + SchoolHoliday
no remove outlines
0.13606

## result_3
min(Sales ~ DayOfWeek + Promo, Sales ~ DayOfWeek + Promo + SchoolHoliday)
no remove outlines
1692 0.13452


## result_4
using outlines with result_3 best_choices
0.13755

## result_5
using score now
only for best choices
no remove outlines
Sales ~ DayOfWeek + Promo

## result_6
using score now
only for best choices
no remove outlines
Sales ~ DayOfWeek + Promo + SchoolHoliday
find using Sales ~ DayOfWeek + SchoolHoliday and remove outlines works for some

## result_7
using score now
remove outlines
Sales ~ DayOfWeek + Promo

## result_8
using score now
remove outlines
Sales ~ DayOfWeek + Promo + SchoolHoliday

## result_9
using score now
remove outlines
Sales ~ DayOfWeek

## result_10
using score now
remove outlines
Sales ~ DayOfWeek + SchoolHoliday

## result_11
merge 7,8,9,10
0.13686

mimic score: 0.13743

## 12
using score now
Sales ~ DayOfWeek

## 13
using score now
Sales ~ DayOfWeek + SchoolHoliday

## 14
merge 5,6,12,13
0.13520

mimic score: 0.14467

# use right boosting_cv
the above boosting_cv is using fixed formula
Sales ~ DayOfWeek + Promo

## 164
merger 101 - 163
0.12888
nohup Rscript choose_methods.R -b result_all/best_choices101.csv -f "Sales~DayOfWeek" >logs/log101.log 2>&1 &

using last 50 as testset, the score will be 0.11763
mimic score: 0.11763

# don't remove sales == 0 records, changed the log_regression



formula           method1   mean1
1056                                Sales ~ DayOfWeek + Promo + DateInt               svm 0.15005
1107                           Sales ~ DayOfWeek + Month + Week + Promo       boosting_cv 0.15036
1028 Sales ~ DayOfWeek + Month + Week + Promo + SchoolHoliday + DateInt      randomforest 0.15148
680                            Sales ~ DayOfWeek + Month + Week + Promo      randomforest 0.15195
848  Sales ~ DayOfWeek + Month + Week + Promo + SchoolHoliday + DateInt      randomforest 0.15334
1014         Sales ~ DayOfWeek + Week + Promo + SchoolHoliday + DateInt          boosting 0.15344
417                                 Sales ~ DayOfWeek + Promo + DateInt simple_regression 0.15369
518                            Sales ~ DayOfWeek + Month + Week + Promo       boosting_cv 0.15502
678                         Sales ~ DayOfWeek + Month + Promo + DateInt               svm 0.15554
881                   Sales ~ DayOfWeek + Month + Promo + SchoolHoliday               svm 0.15617
58   Sales ~ DayOfWeek + Month + Week + Promo + SchoolHoliday + DateInt      randomforest 0.15678
1019           Sales ~ DayOfWeek + Month + Week + Promo + SchoolHoliday       boosting_cv 0.15692
701         Sales ~ DayOfWeek + Month + Promo + SchoolHoliday + DateInt          boosting 0.15760
575            Sales ~ DayOfWeek + Month + Week + Promo + SchoolHoliday          boosting 0.15768
695                            Sales ~ DayOfWeek + Month + Week + Promo       boosting_cv 0.15862
589                  Sales ~ DayOfWeek + Month + Week + Promo + DateInt          boosting 0.15866
675                  Sales ~ DayOfWeek + Month + Week + Promo + DateInt       boosting_cv 0.15910
1076                 Sales ~ DayOfWeek + Month + Week + Promo + DateInt      randomforest 0.16022
127                          Sales ~ DayOfWeek + Week + Promo + DateInt               svm 0.16377
713                                 Sales ~ DayOfWeek + Promo + DateInt               svm 0.16589
973                                 Sales ~ DayOfWeek + Promo + DateInt               svm 0.16676
1073 Sales ~ DayOfWeek + Month + Week + Promo + SchoolHoliday + DateInt      randomforest 0.16781
551                    Sales ~ DayOfWeek + Week + Promo + SchoolHoliday       boosting_cv 0.16792
102            Sales ~ DayOfWeek + Month + Week + Promo + SchoolHoliday          boosting 0.16977
563                  Sales ~ DayOfWeek + Month + Week + Promo + DateInt               svm 0.17062
628                                    Sales ~ DayOfWeek + Week + Promo       boosting_cv 0.17238
737                           Sales ~ DayOfWeek + Promo + SchoolHoliday           bagging 0.17259
657                   Sales ~ DayOfWeek + Month + Promo + SchoolHoliday               svm 0.17558
612                                   Sales ~ DayOfWeek + Month + Promo          boosting 0.17701
692  Sales ~ DayOfWeek + Month + Week + Promo + SchoolHoliday + DateInt               svm 0.18033
427                                           Sales ~ DayOfWeek + Promo           bagging 0.18115
13                   Sales ~ DayOfWeek + Month + Week + Promo + DateInt    log_regression 0.18339
269                                   Sales ~ DayOfWeek + Month + Promo               svm 0.18505
956          Sales ~ DayOfWeek + Week + Promo + SchoolHoliday + DateInt               svm 0.18513
279         Sales ~ DayOfWeek + Month + Promo + SchoolHoliday + DateInt          boosting 0.18528
710          Sales ~ DayOfWeek + Week + Promo + SchoolHoliday + DateInt           bagging 0.19314
782                              Sales ~ Month + Week + Promo + DateInt      randomforest 0.19738
274                                 Sales ~ DayOfWeek + Promo + DateInt          boosting 0.19753
534                            Sales ~ DayOfWeek + Month + Week + Promo       boosting_cv 0.19866
636                          Sales ~ DayOfWeek + Week + Promo + DateInt          boosting 0.20926
722                            Sales ~ DayOfWeek + Week + SchoolHoliday       boosting_cv 0.21208
268                                    Sales ~ DayOfWeek + Week + Promo       boosting_cv 0.21478
183         Sales ~ DayOfWeek + Month + Promo + SchoolHoliday + DateInt      randomforest 0.36690
909                                 Sales ~ DayOfWeek + Month + DateInt               svm 0.60666

1056 1107 1028  680  848 1014  417  518  678  881   58 1019  701  575  695  589  675 1076  127  713  973 1073  551  102  563  628  737  657  612  692  427   13  269  956  279 710  782  274  534  636  722  268  183  909
