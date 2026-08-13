class Solution:
    #universal solution, no ascii only cheat code
    def encode(self, strs: List[str]) -> str:
        encoded = str()
        # add the strings length and a marker for decoder to use, the marker can be ascii or not, so its universal
        for string in strs:
            length = len(string)
            encoded += str(length)+"@"+string 
        return(encoded)


    def decode(self, s: str) -> List[str]:
        decoded = list()
        i = 0
        while i < len(s):
            j = i

            # find how many characters the length of the next string spans using our marker (2 vs 20 vs 200 all is 1 char vs 2 vs 3)
            while s[j] != "@":
                j+=1
            length = int(s[i:j]) # use i and j now for string length

            next_string = s[j+1:j+1+length] #slice next string in the encoding using j and string's length
            decoded.append(next_string)

            i = j+1+length #update i for next string, should be pointed to first char of next string's length number
        return(decoded)
