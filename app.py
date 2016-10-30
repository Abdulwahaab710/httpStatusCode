import sys
import json


def getStatusCode(httpStatusCode):
    try:
        data = ''
        with open('./httpStatusCode.json') as data_file:
            data = json.load(data_file)
        return data[httpStatusCode]
    except KeyError:
        print 'Invalid http status code :('


def main():
    httpStatusCode = ''
    try:
        httpStatusCode = sys.argv[1]
    except NameError:
        httpStatusCode = raw_input('Please type a http status code')
    finally:
        print getStatusCode(httpStatusCode)
