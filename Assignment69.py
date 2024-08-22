"""
Assignment - 69 : 15th July'2024
return uniquely present letters followed by digit(s) from given string.
input : aakan1ksh44a
output : nh

"""
class Assignment69:
    def getUnique(self,input_str):
        new_dic={}
        for ch in input_str:
            # isdigit() method is used for find digit in character and skip digit
            if ch.isdigit():
                continue
            # Counting occurrences of characters (non-digits)
            if ch in new_dic:
                new_dic[ch]+=1
            else:
                new_dic[ch]=1
        # Print characters that appear exactly once
        for char in new_dic:
            if new_dic[char]>0 and new_dic[char]<=1:
                print(char,end="")
        print()

str1=int(input("How many string you want :"))
num1=[]
for i in range(str1):
    inp_str=input(f"Enter the string {i+1}")
    num1.append(inp_str)

# Creating an instance of the class and calling the method
a=Assignment69()
for string in num1:
    a.getUnique(string)

#a=Assignment69()
#a.getUnique("aakan1ksh44a")