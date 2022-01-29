class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        ans = 0
        for (i, height) in enumerate(heights + [0]):
            while stack and stack[-1][0] > height:
                (h, _) = stack.pop()
                start = stack[-1][1] if stack else -1
                w = i - start - 1
                ans = max(ans, h*w)
      
            stack.append((height, i))
            
        return ans
        