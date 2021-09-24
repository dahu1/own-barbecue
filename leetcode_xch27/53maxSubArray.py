# 给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
#
# 示例:
#
# 输入: [-2,1,-3,4,-1,2,1,-5,4]
# 输出: 6
# 解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
# 进阶:
#
# 如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。
#
class Solution_tijie(object):
    # dp[i]：表示以 nums[i] 结尾的连续子数组的最大和。dp 保存的总是n-1 规模的解，可分解的
    def maxSubArray(self, nums):
        size = len(nums)
        if size == 0:
            return 0
        dp = [0 for _ in range(size)]

        dp[0] = nums[0]
        for i in range(1, size):
            dp[i] = max(dp[i - 1] + nums[i], nums[i])
        return max(dp)

class Solution1226(object):
    def maxSubArray(self, nums):
        n=len(nums)
        if n==0:
            return 0
        dp= [ 0 for _ in range(n)]
        dp[0]=nums[0]
        for i in range(1,n):
            dp[i]=max(dp[i-1]+nums[i],nums[i])
        return max(dp)



if __name__ == '__main__':
    # num=[-2,1,-3,4,-1,2,1,-5,4]
    num=[-1,-1]
    print(num)
    print(Solution1226().maxSubArray(num))
