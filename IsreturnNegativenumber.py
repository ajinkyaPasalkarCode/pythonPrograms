"""
Assignment - 41
Return the array of only numbers which is negative
input : {-10,33,44,-55,-2,-23,56,0,78}
output : {-10,-55,-2,-23}

"""


class IsreturnNegativenumber:
    def getnegativeNumber(self,input_num):
        negativeNum=[]
        for num in input_num:
            if num<0 :
                negativeNum.append(num)
        print("Negative number :",negativeNum)

a=IsreturnNegativenumber()
a.getnegativeNumber([-10,33,44,-55,-2,-23,56,0,78])



