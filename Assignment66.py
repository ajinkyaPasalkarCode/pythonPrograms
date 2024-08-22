"""
Assignment - 66 : 13th July'2024
return intersecition of 2 array.
input : {10,33,24,55,109}
{4,109,33,12,100}
output : {33,109,0,0,0}

"""
class Assignment66:
    def getinterception_arr(self,input_arr1, input_arr2):
        res_inter_arr=[]
        count=0
        for i in range(len(input_arr1)):
            # check array1 elements present in array2
            if input_arr1[i] in input_arr2 and input_arr1[i] not in res_inter_arr:
                res_inter_arr.append(input_arr1[i])
                count+=1

        print(res_inter_arr)

input_str1=input("Enter the string1....") # input a string
num1=list(map(int, input_str1.split())) # Convert input into list of integers

input_str2=input("Enter the string2...") #input a string
num2=list(map(int, input_str2.split())) #Convert input into list of integers

a=Assignment66()
a.getinterception_arr(num1,num2)
