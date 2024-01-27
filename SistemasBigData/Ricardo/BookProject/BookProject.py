from pyspark import SparkContext
import re


def process_line(line):
    line = line.lower()
    line = re.sub(r"[^\w\s]", "", line)
    array_line = line.split(" ")

    for word in array_line:
        if word in word_count:
            word_count[word] = word_count[word] + 1
        else:
            word_count[word] = 1


sc = SparkContext("local", "Number RDD App")
word_count = {}

file_handler = open('./RawBooks/Germana.txt', 'r', encoding="utf-8")
lines = file_handler.readlines()

rdd_lines = sc.parallelize(lines)
rdd_lines.foreach(process_line)

print(word_count)

sc.stop()
