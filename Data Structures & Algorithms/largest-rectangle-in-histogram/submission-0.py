class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0
        for i,h in enumerate(heights):
            start = i
            while stack and stack[-1][1] > h:
                index,height = stack.pop()
                width = i - index
                maxArea = max(maxArea,width * height)
                start = index
            stack.append((start,h))
        for index,height in stack:
            width = len(heights) - index
            area = height * width
            maxArea = max(maxArea,area)
        return maxArea