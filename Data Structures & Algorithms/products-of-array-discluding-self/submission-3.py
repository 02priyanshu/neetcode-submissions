class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [0]*n
        sufix = [0]*n
        zeroCount=0

        prefix[0] = sufix[n-1] = 1
        for i in range(1, n):
            if nums[i-1] == 0:
                zeroCount = zeroCount + 1
            prefix[i] = prefix[i-1]*nums[i-1]

        if zeroCount > 2 : return [0]*n

        for j in  range(n-1,0, -1):
            sufix[j-1] = sufix[j]*nums[j]

        print(prefix)
        print(sufix)
        out = [0]*n

        for i in range(n):
            out[i] = prefix[i]*sufix[i]
        return out