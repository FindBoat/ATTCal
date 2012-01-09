#!/usr/bin/env python

from User import User
import DataProcess

__path__ = 'data'

def main():
    data = DataProcess.fetchData(__path__)
    users = []
    for dt in data:
        if len(dt) == 5:
            user = User(dt[0], dt[1], dt[2], dt[3], dt[4])
            users.append(user)
        else:
            print 'Data length error: %s' % str(dt)
    User.calPayment(users)

if __name__ == '__main__':
    main()
