class Solution:
    def reorganizeString(self, s: str) -> str:
        counts = {}

        for char in s:
            counts[char] = counts.get(char,0) + 1
        
        result = []
        previous = ""

        while len(result) < len(s):
            choice = ""

            for char in counts:
                if char != previous and counts[char] > 0:
                    if choice == "" or counts[char] > counts[choice]:
                        choice = char
            
            if choice == "":
                return ""
            
            result.append(choice)
            counts[choice] -= 1
            previous = choice
        
        return "".join(result)