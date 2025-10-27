import math

def dgim(stream, window):
    buckets = []
    time = 0

    for bit in stream:
        time += 1
        if bit == '1':
            buckets.insert(0, [1, time])
            i = 0
            while i + 2 < len(buckets) and buckets[i][0] == buckets[i+1][0] == buckets[i+2][0]:
                buckets[i+1][0] += buckets[i][0]
                del buckets[i]
            i += 1

    count = 0
    current_time = time
    for b in buckets:
        if current_time - b[1] < window:
            count += b[0]
        else:
            count += b[0] / 2
            break
    return int(count)

stream = "11010111100101"
window = 8
print("Approx count of 1s in last", window, "bits:", dgim(stream, window))


# Sample data
x <- c(1,2,3,4,5)
y <- c(10,20,15,25,30)

# Line Plot
plot(x, y, type="o", col="blue", main="Line Chart", xlab="X Values", ylab="Y Values")

# Bar Plot
barplot(y, names.arg=x, col="red", main="Bar Chart")

# Histogram
hist(y, col="green", main="Histogram")

#Dot 
dotchart(y, labels=x, color="purple", pch=19, main="Dot Graph", xlab="Y Values", ylab="X Values")

# Check Hadoop version
hadoop version

# List files in HDFS root
hdfs dfs -ls /

# Make directory in HDFS
hdfs dfs -mkdir /user/cloudera/test_dir

# Copy a file from local to HDFS
hdfs dfs -put /etc/passwd /user/cloudera/test_dir/

# List contents
hdfs dfs -ls /user/cloudera/test_dir

# View file contents
hdfs dfs -cat /user/cloudera/test_dir/passwd

# Copy back to local
hdfs dfs -get /user/cloudera/test_dir/passwd /home/cloudera/Desktop/

# Remove file
hdfs dfs -rm /user/cloudera/test_dir/passwd
