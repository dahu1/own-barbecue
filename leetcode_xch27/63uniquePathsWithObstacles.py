'''
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为 “Start” ）。

机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为 “Finish”）。

现在考虑网格中有障碍物。那么从左上角到右下角将会有多少条不同的路径？



网格中的障碍物和空位置分别用 1 和 0 来表示。

 

示例 1：


输入：obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
输出：2
解释：
3x3 网格的正中间有一个障碍物。
从左上角到右下角一共有 2 条不同的路径：
1. 向右 -> 向右 -> 向下 -> 向下
2. 向下 -> 向下 -> 向右 -> 向右
示例 2：


输入：obstacleGrid = [[0,1],[0,0]]
输出：1

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/unique-paths-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution(object):
    def uniquePathsWithObstacles_ans(self, obstacleGrid):
        height, width = len(obstacleGrid), len(obstacleGrid[0])
        store = [[0] * width for i in range(height)]

        # 从上到下，从左到右
        for m in range(height):  # 每一行
            for n in range(width):  # 每一列
                if not obstacleGrid[m][n]:  # 如果这一格没有障碍物
                    if m == n == 0:  # 或if not(m or n)
                        store[m][n] = 1
                    else:
                        a = store[m - 1][n] if m != 0 else 0  # 上方格子
                        b = store[m][n - 1] if n != 0 else 0  # 左方格子
                        store[m][n] = a + b
        return store[-1][-1]

    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        原点才是1，两个边不一定是1，可能有障碍物，两条边的值一定要是从原点加过来的。
        """
        m=len(obstacleGrid)
        n=len(obstacleGrid[0])
        dp = [[0 for i in range(n)] for j in range(m)]
        for i in range(m):
            for j in range(n):
                if not obstacleGrid[i][j]:
                    if i == j == 0:
                        dp[i][j] = 1
                    else:
                        a=dp[i-1][j] if i!=0 else 0
                        b=dp[i][j-1] if j!=0 else 0
                        dp[i][j] = a+b
        return dp[m-1][n-1]

        pass
if __name__ == '__main__':
    a=[[0,0,0],[0,1,0],[0,0,0]]
    a=[[0,0],[0,1]]
    a=[[0,1],[0,0]]
    a=[[1]]
    a=[[1,0]]
    a=[[0,1]]
    a=[[0, 0], [1, 1], [0, 0]]
    print(Solution().uniquePathsWithObstacles(a))