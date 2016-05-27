## link
http://blog.csdn.net/zhaohansk/article/details/49509801

## test without hadoop
cat words.txt | python count_words_mapper.py | sort | python count_words_reducer.py

## how to run
ssh yarn-master
su - hduser
start-dfs.sh
start-yarn.sh

hadoop fs -mkdir /count_words/
hadoop fs -put words.txt /count_words/words.txt 
hadoop fs -put count_words_mapper.py /count_words/count_words_mapper.py 
hadoop fs -put count_words_reducer.py /count_words/count_words_reducer.py 
hadoop fs -ls /count_words/

hadoop fs -rm /count_words/count_words_mapper.py 
hadoop fs -rm /count_words/count_words_reducer.py 

hadoop fs -rm -R /count_words/output

# notice, -mapper just give the name, -file give the true path
hadoop jar $YARN_HOME/share/hadoop/tools/lib/hadoop-streaming-2.7.2.jar -mapper count_words_mapper.py -file ./count_words_mapper.py -reducer count_words_reducer.py  -file ./count_words_reducer.py -input /count_words/words.txt -output /count_words/output

http://stackoverflow.com/questions/4339788/hadoop-streaming-unable-to-find-file-error