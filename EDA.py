from pyspark.sql import SparkSession
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Initialize Spark session
spark = SparkSession.builder.appName("NetflixEDA").getOrCreate()

# Load Netflix dataset
df = spark.read.csv("netflix_titles.csv", header=True, inferSchema=True)

# Perform basic EDA
print("Dataset Schema:")
df.printSchema()

print("Total Records:", df.count())

# Count movies vs TV shows
df.groupBy("type").count().show()

# Count by genre
df.groupBy("listed_in").count().orderBy("count", ascending=False).show()

# Distribution of release years
df.groupBy("release_year").count().orderBy("release_year").show()

# Handle missing values
cleaned_df = df.dropna()

# Plotting
pandas_df = df.toPandas()
sns.countplot(data=pandas_df, x="type")
plt.title("Content Type Distribution")
plt.show()

# Stop Spark
spark.stop()