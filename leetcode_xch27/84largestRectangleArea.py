'''
给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。

求在该柱状图中，能够勾勒出来的矩形的最大面积。

 



以上是柱状图的示例，其中每个柱子的宽度为 1，给定的高度为 [2,1,5,6,2,3]。

 



图中阴影部分为所能勾勒出的最大矩形面积，其面积为 10 个单位。

 

示例:

输入: [2,1,5,6,2,3]
输出: 10
通过次数 137,619 提交次数 321,091
在真实的面试中遇到过这道题？

是

否


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/largest-rectangle-in-histogram
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
https://leetcode-cn.com/problems/largest-rectangle-in-histogram/solution/84-zhu-zhuang-tu-zhong-zui-da-de-ju-xing-h8xb/
'''
class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        朴素法。 枚举每个矩形高度，然后中心扩散到两边。
        """
        if not heights:
            return 0
        res = 0
        for i in range(len(heights)):
            m = i
            n = i
            h = heights[i]
            while m > 0 and heights[m-1] >= h:
                m -= 1
            while n < len(heights) -1 and heights[n+1] >= h:
                n += 1
            res = max(res, h * (n - m + 1))
        return res

    def largestRectangleArea_stack(self, heights):
        # time O(n), space O(n)
        if not heights:
            return 0
        stack = []
        heights = [0] + heights + [0] # [0,2,1,5,6,2,3,0]
        res = 0
        for i in range(len(heights)):
            # stack[-1]是栈底，要存最小的
            while stack and heights[stack[-1]] > heights[i]: #栈底存的不是最小的，要pop掉
                idx = stack.pop()   #栈底高的要pop掉，对应的是那个高度
                res = max(res, heights[idx] * (i - stack[-1] - 1)) #长度是新加入的index- 上一个新加的index
            stack.append(i)
            # print(heights[:i+1],stack)
        return res
    def sss(self,heights):
        if not heights:
            return 0
        stack=[]
        heights=[0]+heights+[0]
        res=0
        n=len(heights)
        for i in range(n):
            while stack and heights[stack[-1]] > heights[i]:
                idx=stack.pop()
                res=max(res,heights[idx]*(i-stack[-1]-1))
            stack.append(i)
        return res

if __name__ == '__main__':
    x=[2,1,5,6,2,3]
    print(Solution().largestRectangleArea(x))
    print(Solution().largestRectangleArea_stack(x))
    print(Solution().sss(x))
