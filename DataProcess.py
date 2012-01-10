#!/usr/bin/env python

def fetchData(path):
    handle = open(path, 'r')
    data = []
    for line in handle:
        # '#' is for comment
        if line[0] == '#':
            continue
        data.append(analize(line))
    handle.close()
    return data

def analize(line):
    if line is not None:
        str = line.replace('\n', '').split(':')
        if len(str) == 5:
            str[1] = str[1].split(',')
            str[2] = str[2].split(',')
            str[3] = str[3].split(',')
            print 'Get Data: %s' % str
            return str
        else:
            print 'Data format error %s' % str
            return None
        


def test():
    data = fetchData('data');
    print 'Get: %s' % data

if __name__ == '__main__':
    test()
