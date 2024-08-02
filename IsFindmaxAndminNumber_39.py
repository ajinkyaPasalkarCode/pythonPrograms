"""
Assignment - 39 : 30th Jun'2024 [20 mins]
write a method to return max number from given array.
write an another method to return min number from given array.
input : {11,-33,22,44,56,23}
output : 56 is max number from given array
-33 is the mininum num from given array.

"""
class IsfindmaxNumber:
  def getmaxNumber(self,input_array):
    max_num=input_array[0]
    #max_num=0
    for num in input_array:
      if  num>max_num:
        max_num=num
    #print(" maximum number is :",max_num)
    return max_num

  def getminNumber(self,input_array):
    min_num=input_array[0]
    for num in input_array:
      if num<min_num:
        min_num=num
    return min_num
    #print("Minimum number :",min_num)

  def display(self):
    a=self.getmaxNumber([11,-33,22,44,56,23])
    b=self.getminNumber([11,-33,22,44,56,23,-99])

    print("Max number :",a)
    print("Min number :",b)


a=IsfindmaxNumber()
#a.getmaxNumber([11,-33,22,44,56,23])
#a.getminNumber([11,-33,22,44,56,23,-99])
a.display()