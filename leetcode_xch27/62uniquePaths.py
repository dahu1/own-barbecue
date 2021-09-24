'''
一个机器人位于一个 m x n 网格的左上角 （起始点在下图中标记为 “Start” ）。

机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为 “Finish” ）。

问总共有多少条不同的路径？

 

示例 1：


输入：m = 3, n = 7
输出：28
示例 2：

输入：m = 3, n = 2
输出：3
解释：
从左上角开始，总共有 3 条路径可以到达右下角。
1. 向右 -> 向下 -> 向下
2. 向下 -> 向下 -> 向右
3. 向下 -> 向右 -> 向下
示例 3：

输入：m = 7, n = 3
输出：28
示例 4：

输入：m = 3, n = 3
输出：6
 

提示：

1 <= m, n <= 100
题目数据保证答案小于等于 2 * 109
通过次数 229,552 提交次数 355,096

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/unique-paths
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class Solution0401(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp=[ [0 for i in range(n)] for j in range(m)]
        for i in range(m):
            for j in range(n):
                if i*j==0:
                    dp[i][j]=1
                else:
                    dp[i][j]=dp[i-1][j]+dp[i][j-1]
        return dp[m-1][n-1]
    def uniquePaths_1(self, m, n):
        # 借鉴63的想法，原点才是1，其他的都从原点来
        dp=[[0] * n for i in range(m)]
        for i in range(m):
            for j in range(n):
                if i ==j==0:
                    dp[i][j]=1
                else:
                    a=dp[i-1][j] if i!=0 else 0
                    b=dp[i][j-1] if j!=0 else 0
                    dp[i][j]=a + b
        return dp[m-1][n-1]


if __name__ == '__main__':
    m,n=3,2
    print(Solution0401().uniquePaths_1(m,n))
    m, n = 3, 7
    print(Solution0401().uniquePaths_1(m, n))
