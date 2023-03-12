from pyspark.sql import functions as F
from pyspark.sql.types import *
from pyspark.sql.functions import *

def Transform(df):
    try:

        df2 = df.withColumn("room_id",F.split("id","_")[7])\
            .withColumn("id",F.split("id","_")[6].cast(IntegerType())) \
            .withColumnRenamed("room_id/id","room_name") \
            .withColumn("noted_date", F.to_timestamp("noted_date", "d-M-y H:m"))
        #New Columns
        df3 = df2.withColumn("year",year(col('noted_date')))\
                .withColumn('dayOfWeek', dayofweek(col('noted_date')))\
                .withColumn('month', month(col('noted_date')))
        return df3
    except BaseException as err:
        return print("Transform error --> {}".format(err))
