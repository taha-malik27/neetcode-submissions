class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = str()
        for string in strs:
            encoded += string + "π"  #little cheat code, using non ascii character as delimiter since restriction is ascii
        return(encoded)


    def decode(self, s: str) -> List[str]:
        decoded = list()
        str_maker = str()
        # simply reverse the encode process.
        for c in s:
            if c =="π":
                decoded.append(str_maker)
                str_maker = str()
                continue
            str_maker += c
        return(decoded)

