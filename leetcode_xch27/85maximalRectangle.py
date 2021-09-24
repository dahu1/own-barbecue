'''
给定一个仅包含 0 和 1 、大小为 rows x cols 的二维二进制矩阵，找出只包含 1 的最大矩形，并返回其面积。

 

示例 1：


输入：matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
输出：6
解释：最大矩形如上图所示。
示例 2：

输入：matrix = []
输出：0
示例 3：

输入：matrix = [["0"]]
输出：0
示例 4：

输入：matrix = [["1"]]
输出：1
示例 5：

输入：matrix = [["0","0"]]
输出：0
 

提示：

rows == matrix.length
cols == matrix[0].length
0 <= row, cols <= 200
matrix[i][j] 为 '0' 或 '1'
通过次数 73,915 提交次数 143,185
在真实的面试中遇到过这道题？

是

否


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximal-rectangle
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix:
            return 0
        m=len(matrix)
        n=len(matrix[0])
        heights=[[0] * n for _ in range(m)]
        heights[0]=[int(i) for i in matrix[0]]
        for i in range(1,m):
            for j in range(n):
                heights[i][j]=heights[i-1][j]+int(matrix[i][j]) if int(matrix[i][j]) !=0 else 0
        res=[self.largestRectangleArea(heights[i]) for i in range(m)]
        return max(res)
    def largestRectangleArea(self,height):
        if not height:
            return 0
        height=[0] + height + [0]
        stack=[]
        max_res=0
        for i in range(len(height)):
            while stack and height[stack[-1]] > height[i]:
                idx= stack.pop()
                max_res=max(max_res,height[idx]*(i-stack[-1]-1))
            stack.append(i)
        return max_res
if __name__ == '__main__':
    matrix = [["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"], ["1", "1", "1", "1", "1"],
              ["1", "0", "0", "1", "0"]]
    matrix=[]
    matrix=[['0','0']]
    x = [2, 1, 5, 6, 2, 3]
    print(Solution().maximalRectangle(matrix))
    # print(Solution().largestRectangleArea(x))
