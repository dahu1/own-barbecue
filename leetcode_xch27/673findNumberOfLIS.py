# 给定一个未排序的整数数组，找到最长递增子序列的个数。
#
# 示例 1:
#
# 输入: [1,3,5,4,7]
# 输出: 2
# 解释: 有两个最长递增子序列，分别是 [1, 3, 4, 7] 和[1, 3, 5, 7]。
# 示例 2:
#
# 输入: [2,2,2,2,2]
# 输出: 5
# 解释: 最长递增子序列的长度是1，并且存在5个子序列的长度为1，因此输出5。
# 注意: 给定的数组长度不超过 2000 并且结果一定是32位有符号整数。

class Solution(object):
    def findNumberOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        lens=[1]*n
        cnts=[1]*n
        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    if lens[i] < lens[j]+1:
                        lens[i] =lens[j]+1
                        cnts[i]=cnts[j]
                    elif lens[i]==lens[j]+1:
                        cnts[i]+=cnts[j]

        print(lens)
        print(cnts)
        maxnum=max(lens)
        res=0
        for i in range(n):
            if lens[i]==maxnum:
                res+=cnts[i]
        return res

if __name__ == '__main__':
    nums=[1,3,5,4,7]
    # nums=[2,2,2,2,2]
    print(Solution().findNumberOfLIS(nums))