class InitializeUser:

    def __init__(self, name: str, password: str, amount: float = 0.00):
        self.name = name
        self.password = password
        self.amount = amount

    def __repr__(self):
        return f'{self.name} has {self.amount:.2f} in this moment'


def check_correct_sign(money):
    assert money > 0


class ValidateUserPassword:
    def __init__(self, account: InitializeUser, password: str):
        self.user_password = password
        self.account = account


class BankTransfer(ValidateUserPassword):

    def __init__(self, account: InitializeUser, password: str):
        super().__init__(account, password)
        assert password == account.password

    def deposit(self, amount):

        # validate sign of the money
        check_correct_sign(amount)
        self.account.amount += amount
        print(self.account.amount)

    def withdraw(self, withdraw_amount):

        check_correct_sign(withdraw_amount)
        if withdraw_amount <= self.account.amount:
            self.account.amount -= withdraw_amount
        else:
            raise ValueError('Can not drawe more than you have')
        print(self.account.amount)


if __name__ == '__main__':
    user_one = InitializeUser('John', '123qwe')
    transfer = BankTransfer(user_one, '123qwe')
    transfer.deposit(100)
    transfer.withdraw(100)
