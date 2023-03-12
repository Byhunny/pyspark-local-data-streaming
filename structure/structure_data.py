from pyspark.sql.types import StructType, StructField, StringType, IntegerType, TimestampType

Schema = StructType(
    [
        StructField("id",StringType(),True),
        StructField("room_id/id",StringType(),True),
        StructField("noted_date",StringType(),True),
        StructField("temp",IntegerType(),True),
        StructField("out/in",StringType(),True),
        StructField("event_time",TimestampType(),True)
    ]
)