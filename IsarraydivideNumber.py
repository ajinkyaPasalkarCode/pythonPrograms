"""
Assignment - 42 : 2nd July'2024
Return the array of only numbers which is div by 3 and 5.
input : {10,33,30,44,60,2,23,56,0,78}
output : {30,60}
NOTE : to print array you can use System.out.println(Arrays.toString(outputArr));

"""

class IsarraydivideNumber:
    def getdivideNumber(self,input_num):
        new_array=[]
        for num in input_num:
            if num%3==0 and num%5==0:
                new_array.append(num)
        print(f"New Array : {new_array}")

a=IsarraydivideNumber()
a.getdivideNumber([10,33,30,44,60,2,23,56,0,78])