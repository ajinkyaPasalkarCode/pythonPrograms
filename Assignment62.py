"""
Assignment - 62 : 11th July'2024
Find the vowel having max frequency.
input : Deharmadhikari : a -> 3
Entertainment : e -> 3
Persistent : e -> 2

"""
from itertools import count


class Ismaxfreq:
  def getMax_fre(self,input_string):
    max_dic={}
    index=0
    while index<len(input_string):
      ch=input_string[index]
      if ch in max_dic:
        max_dic[ch]+=1
      else:
        max_dic[ch]=1
      index+=1

    max_char=None
    max_count=0
    for ch in max_dic:
        if max_dic[ch]>max_count:
            max_count=max_dic[ch]
            max_char=ch

    print(f"{max_char}->{max_count}")

inpstr=input("Enter the string :")
maxstr=Ismaxfreq()
maxstr.getMax_fre(inpstr)