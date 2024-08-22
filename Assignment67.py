"""
Assignment - 67 : 15th July'2024 [IMP]
return uniquely present characters from given string.
input : aakanksha
output : nsh

"""
class Assignment67:
    def getunique_char(self,input_str):
        res_dic={}
        for ch in input_str:
            if ch in res_dic:
                res_dic[ch]+=1
            else:
                res_dic[ch]=1

        for char in res_dic:
            if res_dic[char]>0 and res_dic[char]<=1:
                print(char, end="")
a=Assignment67()
a.getunique_char("aakanksha")