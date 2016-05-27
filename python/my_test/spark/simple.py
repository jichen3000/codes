from pyspark import SparkConf, SparkContext
import sys

def main():
    inputFile = sys.argv[1]
    outputFile = sys.argv[2]
    # inputFile = 'words.md'
    # outputFile = 'word_count.md'

    master = "local"
    sc = SparkContext(master, "WordCount")
    # lines = sc.parallelize(["pandas", "i like pandas"])
    # result = lines.flatMap(lambda x: x.split(" ")).countByValue()
    # for key, value in result.iteritems():
    #     print "%s %i" % (key, value)

    lines = sc.textFile(inputFile)
    # words = input.flatMap(line => line.split(" "))
    words = lines.flatMap(lambda x: x.split(" ")).countByValue()
    result = sc.parallelize(words)
    result.saveAsTextFile(outputFile)
    print "ok"


main()    