class InvalidBalanceError(Exception):
  def __init__(self,message):
    super().__init__(message)


def withdraw(balance=5000,amount=0):
  if amount>balance:
      raise InvalidBalanceError("Insufficient funds")
  else :
    print(f"withdraw successful balance :{balance} amount :{amount}")

try:
  amount=int(input('Enter the amount to withdraw'))
  withdraw(5000,amount)
except InvalidBalanceError as ibe :
  print(ibe)
except ValueError as ve:
  print(ve)
except Exception as e:
  print(e)
finally:
  print("End of Program")

