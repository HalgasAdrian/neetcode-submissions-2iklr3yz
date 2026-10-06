class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        for test in strs:
            sortedStrings = ''.join(sorted(test))
            result[sortedStrings].append(test)
        return list(result.values())
        