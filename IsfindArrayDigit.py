"""
Assignment - 40 : 30th Jun'2024 [40 mins]
find total number of digits in array.
input : {"tec1hn3o","cr1e1d1i1t1s","india","pune1","A22nvit","tirth"}
output : 14

"""


class IsfindArrayDigit:
    def getDigit(self, input_array):
        count = 0
        new_array=input_array[0]
        for char in input_array:
            for ch in char:
                #if ch.isdigit():
                if ch>='0' and ch <='9':      # without isdigit method
                    count=count+int(ch)
        print("count :", count)


a = IsfindArrayDigit()
a.getDigit(["tec1hn3o", "cr1e1d1i1t1s"])
