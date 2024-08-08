"""
Assignment - 52 : 5th July'2024 [IMP]
Print all characters uniquely from given string.
input : aakanksha
output : aknsh

"""


class Assignment52:
    def getuniqueString(self, input_string):
        uniq_set = set();
        for ch in input_string:
            if ch not in uniq_set:
                uniq_set.add(ch)
        print(uniq_set)


uniqchar = Assignment52()
uniqchar.getuniqueString("aakanksha")