class Solution:
    def countAndSay(self, n: int) -> str:
        current = "1"
        
        for _ in range(2, n + 1):
            next_string = []
            i = 0
            length = len(current)
            
            while i < length:
                count = 1
                # Count consecutive identical characters
                while i + 1 < length and current[i] == current[i + 1]:
                    count += 1
                    i += 1
                
                # Append count and character
                next_string.append(str(count))
                next_string.append(current[i])
                i += 1
                
            current = "".join(next_string)
            
        return current
        