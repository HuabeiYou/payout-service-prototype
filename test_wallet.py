import unittest
from wallet import Wallet, Currency, WalletRepository


class TestWallet(unittest.TestCase):
    def test_add_funds(self):
        wallet = Wallet(id=0, balance=100.0, currency=Currency.RMB, user_id=1)
        wallet.add_funds(25.0)
        self.assertEqual(wallet.balance, 125.0)

    def test_remove_funds(self):
        wallet = Wallet(id=1, balance=100.0, currency=Currency.RMB, user_id=1)
        wallet.remove_funds(25.0)
        self.assertEqual(wallet.balance, 75.0)

    def test_str(self):
        wallet = Wallet(id=3, balance=100.0, currency=Currency.CAD, user_id=1)
        self.assertEqual(
            str(wallet), "Wallet(id=3, user_id=1, balance=100.0, currency=Currency.CAD)"
        )


class TestWalletRepository(unittest.TestCase):
    def setUp(self):
        self.repo = WalletRepository()

    def test_create_one(self):
        wallet = self.repo.create_one(user_id=2, balance=100, currency=Currency.RMB)
        self.assertNotIn(wallet.id, [0, None])
        self.assertEqual(wallet.user_id, 2)
        self.assertEqual(wallet.balance, 100)
        self.assertEqual(wallet.currency, Currency.RMB)

    def test_delete_one_by_id(self):
        wallet = self.repo.create_one(user_id=1, balance=100, currency=Currency.RMB)
        self.repo.delete_one_by_id(wallet.id)
        self.assertIsNone(self.repo.find_one(id=wallet.id))

    def test_find_one(self):
        wallet1 = self.repo.create_one(user_id=3, balance=100, currency=Currency.RMB)
        wallet2 = self.repo.create_one(user_id=3, balance=200, currency=Currency.USD)
        self.assertEqual(self.repo.find_one(id=wallet1.id), wallet1)
        self.assertEqual(self.repo.find_one(id=wallet2.id), wallet2)
        self.assertEqual(self.repo.find_one(user_id=3, currency=Currency.RMB), wallet1)
        self.assertEqual(self.repo.find_one(user_id=3, currency=Currency.USD), wallet2)
        self.assertIsNone(self.repo.find_one(id=99999))


if __name__ == "__main__":
    unittest.main()
