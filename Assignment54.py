"""
Assignment - 54 : 5th July'2024 [IMP]
Print repeatative characters from given String.
input : aakanksha
output : ak

"""


class Assignment54:
    def getRepeatecharfind(self, input_string):
        new_list = []
        new_rep = []
        count = 0
        for ch in input_string:
            if ch in new_list:
                if ch not in new_rep:
                    new_rep.append(ch)
            else:
                new_list.append(ch)
        print(f"{new_rep}")


a = Assignment54()
a.getRepeatecharfind("aakanksha")
