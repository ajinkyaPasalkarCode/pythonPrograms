"""
WAP find largest elements in array
"""
class Imp_program_5:
    def getSmallest_arr_ele(self,input_array):
        smallest=input_array[0]
        for num in input_array:
            if num<smallest:
                smallest=num
        print(f"Smallest element :{smallest}")

inp_array=int(input("Enter user wan't array elements :"))
num1=[]
for i in range(inp_array):
    arr_ele=int(input("Enter the elements :"))
    num1.append(arr_ele)

a=Imp_program_5()
a.getSmallest_arr_ele(num1)