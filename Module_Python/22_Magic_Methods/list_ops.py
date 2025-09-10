# __setitem__
#mylist[0]=90# mylist.__setitem__(90)
class MyDemo:
  def __init__(self):
    self.items=[]

  def __setitem__(self,index,value):
    self.items[index]=value

my_list=MyDemo()
my_list=[10,20,30]
my_list[1]=25
print(my_list)
print(my_list[1])