class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace('.', '[.]')
    

class Solution:
    def defangIPaddr(self, address: str) -> str:
        result = []

        for char in address:
            if char == '.':
                result.append('[.]')
            else:
                result.append(char)
        
        return ''.join(result)
    
