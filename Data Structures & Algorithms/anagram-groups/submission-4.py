class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = defaultdict(list)

        for i in strs:
            j = ''.join(sorted(i))
            seen[j].append(i)

        return list(seen.values())