# 给你两个单词 word1 和 word2，请你计算出将 word1 转换成 word2 所使用的最少操作数 。
#
# 你可以对一个单词进行如下三种操作：
#
# 插入一个字符
# 删除一个字符
# 替换一个字符
#  
#
# 示例 1：
#
# 输入：word1 = "horse", word2 = "ros"
# 输出：3
# 解释：
# horse -> rorse (将 'h' 替换为 'r')
# rorse -> rose (删除 'r')
# rose -> ros (删除 'e')
# 示例 2：
#
# 输入：word1 = "intention", word2 = "execution"
# 输出：5
# 解释：
# intention -> inention (删除 't')
# inention -> enention (将 'i' 替换为 'e')
# enention -> exention (将 'n' 替换为 'x')
# exention -> exection (将 'n' 替换为 'c')
# exection -> execution (插入 'u')
#  
#
# 提示：
#
# 0 <= word1.length, word2.length <= 500
# word1 和 word2 由小写英文字母组成

class Solution(object):
    def minDistance(self,s1, s2):
        def dp(i, j):
            # base case
            if i == -1: return j + 1
            if j == -1: return i + 1

            if s1[i] == s2[j]:
                return dp(i - 1, j - 1)  # 啥都不做
            else:
                return min(
                    dp(i, j - 1) + 1,  # 插入
                    dp(i - 1, j) + 1,  # 删除
                    dp(i - 1, j - 1) + 1  # 替换
                )
        # i，j 初始化指向最后一个索引
        return dp(len(s1) - 1, len(s2) - 1)

class Solution1224(object):
    def minDistance(self,s1, s2):
        def dp(i,j):
            if i==-1:
                return j+1
            if j==-1:
                return i+1
            if s1[i]==s2[j]:
                return dp(i-1,j-1)
            else :
                return min(
                    dp(i-1,j),
                    dp(i,j-1),
                    dp(i-1,j-1)
                ) + 1
        return dp(len(s1)-1,len(s2)-1)
class Solution1225ans(object):
    def minDistance(self,word1, word2):
        # 递推填表
        m, n = len(word1), len(word2)
        dp = [[0 for j in range(n + 1)] for i in range(m + 1)]
        for i in range(m + 1):
            for j in range(n + 1):   #遍历整张表，然后填上去
                if i == 0 or j == 0:
                    dp[i][j] = i + j
                elif word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
        return dp[-1][-1]
class Solution1225(object):
    def minDistance(self,word1, word2):
        m,n=len(word1),len(word2)
        dp=[[0 for i in range(n+1) ] for j in range(m+1)]
        #print(dp)
        for i in range(m+1):
            for j in range(n+1):
                if i*j==0:
                    dp[i][j]=i+j
                elif word1[i-1] == word2[j-1]:
                    dp[i][j]=dp[i-1][j-1]
                else:
                    dp[i][j]=1+min(dp[i-1][j],dp[i-1][j-1],dp[i][j-1])
        return dp[m][n]

class Solution1225_x(object):
    # 记忆化递归 ,也是 填表，但是 只有在调用的时候才填，其他不用的不填表
    def minDistance(self,word1, word2):
        m,n=len(word1),len(word2)
        dp=[ [-1 for i in range(n+1)] for i in range(m+1)] #构建表，全-1
        def dp_process(i,j):
            if dp[i][j]>=0:     #先判断下，不是-1，说明更新过了，直接输出
                return dp[i][j]
            if i*j==0:
                dp[i][j]=i+j
            elif word1[i-1]==word2[j-1]:
                dp[i][j]=dp_process(i-1,j-1)   #分情况讨论，不停的更新dp表
            else:
                dp[i][j]= 1+min(
                    dp_process(i-1,j),
                    dp_process(i,j-1),
                    dp_process(i-1,j-1)
                )
            return dp[i][j]
        return dp_process(m,n)
class Solution1226(object):
    def minDistance(self,word1, word2):
        m,n=len(word1),len(word2)
        dp=[ [-1 for i in range(n+1)] for i in range(m+1) ]
        # print(dp)
        def dp_process(i,j):
            if dp[i][j]!=-1:
                return dp[i][j]
            if i*j==0:
                dp[i][j]=i+j
            elif word1[i-1]==word2[j-1]:
                dp[i][j]=dp_process(i-1,j-1)
            else:
                dp[i][j]=min(
                    dp_process(i-1,j),
                    dp_process(i,j-1),
                    dp_process(i-1,j-1)
                ) + 1
            return dp[i][j]
        return dp_process(m,n)


if __name__ == '__main__':
    a="horse"
    b="ros"
    a="intention"
    b="execution"
    print(Solution1226().minDistance(a,b))