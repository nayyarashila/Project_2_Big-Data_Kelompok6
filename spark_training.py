from pyspark.sql import SparkSession
from pyspark.ml.feature import VectorAssembler, StringIndexer
from pyspark.ml.classification import RandomForestClassifier
from pyspark.ml.clustering import KMeans
from pyspark.ml.regression import LinearRegression
from pyspark.ml import Pipeline
import os

# Create Spark session
spark = SparkSession.builder \
    .appName("BigData-Training-Models") \
    .getOrCreate()

print("Mulai baca 3 batch data csv")
# Baca 3 batch file csv
df0 = spark.read.csv("batch_data/batch_0.csv", header=True, inferSchema=True).dropna()
df1 = spark.read.csv("batch_data/batch_1.csv", header=True, inferSchema=True).dropna()
df2 = spark.read.csv("batch_data/batch_2.csv", header=True, inferSchema=True).dropna()

print(f"Jumlah data batch_0: {df0.count()}")
print(f"Jumlah data batch_1: {df1.count()}")
print(f"Jumlah data batch_2: {df2.count()}")

# Gabungkan batch sesuai skema model
# Model 1 = batch 0
model1_data = df0

# Model 2 = batch 0 + batch 1
model2_data = df0.union(df1)

# Model 3 = batch 0 + batch 1 + batch 2 (semua data)
model3_data = df0.union(df1).union(df2)

# Model 1: Random Forest Classifier ===
print("Training Model 1: Random Forest Classifier...")

rfc_data = model1_data.select("Accident_Severity", "Number_of_Vehicles", "Number_of_Casualties")

assembler1 = VectorAssembler(
    inputCols=["Number_of_Vehicles", "Number_of_Casualties"],
    outputCol="features"
)
indexer1 = StringIndexer(inputCol="Accident_Severity", outputCol="label")
rfc = RandomForestClassifier(numTrees=20, maxDepth=5)

pipeline1 = Pipeline(stages=[assembler1, indexer1, rfc])
model1 = pipeline1.fit(rfc_data)

model1.write().overwrite().save("../models/model1_rfc")

# Model 2: KMeans Clustering ===
print("Training Model 2: KMeans Clustering...")

kmeans_data = model2_data.select("Longitude", "Latitude").dropna()
assembler2 = VectorAssembler(inputCols=["Longitude", "Latitude"], outputCol="features")
features2 = assembler2.transform(kmeans_data)

kmeans = KMeans(k=4, seed=1)
model2 = kmeans.fit(features2)

model2.write().overwrite().save("../models/model2_kmeans")

# Model 3: Linear Regression ===
print("Training Model 3: Linear Regression...")

lr_data = model3_data.select("Accident_Severity", "Number_of_Vehicles", "Number_of_Casualties")
assembler3 = VectorAssembler(
    inputCols=["Number_of_Vehicles", "Number_of_Casualties"],
    outputCol="features"
)
features3 = assembler3.transform(lr_data).select("features", "Accident_Severity").withColumnRenamed("Accident_Severity", "label")

lr = LinearRegression()
model3 = lr.fit(features3)

model3.write().overwrite().save("../models/model3_linear")

print("All models trained and saved.")
