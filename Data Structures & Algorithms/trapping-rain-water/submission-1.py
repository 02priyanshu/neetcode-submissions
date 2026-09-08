class Solution:
    def trap(self, height: List[int]) -> int:
        n= len(height)
        prefix = [0]*n
        sufix = [0]*n
        count=0

        prefix[0] = sufix[n-1] = 0

        for i in range(1, n):
            prefix[i] = prefix[i-1] if prefix[i-1] > height[i-1] else height[i-1]

        for j in range(n-1, 0, -1):
            sufix[j-1] = sufix[j] if sufix[j] > height[j] else height[j]

        for i in range(1, n-1):
            area = min(prefix[i], sufix[i]) - height[i]
            if area > 0:
                count = count + area

        return count