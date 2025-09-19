# class InvalidBalanceError(Exception):
#   def __init__(self,message):
#     super().__init__(message)


# def withdraw(balance=5000,amount=0):
#   if amount>balance:
#       raise InvalidBalanceError("Insufficient funds")
#   else :
#     print(f"withdraw successful balance :{balance-amount} amount :{amount}")

# try:
#   amount=int(input('Enter the amount to withdraw: Rs.'))
#   withdraw(5000,amount)
# except InvalidBalanceError as ibe :
#   print(ibe)
# except ValueError as ve:
#   print(ve)
# except Exception as e:
#   print(e)
# finally:
#   print("End of Program")

s = {31,12,4,134,46}
s1 = {1,2,3,5}
print(s.isdisjoint(s1))
# print(s.pop())

# my_frozen = frozenset([1, 2, 3])
# for item in my_frozen:
#   print(item)
