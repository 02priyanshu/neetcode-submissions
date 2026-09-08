class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for i in nums:
            count[i] = 1 + count.get(i, 0)

        count = dict(sorted(count.items(), key=lambda item: item[1], reverse=True))
        l=[]
        for j in count:
            if len(l) < k:
                l.append(j)

        return l