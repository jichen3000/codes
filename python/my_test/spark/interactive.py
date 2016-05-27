# hadoop fs -mkdir -p /spark
# hadoop fs -put words.md /spark/words.md
# hadoop fs -put simple_words.md /spark/simple_words.md

def ch2():
    lines = sc.textFile("words.md")
    pythonLines = lines.filter(lambda line: "Python" in line)
    pythonLines.first()
    pythonLines.count()

def ch3_persist():
    lines = sc.textFile("words.md")
    pythonLines = lines.filter(lambda line: "Python" in line)
    pythonLines.first()
    pythonLines.persist()
    pythonLines.count()  

def ch3_parallelize():
    lines = sc.parallelize(["pandas", "i like pandas"])

def ch3_some_transformations():
    inputRDD = sc.textFile("words.md")
    sparksRDD = inputRDD.filter(lambda x: "Spark" in x) 
    apachesRDD = inputRDD.filter(lambda x: "Apache" in x) 
    # notice, when the file is not exist, 
    # it will check for this transformation
    sumRDD = sparksRDD.union(apachesRDD)
    return sumRDD

def ch3_some_actions():
    sumRDD = ch3_some_transformations()
    sumCount = sumRDD.count()
    sumLines = [line for line in sumRDD.take(sumCount)]
    # notice, Keep in mind that your entire dataset 
    # must fit in memory on a single machine to 
    # use collect() on it, 
    # so collect() shouldn’t be used on large datasets.
    sumLines2 = sumRDD.collect()

def ch3_map():
    nums = sc.parallelize(range(5))
    squared_nums = nums.map(lambda x: x*x)
    squared_nums.collect()

    ranged_nums = nums.flatMap(lambda x: range(x))
    ranged_nums.collect()

def ch3_filter():
    nums = sc.parallelize(range(5))
    even_nums = nums.filter(lambda x: x % 2 == 0)
    even_nums.collect()

def ch4_rdd_pair():
    lines = sc.textFile("simple_words.md")
    pairs = lines.map(lambda x: (x.split(" ")[0], x))
    pairs.collect()
    result = pairs.filter(lambda keyValue: len(keyValue[1]) < 20)
    result.collect()

    # one pair will be ("in", ("in some", 1))
    # mapValues, only impact the value, not the key
    pairs.mapValues(lambda x: (x, 1)).collect()
    pairs.mapValues(lambda x: (x, 1)).reduceByKey(lambda x, y: (x[0] + y[0], x[1] + y[1])).collect()

def ch4_combineByKey():
    nums = sc.parallelize([("panda",0),("pink",1),("pirate",3),("panda",1),("pink",4)])
    sumCount = nums.combineByKey(
            (lambda x: (x,1)),
            (lambda x, y: (x[0] + y, x[1] + 1)),
            (lambda x, y: (x[0] + y[0], x[1] + y[1]))) 
    # {'panda': 0, 'pink': 2, 'pirate': 3}
    sumCount.map(lambda xy: (xy[0], xy[1][0]/xy[1][1])).collectAsMap()
    # [('pink', 2), ('panda', 0), ('pirate', 3)]
    sumCount.map(lambda xy: (xy[0], xy[1][0]/xy[1][1])).collect()

def ch4_join():
    storeAddress = sc.parallelize([
            ("Ritual", "1026 Valencia St"), 
            ("Philz", "748 Van Ness Ave"), 
            ("Philz", "3101 24th St"), 
            ("Starbucks", "Seattle")])
    storeRating = sc.parallelize([
            ("Ritual", 4.9), 
            ("Philz", 4.8)])
    storeAddress.join(storeRating).collect() == [
            ('Philz', ('748 Van Ness Ave', 4.8)),
            ('Philz', ('3101 24th St', 4.8)),
            ('Ritual', ('1026 Valencia St', 4.9))]

    storeAddress.leftOuterJoin(storeRating).collect() == [
             ('Philz', ('748 Van Ness Ave', 4.8)),
             ('Philz', ('3101 24th St', 4.8)),
             ('Ritual', ('1026 Valencia St', 4.9)),
             ('Starbucks', ('Seattle', None))]

    storeAddress.rightOuterJoin(storeRating).collect() == [
            ('Philz', ('748 Van Ness Ave', 4.8)),
            ('Philz', ('3101 24th St', 4.8)),
            ('Ritual', ('1026 Valencia St', 4.9))]

def ch4_parie_actions():
    nums = sc.parallelize([(1,2),(3,4),(3,6)]) 
    nums.countByKey() == {1:1, 3:2}
    # note, it's different in book Map{(1, 2), (3, 4), (3, 6)}
    nums.collectAsMap() == {1: 2, 3: 6}
    nums.lookup(3) == [4,6]

