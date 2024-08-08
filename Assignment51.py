"""
Assignment - 51 : 5th July'2024 [IMP]
Print frequency of each vowel character in a given string.
input : technocredits
output : e -> 2
o -> 1
i -> 1

"""


class Assignment51:
    def getFrecountVowel(self, input_string):
        vowel = 'aeiouAEIOU'
        frequency = {}
        for char in input_string:
            if char in vowel:
                if char in frequency:
                    frequency[char] += 1
                else:
                    frequency[char] = 1

        for ch in frequency:
            print(f"{ch}->{frequency[ch]}")


freCount = Assignment51()
freCount.getFrecountVowel("technocredits")
