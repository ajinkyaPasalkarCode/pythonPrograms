"""
WAP to print duplicate elements from array
"""
class Imp_program_2:
    def getDuplicate(self,input_array):
        array_ele={}
        dublicate=[]
        for element in input_array:
            if element in array_ele:
                array_ele[element]+=1
            else:
                array_ele[element]=1

        for ele in array_ele:
            if array_ele[ele]>1:
                dublicate.append(ele)
        print(dublicate)

#inp_array=int(input("Enter the array elements"))
#print(inp_array)
a=Imp_program_2()
a.getDuplicate([1,2,3,8,12,1,8])