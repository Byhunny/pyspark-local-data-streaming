from pyspark.sql import SparkSession

def Session(name):
    try:
        spark = SparkSession.builder \
            .appName(name)\
            .getOrCreate()
        return spark
    except BaseException as err :
        return print("Session Error! --> {}".format(err))