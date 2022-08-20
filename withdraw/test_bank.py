import unittest
from unittest import TestCase
from implement import InitializeUser, BankTransfer


class TestInitialUser(TestCase):
    u = InitializeUser('name', 'password')

    def test_all_needed_params_is_ok(self):
        self.assertEqual(self.u.name, 'name')
        self.assertEqual(self.u.password, 'password')
        self.assertEqual(self.u.amount, 0.00)

    def test_missing_params(self):
        with self.assertRaises(TypeError):
            not_valid = InitializeUser('name')

        with self.assertRaises(TypeError):
            not_valid = InitializeUser(password='name')

    def test_repr(self):
        initial = f'{self.u.name} has {self.u.amount:.2f} in this moment'
        self.assertEqual(repr(self.u), initial)


class TestBankTransfer(TestCase):
    u = InitializeUser('name', 'password')
    bank = BankTransfer(u, 'password')

    def test_correct(self):
        self.assertEqual(self.u.name, 'name')

    def test_bank_account_with_not_correct_password(self):
        with self.assertRaises(AssertionError):
            incorrect_bank = BankTransfer(self.u, 'pass')

    def test_make_deposite_with_correct_parameter(self):
        self.bank.deposit(100)
        self.assertEqual(self.u.amount, 100.00)

    def test_make_deposite_with_negative_sign(self):
        with self.assertRaises(AssertionError):
            self.bank.deposit(-100)

    def test_withdraw_with_not_correct_sign(self):
        with self.assertRaises(AssertionError):
            self.bank.withdraw(-100)

    def test_withdraw_with_correct_params_and_when_have_needed_money(self):
        self.bank.withdraw(100)
        self.assertEqual(self.u.amount, 0.00)

    def test_withdraw_with_correct_params_and_when_not_have_needed_money(self):
        with self.assertRaises(ValueError) as e:
            self.bank.withdraw(100)
        self.assertEqual(str(e.exception), 'Can not drawe more than you have')


if __name__ == '__main__':
    unittest.main()
