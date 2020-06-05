import sys


def is_card_valid(id):
    if id == '1234':
        return True
    return False


def get_balance(p_card_id):
    if p_card_id == '1234':
        return 110000
    return 0


def withdraw_money(p_money, p_balance):
    print('출금 {} 원  잔고 {} 원'.format(p_money, p_balance))


def get_atm_balance():
    return 500000


def set_atm_balance(p_atm_balance):
    print('현재 ATM 잔고 {}'.format(p_atm_balance) )


card_id = sys.argv[1]
withdraw = int(sys.argv[2])

# card id를 확인한다.
if is_card_valid(card_id):
    atm_balance = get_atm_balance()

    # ATM 잔고 확인
    if atm_balance >= withdraw:
        atm_balance -= withdraw
        set_atm_balance(atm_balance)

        # 개인 잔고 확인
        balance = get_balance(card_id)
        if balance >= withdraw:
            balance -= withdraw
            withdraw_money(withdraw, balance)

        else:
            raise ValueError('잔고 부족')
    else:
        raise ValueError('ATM 잔고 부족')


else:
    raise ValueError('Card ID가 맞지 않습니다.')
