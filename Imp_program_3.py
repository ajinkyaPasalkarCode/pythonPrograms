"""
WAP Print elements of an array in reverse order
"""
class Imp_program_3:
    def getReverse_order(self,input_array):
        rev_list=[]
        for num in range(len(input_array)-1,-1,-1):
            rev_list.append(input_array[num])
        print(rev_list)


inp_array=int(input("Enter the array Elements user wan't :"))
num1=[]
for i in range(inp_array):
    arr_ele=input("Enter the Elements in array :")
    num1.append(arr_ele)

a=Imp_program_3()
a.getReverse_order(num1)