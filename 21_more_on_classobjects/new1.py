class Employee:
  def __init__(self,name,salary):
    self._name=name
    self._salary=salary

  @property
  def name(self):
    return self._name

  @property
  def salary(self):
    return self._salary

  @name.setter
  def name(self, new_name):
    self._name = new_name

  @salary.setter
  def salary(self, new_salary):
    self._salary = new_salary

  @name.deleter
  def name(self):
    print("Deleting Name")
    del self._name

  @salary.deleter
  def salary(self):
    print("Deleting Salary")
    del self._salary


obj = Employee("Adarsh", 50000)
print(obj.name)
print(obj.salary)
obj.salary = 400
obj.name = "Amit"
print(obj.name)
print(obj.salary)
del obj.name
print(obj.salary)
print(obj.name)
