class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for i in nums:
                count[i] = 1 + count.get(i, 0)

        freq = []
        for j in range(0,k):
            temp=0
            key=0
            for i in count.keys():
                if i in freq:
                    continue
                if count[i] > temp:
                    temp = count[i]
                    key = i
            freq.append(key)
        
        return freq