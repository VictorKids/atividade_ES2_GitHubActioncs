import unittest
import bank_acc

class Test_Bank_Account(unittest.TestCase):

    def test_creat_bank_account(self):
        BA = bank_acc.Bank_account(100, 1000)
        self.assertEqual(BA.money, 100)

    def test_deposit(self):
        BA = bank_acc.Bank_account(100, 1000)
        BA.deposit(100)
        self.assertEqual(BA.money, 200)

    def test_withdraw_sucess(self):
        BA = bank_acc.Bank_account(100, 1000)
        BA.withdraw(50)
        self.assertEqual(BA.money, 50)

    def test_withdraw_fail(self):
        BA = bank_acc.Bank_account(100, 1000)
        BA.withdraw(150)
        self.assertEqual(BA.money, 100)

    def test_use_nonblock_credit_card_sucess(self):
        BA = bank_acc.Bank_account(100, 1000)
        BA.use_credit_card(100)
        self.assertEqual(BA.used_credits, 100)
        
    def test_use_block_credit_card(self):
        BA = bank_acc.Bank_account(100, 1000)
        BA.blocked_card = True
        BA.use_credit_card(100)
        self.assertEqual(BA.used_credits, 0)

    def test_use_nonblock_credit_card_fail(self):
        BA = bank_acc.Bank_account(100, 1000)
        BA.use_credit_card(1001)
        self.assertEqual(BA.used_credits, 0)

    def test_credit_payment_with_enought_money(self):
        BA = bank_acc.Bank_account(100, 1000)
        BA.used_credits = 100
        BA.credit_payment()
        self.assertEqual(BA.used_credits, 0)
    
    def test_credit_payment_without_enought_money(self):
        BA = bank_acc.Bank_account(100, 1000)
        BA.used_credits = 300
        BA.credit_payment()
        self.assertEqual(BA.used_credits, 200)
    

 