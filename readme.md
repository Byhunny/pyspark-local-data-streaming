# Intro

You can instantly capture and transform the data in the specified folder in the local environment.

# Requirements

Install required packages
```
pip install -r requirements.txt
```

Set the variables
```
var = {
        "streamingDir" : "/tmp/iot-temp-input",
        "checkPointDir"  : "/tmp/Streaming/IOT",
        "outputPointDir"  : "/tmp/iot-temp-output"
    }
```
Specify the type of data
```
structure/structure_data.py --> Structure Type
```

Examine the arguments
```
--read_format --> Type of data to be streaming
--write_format --> Type of file to be written at the end of the operation (note: 'Console' for dev)
--app_name --> Give this pipeline a name
```

# Test
You can generate sample data to the folder you specified.

And Start
```
python3 main.py
or
python main.py
```
