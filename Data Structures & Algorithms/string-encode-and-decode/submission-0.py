class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ''
        for string in strs:
            encoded_string += str(len(string))+'#'+string
        return encoded_string

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0

        while i < len(s):
            separator = i
            while s[separator] != '#':
                separator += 1
            
            length = int(s[i:separator])
            word_start = separator + 1
            word_end = word_start + length
            
            result.append(s[word_start:word_end])
            i = word_end

        return result




                



            

                
            
            
           
