# 假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
#
# 每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？
#
# 注意：给定 n 是一个正整数。
#
# 示例 1：
#
# 输入： 2
# 输出： 2
# 解释： 有两种方法可以爬到楼顶。
# 1.  1 阶 + 1 阶
# 2.  2 阶
# 示例 2：
#
# 输入： 3
# 输出： 3
# 解释： 有三种方法可以爬到楼顶。
# 1.  1 阶 + 1 阶 + 1 阶
# 2.  1 阶 + 2 阶
# 3.  2 阶 + 1 阶

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp=[ 0 for i in range(n+1)]
        if n==1:
            return 1
        dp[1]=1
        dp[2]=2
        for i in range(3,n+1):
            dp[i]=dp[i-1]+dp[i-2]
        return dp[n]
class Solution1228(object):
    def climbStairs(self, n):
        if n==1 or n==2:
            return n
        a=[ 0 for i in range(n+1)]
        a[1]=1
        a[2]=2
        for i in range(3,n+1):
            a[i]=a[i-1]+a[i-2]
        return a[n]
if __name__ == '__main__':
    print(Solution1228().climbStairs(1))
    print(Solution1228().climbStairs(2))
    print(Solution1228().climbStairs(3))
    print(Solution1228().climbStairs(4))
