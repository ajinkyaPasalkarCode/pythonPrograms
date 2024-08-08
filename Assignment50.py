"""
Assignment - 50 : 5th July'2024 [IMP]
Print frequency of each character in a given string.
input : aakanksha
output : a -> 4
k -> 2
n -> 1
s -> 1
h -> 1

"""


class Assignment50:
    def getcal_CharFreq(self, input_string):
        frequency = {}
        for char in input_string:
            if char in frequency:
                frequency[char] += 1
            else:
                frequency[char] = 1
        for ch in frequency:
            print(f"{ch}->{frequency[ch]}")


a = Assignment50()
a.getcal_CharFreq("aakanksha")
