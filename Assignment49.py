"""
Assignment - 49 : 5th July'2024
Print frequency of each vowel character in a given string.
input : technocredits
output : e -> 2
o -> 1
e -> 2
i -> 1

"""
class Assignment49:
    def getVowelfre(self, input_string):
        vowel = 'aeiouAEIOU'
        frequency = {}
        for char in input_string:
            if char in vowel:
                if char in frequency:
                    frequency[char] += 1
                else:
                    frequency[char] = 1

        for ch in input_string:
            if ch in vowel:
                print(f"{ch}->{frequency[ch]}")


a = Assignment49()
a.getVowelfre("technocredits")