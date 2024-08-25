"""
WAP print sum of all the item in array
"""
class Imp_program_6:
    def getSum_arr_ele(self,input_array):
        arr_sum=0
        for num in input_array:
            arr_sum+=num
        print(f"Sum:{arr_sum}")

num1=[]
for i in range(0,5):
    arr_ele=int(input("Enter the elements :"))
    num1.append(arr_ele)

a=Imp_program_6()
a.getSum_arr_ele(num1)
