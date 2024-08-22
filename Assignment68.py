"""
return uniquely present characters from given string array.
input : {aakanksha, techno, rutuja }
output : {nh, techno, rtja}

"""

class Assignment68:
    def getunique_char(self,input_str):
        res_dic={}
        for ch in input_str:
            if ch in res_dic:
                res_dic[ch]+=1
            else:
                res_dic[ch]=1

        for char in res_dic:
            if res_dic[char]>0 and res_dic[char]<=1:
                print(char,end="")
        print()


num_str=int(input("Enter how many string you want..?"))
str1=[]
for i in range(num_str):
    inp_str = input(f"Enter the string {i+1}:")
    str1.append(inp_str)

a=Assignment68()
for string in str1:
    a.getunique_char(string)

