class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        results = []
        anagrams = {}
        for word in strs:
            signature = "".join(sorted(word))
            if signature in anagrams:
                anagrams[signature].append(word)
            else:
                anagrams[signature] = [word]
        return list(anagrams.values())