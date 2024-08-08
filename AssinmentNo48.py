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