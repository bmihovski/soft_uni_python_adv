class Account:
    def __init__(self, id: int, balance: int, pin: int):
        self._id = id
        self.balance = balance
        self.__pin = pin

    def get_id(self, pin: int):
        return self._id if pin == self.__pin else "Wrong pin"

    def get_balance(self):
        return self.balance

    def change_pin(self, old_pin: int, new_pin: int):
        if old_pin != self.__pin:
            return "Wrong pin"
        self.__pin = new_pin
        return "Pin changed"


account: Account = Account(8827312, 100, 3421)
print(account.get_id(1111))
print(account.get_id(3421))
print(account.get_balance())
print(account.change_pin(2212, 4321))
print(account.change_pin(3421, 1234))
