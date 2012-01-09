#!/usr/bin/env python

class User(object):
    def __init__(self, name, common, personal, balance, reserve, payment = 0):
        # reserve is currently not used
        self.name = name
        self.common = User.addUp(common)
        self.personal = User.addUp(personal)
        self.balance = float(balance)
        self.reserve = float(reserve)
        self.payment = float(payment)
        print 'Initial: %s(%s, %s, %s, %s, %s)' % (name, str(self.common), str(self.personal), str(balance), str(reserve), str(payment))

    @staticmethod
    def addUp(money):
        sum = 0.0
        if money is not None:
            for m in money:
                sum += float(m)
        return sum

    @staticmethod
    def calPayment(users):
        if users is not None:
            totalCommon = 0
            total = 0
            for user in users:
                totalCommon += user.common
            for user in users:
                aveCommon = totalCommon / len(users)
                user.payment = aveCommon + user.personal + user.balance
                total += user.payment
                print '''%s's payment: %s + %s + %s = %s''' % (user.name, str(aveCommon), str(user.personal), str(user.balance), str(user.payment))
        print 'total = %s' % total

                
# test
def test():
    user1 = User('name1', [1.0, 2.0], [3.5, 4.1], 9.7, 0)
    user2 = User('name2', [3.0, 4.0], [4.5, 5.1], 8.7, 0)
    User.calPayment([user1, user2])

if __name__ == '__main__':
    test()
