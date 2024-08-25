"""
    WAP print the largest element in array
"""

class Imp_program_5:
    def getLargest_ele(self,input_array):
        largest= input_array[0]
        for num in input_array:
            if num>largest:
                largest=num
        print(f"Largest Number :{largest}")

inp_array=int(input("Enter the Elements user wan't in array :"))
num1=[]
for i in range(inp_array):
    arr_ele=int(input("Enter the Elements in array :"))
    num1.append(arr_ele)

a=Imp_program_5()
a.getLargest_ele(num1)