
"""
Assignment - 48 : 5th July'2024
Print frequency of each character in a given string.
input : aakanksha
output : a -> 4
a -> 4
k -> 2
a -> 4
n -> 1
k -> 2
s -> 1
h -> 1
a -> 4
"""


class AssignmentNo48:
    def getcharFrequencycount(self,input_string):
        frequency={}                 # Dictionary used key and value
        for ch in input_string:
            if ch in frequency:
                frequency[ch]+=1
            else:
                frequency[ch]=1
        for char in input_string:
            print(f"{char}->{frequency[char]}")
a=AssignmentNo48()
a.getcharFrequencycount("aakanksha")