import sys


def getStatusCode(httpStatusCode):
    pass


def main():
    httpStatusCode = ''
    try:
        httpStatusCode = sys.argv[1]
    except NameError:
        httpStatusCode = raw_input('Please type a http status code')
    finally:
        print getStatusCode(httpStatusCode)
