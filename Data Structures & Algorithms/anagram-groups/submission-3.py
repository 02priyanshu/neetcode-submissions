class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        count = defaultdict(list)

        for i in strs:
            sortedS = ''.join(sorted(i))
            count[sortedS].append(i)

        return list(count.values())