"""
Program 1 : Reverse index order from given Array, write a method to accept an array and return new
array by reversing index order.
input : {"Prajakta", "Bhairavi", "Chaitanya", "Vishakha", "Pooja"}
output : {"Pooja", "Vishakha", "Chaitanya", "Bhairavi", "Prajakta"}

"""
class IsreverseIndexorder:
    def getReverseorder(self,input_string):
        rev_array=[]
        for char in  range(len(input_string)-1,-1,-1):
            rev_array.append(input_string[char]);
        print(rev_array)

a=IsreverseIndexorder();
a.getReverseorder(["Prajakta", "Bhairavi", "Chaitanya", "Vishakha", "Pooja"]);


