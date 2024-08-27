"""
WAP to sort elements in array in ascending order
"""
class Imp_program_7:
    def getRevers_order(self,input_array):
        n=len(input_array)
        for i in range(1,n):
            key=input_array[i]
            j=i-1
            while j>=0 and key<input_array[j]:
                input_array[j+1]=input_array[j]
                j=j-1
            input_array[j+1]=key
        print(input_array)
a=Imp_program_7()
a.getRevers_order([12,1,8,5,2])




