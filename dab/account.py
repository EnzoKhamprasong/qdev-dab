import sys

def checkWithdrawal(balance, amount):
  if 0<amount<=500 and amount<= balance:
    return True

class Account:
  def __init__(self, number, client="", initial_balance=0.0):
    self.number = number
    self.client = client
    self.balance = initial_balance

  def __str__(self):
    return f"Your current balance is {self.balance} €.\n"

  def __eq__(self, other):
    if self.number == other:
      return True
    else:
      return False

  def deposit(self, amount):
    self.balance += amount
    print("Deposit complete. New balance is %.2f" % self.balance)

  def withdraw(self, amount):
    try:
      if checkWithdrawal(self.balance, amount):
        self.balance -= amount
        print("Withdrawal complete. New balance is %.2f €" % self.balance)
      else:
        print("Withdrawal refused! Current balance is %.2f €" % self.balance)
    except ValueError:
      print("Error: unable to withdraw a negative amount!", file=sys.stderr)
