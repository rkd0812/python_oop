import sys


class Customer:
    def __init__(self):
        self.card_id = '1234'
        self.balance = 101000

    def withdraw(self, money):
        if self.balance >= money:
            self.balance -= money
            print('출금 {} 원  잔고 {} 원'.format(money, self.balance))
        else:
            raise ValueError('잔고 부족')


class ATM:
    def __init__(self):
        self.balance = 500000

    def withdraw(self, money):
        if self.balance >= money:
            self.balance -= money
            print('현재 ATM 잔고 {}'.format(self.balance))
        else:
            raise ValueError('ATM 잔고 부족')

    @staticmethod
    def card_id_validate(p_card_id):
        if p_card_id == '1234':
            return True
        return False


card_id = sys.argv[1]
withdraw = int(sys.argv[2])

if ATM.card_id_validate(card_id):
    ATM().withdraw(withdraw)
    Customer().withdraw(withdraw)
else:
    raise ValueError('Card ID가 맞지 않습니다.')
