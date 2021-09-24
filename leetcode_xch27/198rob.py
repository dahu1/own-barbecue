'''
你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。

给定一个代表每个房屋存放金额的非负整数数组，计算你 不触动警报装置的情况下 ，一夜之内能够偷窃到的最高金额。

 

示例 1：

输入：[1,2,3,1]
输出：4
解释：偷窃 1 号房屋 (金额 = 1) ，然后偷窃 3 号房屋 (金额 = 3)。
     偷窃到的最高金额 = 1 + 3 = 4 。
示例 2：

输入：[2,7,9,3,1]
输出：12
解释：偷窃 1 号房屋 (金额 = 2), 偷窃 3 号房屋 (金额 = 9)，接着偷窃 5 号房屋 (金额 = 1)。
     偷窃到的最高金额 = 2 + 9 + 1 = 12 。
 

提示：

0 <= nums.length <= 100
0 <= nums[i] <= 400
通过次数 266,897 提交次数 551,763

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/house-robber
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        dp=[0] * n
        if not nums:
            return 0
        if n<=2:
            return max(nums)
        dp[0]=nums[0]
        dp[1]=max(nums[0],nums[1])
        for i in range(2,n):
            dp[i]=max(dp[i-1],dp[i-2]+nums[i])
        return dp[n-1]
    def rob2(self,nums): #房屋围城一圈
        if not nums:
            return 0
        n=len(nums)
        if n<=3:
            return max(nums)
        dp=[0]* n
        dp[0]=nums[0]
        dp[1]=max(nums[0],nums[1])
        for i in range(2,n):
            dp[i]=max(dp[i-2]+nums[i],dp[i-1])
        ds=[0]*n
        ds[1]=nums[1]
        ds[2]=max(nums[1],nums[2])
        for i in range(3,n):
            ds[i]=max(ds[i-2]+nums[i],ds[i-1])
        return max(dp[n-2],ds[n-1])
    def rob2_x(self,nums):
        n = len(nums)
        if not nums:
            return 0
        if n <= 2:
            return max(nums)
        nums.append(0)
        dp = [0] * (n+1)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, n+1):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
        return dp[n - 1]

if __name__ == '__main__':
    a=[1,2,3,1]
    a=[2,7,9,3,1]
    a=[2,1,1,2]
    a=[1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
    print(Solution().rob2_x(a))