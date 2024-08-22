"""
Assignment - 70 : 15th July'2024
return uniquely present first vowel letter followed by digit(s) from given string.
input : aakan1ksi44au3p
output : i
"""

class Assignment70:
    def getunique_Vowel(self,input_str):
        new_dic={}
        vowel='aeiouAEIOU'
        for ch in input_str:
            #check if digit is present in charater if present skip and continue
            if ch.isdigit():
                continue
            # if character is vowel then go inside the if loop
            if ch in vowel:
                if ch in new_dic:
                    new_dic[ch]+=1
                else:
                    new_dic[ch]=1
        # this for loop used for print unique character
        for char in new_dic:
            if new_dic[char]>0 and new_dic[char]<=1:
                print(char,end="")
        print()

inp_num=int(input("how many string you wan't :"))
num1=[]
# for loop used for multiple input
for i in range(inp_num):
    inp_str=input(f"Enter the string {i+1} :")
    num1.append(inp_str)

# create a class object
a=Assignment70()

# This loop are used for input pass to main method
for string in num1:
    a.getunique_Vowel(string)
