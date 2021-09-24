'''
给定一个整数 n，求以 1 ... n 为节点组成的二叉搜索树有多少种？

示例:

输入: 3
输出: 5
解释:
给定 n = 3, 一共有 5 种不同结构的二叉搜索树:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
通过次数 113,531 提交次数 163,514

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/unique-binary-search-trees
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

 https://leetcode-cn.com/problems/unique-binary-search-trees/solution/bu-tong-de-er-cha-sou-suo-shu-by-leetcode-solution/
'''
class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        G=[0] * (n+1)
        G[0],G[1]=1,1
        for m in range(2,n+1):
            for i in range(1,m+1):
                G[m]+=G[i-1]*G[m-i]

        return G[n]

class Solution0331(object):
    def numTrees(self, n):
        G=[0 for i in range(n+1)]
        G[0],G[1]=1,1
        for m in range(2,n+1): #从小到大累计求G的
            for i in range(1,m+1):   #特定的G[m] 下
                G[m]+=G[i-1]*G[m-i]
        return G[n]

class Solution0401(object):
    def numTrees(self, n):
        G=[ 0 for i in range(n+1)]
        G[0],G[1]=1,1
        for m in range(2,n+1):
            for i in range(1,m+1):
                G[m]+=G[i-1]*G[m-i]
        return G[m]
if __name__ == '__main__':
    print(Solution().numTrees(3))
    print(Solution0331().numTrees(3))
    print(Solution0401().numTrees(3))
