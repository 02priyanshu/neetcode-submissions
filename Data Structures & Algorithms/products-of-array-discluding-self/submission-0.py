class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        list = []
        for i in range(len(nums)):
            pr = 1
            for j in range(len(nums)):
                if i==j :
                    continue
                else:
                    pr = pr * nums[j]
            list.append(pr)
        return list