def ch5_sequence_file():
    nums = sc.parallelize([("panda",0),("pink",1),("pirate",3),("panda",1),("pink",4)])
    nums.saveAsSequenceFile("sequence.seq")    

    nums = sc.sequenceFile("sequence.seq", 
            "org.apache.hadoop.io.Text", 
            "org.apache.hadoop.io.IntWritable")
    nums.collect()

def ch6_accumulator():
    # the_file = sc.textFile("words.md")
    the_file = sc.textFile("hdfs://yarn-master:8020/spark/words.md")
    # Create Accumulator[Int] initialized to 0 
    blankLines = sc.accumulator(0)

    def extractCallSigns(line):
        global blankLines # Make the global variable accessible 
        if (line == ""):
            blankLines += 1 
        return line.split(" ")
    
    callSigns = the_file.flatMap(extractCallSigns)
    # compute
    callSigns.collect() 
    # if not callSigns.collect(), it still 0
    print blankLines.value 

def ch6_broadcast():
    # Look up the locations of the call signs on the 
    # RDD contactCounts. We load a list of call sign 
    # prefixes to country code to support this lookup. 
    signPrefixes = sc.broadcast(loadCallSignTable())
    def processSignCount(sign_count, signPrefixes):
        country = lookupCountry(sign_count[0], signPrefixes.value) 
        count = sign_count[1]
        return (country, count)
    countryContactCounts = (contactCounts
                            .map(processSignCount)
                            .reduceByKey((lambda x, y: x+ y)))    
    countryContactCounts.saveAsTextFile(outputDir + "/countries.txt")

def ch6_basis_on_partitions():
    def processCallSigns(signs):
        """Lookup call signs using a connection pool"""
        # Create a connection pool
        http = urllib3.PoolManager()
        # the URL associated with each call sign record
        urls = map(lambda x: "http://73s.com/qsos/%s.json" % x, signs) 
        # create the requests (non-blocking)
        requests = map(lambda x: (x, http.request('GET', x)), urls)
        # fetch the results
        result = map(lambda x: (x[0], json.loads(x[1].data)), requests) 
        # remove any empty results and return
        return filter(lambda x: x[1] is not None, result)

    def fetchCallSigns(input):
        """Fetch call signs"""
        return input.mapPartitions(lambda callSigns : processCallSigns(callSigns))

    contactsContactList = fetchCallSigns(validSigns)    

def ch8_tuning():
    # Construct a conf
    conf = new SparkConf()
    conf.set("spark.app.name", "My Spark App") 
    conf.set("spark.master", "local[4]") 
    # Override the default port
    conf.set("spark.ui.port", "36000") 

    # Create a SparkContext with this configuration
    sc = SparkContext(conf)    

def ch8_toDebugString():
    the_file = sc.textFile("hdfs://yarn-master:8020/spark/words.md")
    the_file = sc.textFile("words.md")
    
    tokenized = the_file.map(lambda l: l.split(" ")).filter(lambda words: len(words)>0)
    # tokenized.collect() 

    counts = tokenized.map(lambda w: (w[0],1)).reduceByKey(lambda x,y: x+y)


    print the_file.toDebugString()
    print tokenized.toDebugString()
    print counts.toDebugString()

    counts.collect()

def ch8_repartition():
    # Wildcard input that may match thousands of files
    input = sc.textFile("s3n://log-files/2014/*.log") 
    input.getNumPartitions()
    # 35154

    # A filter that excludes almost all data
    lines = input.filter(lambda line: line.startswith("2014-10-17")) 
    lines.getNumPartitions()
    # 35154

    # We coalesce the lines RDD before caching
    lines = lines.coalesce(5).cache()

    lines.getNumPartitions()
    # 4

    # Subsequent analysis can operate on the coalesced RDD... 
    lines.count()


def ch9_sql():
    # Import Spark SQL
    from pyspark.sql import HiveContext, Row
    # Or if you can't include the hive requirements 
    from pyspark.sql import SQLContext, Row

    hiveCtx = HiveContext(sc)

    input_file = hiveCtx.read.json("testweet.json")
    # Register the input_file schema RDD 
    input_file.registerTempTable("tweets")
    # Select tweets based on the retweetCount
    topTweets = hiveCtx.sql("""SELECT text, retweetCount FROM
      tweets ORDER BY retweetCount LIMIT 10""")

    topTweetText = topTweets.map(lambda row: row.text)  
    topTweetText.collect()

    topTweets.schema
    hiveCtx.cacheTable("tweets")

def ch9_dataframe_from_rdd():
    happyPeopleRDD = sc.parallelize([Row(name="holden", favouriteBeverage="coffee")])
    happyPeopleDF = hiveCtx.createDataFrame(happyPeopleRDD)
    happyPeopleDF.registerTempTable("happy_people")

def ch9_udf():
    from pyspark.sql.types import IntegerType
    
    hiveCtx.registerFunction("strLenPython", lambda x: len(x), IntegerType()) 
    lengthSchemaRDD = hiveCtx.sql("SELECT strLenPython('text') FROM tweets LIMIT 10")    
