__author__ = 'amits'

def main():
    f = open('/eduproject/static/templates/lines.txt')
    for line in f:
        print(line, end = '')


if __name__ == "__main__": main()
