#Netflix EDA with Apache Spark
This project demonstrates how to perform exploratory data analysis (EDA) on the Netflix TV Shows & Movies dataset using Apache Spark. The dataset is processed in a Docker container that runs Spark and Python scripts for data cleaning, analysis, and visualization.

##Project Setup
The project uses the following tools and technologies:

Apache Spark: Distributed data processing engine.
Docker: Containerization platform to run Spark in an isolated environment.
Python: Programming language for data manipulation and visualization.
PySpark: Python API for Spark.
Pandas: Data manipulation library.
Matplotlib & Seaborn: Data visualization libraries.

##Files
###Dockerfile
The Dockerfile is used to build a Docker image that contains Apache Spark and the necessary Python libraries for data analysis.

FROM bitnami/spark:latest: Uses the Bitnami Spark image.
RUN pip install pandas matplotlib seaborn: Installs the required Python libraries.
WORKDIR /app: Sets the working directory for the application.
COPY: Copies the dataset and Python script into the container.
CMD: Runs the eda_script.py using spark-submit.

###eda_script.py
The eda_script.py script uses PySpark for data analysis and visualization.
