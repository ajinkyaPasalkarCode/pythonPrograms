"""
WAP Find the frequency of each elements in array
"""
class Imp_Program:
    def getFrequency(self,input_arr):
        new_dic={}
        for num in input_arr:
            if num in new_dic:
                new_dic[num]+=1
            else:
                new_dic[num]=1

        return new_dic

    def display(self,dic_new):
        for num2 in dic_new:
            if dic_new[num2]>0:
                print(f"{num2} ->{dic_new[num2]}")


elements=int(input("enter the array elements user wan't :"))
num1=[]
for i in range(elements):
    array_ele = input(f"Enter the Elements: ")
    num1.append(array_ele)

a=Imp_Program()
arr_num=a.getFrequency(num1)
a.display(arr_num)






