class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for i in nums:
            count[i] = 1 + count.get(i, 0)

        sor = sorted(count.items(), key=lambda item: item[1], reverse=True)
        count = dict(sor)
        keys=list(count.keys())
        lis = []
        for i in range(k):
            lis.append(keys[i])
        return lis