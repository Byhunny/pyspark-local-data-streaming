from pyspark.sql import functions as F
from pyspark.sql.types import *
from pyspark.sql.functions import *
from structure.structure_data import Schema
from scripts.transform_data import Transform
from arguments import Arguments
from service.sessions import Session

if __name__ == "__main__":
    args = Arguments.Args
    read_format = args['read_format']
    write_format = args['write_format']
    app_name = args['app_name']

    var = {
        "streamingDir" : "/tmp/iot-temp-input",
        "checkPointDir"  : "/tmp/Streaming/IOT",
        "outputPointDir"  : "/tmp/iot-temp-output"
    }

    spark = Session(app_name)
    spark.sparkContext.setLogLevel('ERROR')

    #Read
    try:
        stream_schema = Schema # structure/structure_data.py
        df = spark.readStream.format(read_format) \
            .schema(stream_schema) \
            .load("".join(["file://",var["streamingDir"]]))

        checkpointDir = "".join(["file://",var["checkPointDir"]])
        df_last = Transform(df)
    except:
        print("->>>> Read Error <<<<-")

    #Write
    try:
        streamingQuery = (df_last.writeStream.format(write_format)
            .outputMode("append")
            .trigger(processingTime="4 second")
            .option("numRows", 4)
            .option("truncate", False)
            .option("checkpointLocation", checkpointDir)
            .start("".join(["file://",var["outputPointDir"]])))
    except:
        print("->>>> Write Error <<<<-")

    streamingQuery.awaitTermination()