Certainly! Here is a cheat sheet for common PySpark RDD tasks, particularly for processing large text files or arrays of
text. These examples assume you are working with PySpark's RDD API.

### Initializing PySpark

```python
from pyspark import SparkContext

sc = SparkContext(appName="PySparkRDDApp")
```

### Creating RDDs

- **From a Collection**

```python
data = [1, 2, 3, 4, 5]
rdd = sc.parallelize(data)
```

- **From a Text File**

```python
rdd = sc.textFile("path/to/textfile.txt")
```

### Basic RDD Transformations

- **map**

```python
# Applies a function to each element
rdd_result = rdd.map(lambda x: x * 2)
```

- **filter**

```python
# Returns a new RDD containing only the elements that satisfy a predicate
rdd_filtered = rdd.filter(lambda x: x % 2 == 0)
```

- **flatMap**

```python
# Similar to map, but each input item can be mapped to 0 or more output items
rdd_flatmapped = rdd.flatMap(lambda x: (x, x * 100, 42))
```

- **distinct**

```python
# Returns a new RDD containing distinct items
rdd_distinct = rdd.distinct()
```

- **union**

```python
# Returns a new RDD containing all items from both RDDs
other_rdd = sc.parallelize([6, 7, 8, 9, 10])
rdd_union = rdd.union(other_rdd)
```

### Advanced RDD Transformations

- **reduceByKey**

```python
# Merge the values for each key using an associative reduce function
pair_rdd = rdd.map(lambda x: (x, 1))
rdd_count_by_key = pair_rdd.reduceByKey(lambda a, b: a + b)
```

- **groupByKey**

```python
# Group the values for each key in the RDD into a single sequence
rdd_grouped = pair_rdd.groupByKey()
```

- **sortByKey**

```python
# Returns an RDD sorted by the key
rdd_sorted = pair_rdd.sortByKey()
```

- **join**

```python
# Joins two RDDs based on their keys
other_pair_rdd = sc.parallelize([(3, 'three'), (4, 'four')])
rdd_joined = pair_rdd.join(other_pair_rdd)
```

### RDD Actions

- **collect**

```python
# Return all the elements as an array
all_data = rdd.collect()
```

- **count**

```python
# Return the number of elements in the RDD
count_data = rdd.count()
```

- **take**

```python
# Return an array with the first n elements of the RDD
first_n_data = rdd.take(3)
```

- **reduce**

```python
# Reduces the elements of this RDD using the specified commutative and associative binary operator
sum_data = rdd.reduce(lambda a, b: a + b)
```

- **saveAsTextFile**

```python
# Write the elements of the RDD as a text file
rdd.saveAsTextFile("path/to/output")
```

### Working with Text Data

- **flatMap + map**

```python
# Split lines into words and then create a tuple for each word
words = rdd.flatMap(lambda line: line.split(" ")).map(lambda word: (word, 1))
```

- **reduceByKey**

```python
# Count occurrences of each word
word_counts = words.reduceByKey(lambda a, b: a + b)
```

Remember to always use actions (`collect`, `count`, `take`, `first`, `saveAsTextFile`, etc.) to trigger the computations
of RDD transformations. Transformations are lazy and won't execute until an action is called. Also, be aware of the size
of the data when using actions like `collect`, as they will load all data into the driver's memory which could cause an
out-of-memory error for very large datasets.
