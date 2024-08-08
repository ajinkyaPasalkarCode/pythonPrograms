"""
Assignment - 53 : 5th July'2024 [IMP]
Print non repeatative characters from given String.
input : aakanksha
output : nsh

"""


class Assignment53:
    def getNon_repete_char(self, input_string):
        new_dic = {}
        count = 0
        for ch in input_string:
            if ch in new_dic:
                new_dic[ch] += 1
            else:
                new_dic[ch] = 1

        for char in new_dic:
            # print(f"{char}->{new_dic[char]}")   #find count by using dictionary

            if new_dic[char] > 0 and new_dic[char] <= 1:
                print(char, end="")  # end='' print in single line


a = Assignment53()
a.getNon_repete_char("aakanksha")
