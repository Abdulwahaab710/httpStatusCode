import sys
import textwrap
import json


def getStatusCode(httpStatusCode):
    try:
        statusCode = ''
        with open('httpStatusCode.json') as data_file:
            statusCode = json.load(data_file)
        return statusCode[httpStatusCode]
    except KeyError:
        print 'Invalid http status code :('


def getStatusCodeDescription(httpStatusCode):
    try:
        with open('httpStatusCodeDescription.json') as data_file:
            statusCodeDescription = json.load(data_file)
        return statusCodeDescription[httpStatusCode]
    except KeyError:
        return None


def main():
    width = 60
    httpStatusCode = ''
    try:
        httpStatusCode = sys.argv[1]
    except NameError:
        httpStatusCode = raw_input('Please type a http status code')
    finally:
        print '\033[7;4m{0} \033[7;4m{1}'.format(
            httpStatusCode,
            getStatusCode(httpStatusCode)
        )
        dedented_text = textwrap.dedent(
            getStatusCodeDescription(httpStatusCode)
        ).strip()
        print '\033[0m{0}'.format(
            textwrap.fill(
                dedented_text,
                width=width
            )
        )


if __name__ == '__main__':
    main()
