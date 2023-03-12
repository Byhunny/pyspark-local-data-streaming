import argparse

ap = argparse.ArgumentParser()

class Arguments:
    def __init__(self,read_format, write_format, app_name):
        self.read_format = read_format
        self.write_format = write_format
        self.app_name = app_name

    ap.add_argument("-r", "--read_format", required=False, 
                type=str, default='csv',
                help="Read Format. Default: csv")
    ap.add_argument("-w", "--write_format", required=False, 
                type=str, default='console',
                help="Write Format. Default: console")
    ap.add_argument("-n", "--app_name", required=False, 
                type=str, default='example',
                help="App Name. Default: example")
    Args = vars(ap.parse_args())

