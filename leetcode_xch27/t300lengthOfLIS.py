# 给你一个整数数组 nums ，找到其中最长严格递增子序列的长度。
#
# 子序列是由数组派生而来的序列，删除（或不删除）数组中的元素而不改变其余元素的顺序。例如，[3,6,2,7] 是数组 [0,3,1,6,2,2,7] 的子序列。
#
#  
# 示例 1：
#
# 输入：nums = [10,9,2,5,3,7,101,18]
# 输出：4
# 解释：最长递增子序列是 [2,3,7,101]，因此长度为 4 。
# 示例 2：
#
# 输入：nums = [0,1,0,3,2,3]
# 输出：4
# 示例 3：
#
# 输入：nums = [7,7,7,7,7,7,7]
# 输出：1
#  
#
# 提示：
#
# 1 <= nums.length <= 2500
# -104 <= nums[i] <= 104
#  
#
# 进阶：
#
# 你可以设计时间复杂度为 O(n2) 的解决方案吗？
# 你能将算法的时间复杂度降低到 O(n log(n)) 吗？

class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        dp=[]      #dp[i] ,存放的是，在前 i 个元素，以第 i 个数字结尾的最长上升子序列的长度
        for i in range(len(nums)):  #外面大循环，每个值遍历一下
            dp.append(1)
            for j in range(i):     #每次遍历的时候，计算  dp[i]
                if nums[i]> nums[j]:
                    dp[i]=max(dp[i],dp[j]+1)
        print(dp)
        return max(dp)

class Solution1226(object):
    def lengthOfLIS(self, nums):
        if not nums:
            return 0
        n=len(nums)
        dp=[]
        for i in range(n):
            dp.append(1)
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i]=max(dp[i],dp[j]+1)
        return max(dp)

class Solution1226_tijie(object):
    def lengthOfLIS(self, nums):
        tails, res = [0] * len(nums), 0   # tails 是个严格递增的数列，维护一个列表 tails其中每个元素 tails[k] 的值代表 长度为 k+1 的子序列尾部元素的值。
        # res 为 有效 tails的长度
        for num in nums:
            i, j = 0, res    # i 为 tails的起始点  ，j为 tails的结束点
            while i < j:
                m = (i + j) // 2
                if tails[m] < num:
                    i = m + 1  # 如果要求非严格递增，将此行 '<' 改为 '<=' 即可。
                else:
                    j = m
            tails[i] = num   #更新 tails 的元素，换成更新的
            if j == res: res += 1   #j==res，说明j没变小，说明num很大，在tails的数组最后了,整体有效tails的长度要+1
        return res
# 参数最好换成st 和 en ，表示在res里的开头和结尾，然后二分法夹逼 tails数组。
# 讲解： https://leetcode-cn.com/problems/longest-increasing-subsequence/solution/zui-chang-shang-sheng-zi-xu-lie-dong-tai-gui-hua-2/
# NOTE: 这个题，一开始的思路是，先一个大循环过一遍每个数，再过每个数的时候，还需要循环0到当前的数，好确定递增的数量。所以要俩循环。
# 优化点在于，大循环过一遍数很明显必须要有的，计算当前数递增的数量的时候，就可以用 二分法来做。建一个单调增的数组，每次往里放依次最大的数，这样新数比较的时候，就可以用二分法在有序数组里比较了。
class Solution1228(object):
    def lengthOfLIS(self, nums):
        n=len(nums)
        dp=[ 1 for _ in range(n)]
        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j] :
                    dp[i]=max(dp[i],dp[j]+1)
        return max(dp)
    def lengthOfLIS_dp(self, nums):
        n=len(nums)
        dp=[ 0 for _ in range(n)]
        res=0
        for i in range(n):
            st,en=0,res
            while st < en:
                m=(st+en)//2
                if nums[i]> dp[m]:
                    st=m+1
                else:
                    en=m
            dp[st]=nums[i]
            if res==en:
                res+=1
        return res
    def sss(self,nums):
        n=len(nums)
        dp=[0] * n #存单调增的数组
        res=0
        for i in range(n):
            st,en=0,res
            while st< en:
                m=(st+en)//2
                if nums[i]>dp[m]:
                    st=m+1
                else:
                    en=m
            dp[st]=nums[i]
            if res==en:
                res+=1
        return  res


if __name__ == '__main__':
    nums = [10, 9, 2, 5, 3, 7, 101, 18]  # 4
    nums = [0,1,0,3,2,3]   # 4
    nums = [1,3,6,7,9,4,10,5,6]   #6
    nums= [4,5,6,9]
    print(nums)
    print(Solution1228().lengthOfLIS_dp(nums))
    print(Solution1228().sss(nums))
