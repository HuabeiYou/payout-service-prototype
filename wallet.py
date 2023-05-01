from typing import List, Optional
from enum import Enum


class Currency(Enum):
    RMB = "RMB"
    CAD = "CAD"
    USD = "USD"
    GBP = "GBP"
    AUD = "AUD"


class Wallet:
    def __init__(
        self,
        id: int,
        balance: float,
        currency: Currency,
        user_id: int,
    ):
        self.id = id
        self.user_id = user_id
        self.balance = balance
        self.currency = currency

    def __str__(self) -> str:
        return f"Wallet(id={self.id}, user_id={self.user_id}, balance={self.balance}, currency={self.currency})"

    def add_funds(self, amount: float) -> None:
        self.balance += amount
        return

    def remove_funds(self, amount: float) -> None:
        self.balance -= amount
        return


class WalletRepository:
    def __init__(self):
        self.counter = 1
        self.data: List[Wallet] = []

    def __len__(self) -> int:
        return len(self.data)

    def __str__(self) -> str:
        wallet_strs = [str(wallet) for wallet in self.data]
        return f"WalletRepository [{', '.join(wallet_strs)}]"

    def create_one(self, balance: float, currency: Currency, user_id: int) -> Wallet:
        wallet = Wallet(
            id=self.counter,
            balance=balance,
            currency=currency,
            user_id=user_id,
        )
        self.data.append(wallet)
        self.counter += 1
        return wallet

    def delete_one_by_id(self, id: int) -> None:
        self.data = [x for x in self.data if x.id != id]
        return

    def find_one(
        self,
        id: Optional[int] = None,
        user_id: Optional[int] = None,
        currency: Optional[Currency] = None,
    ) -> Optional[Wallet]:
        for elem in self.data:
            if (
                (id is None or elem.id == id)
                and (user_id is None or elem.user_id == user_id)
                and (currency is None or elem.currency == currency)
            ):
                return elem
        return None
