# 354. 俄罗斯套娃信封问题
# 给定一些标记了宽度和高度的信封，宽度和高度以整数对形式 (w, h) 出现。当另一个信封的宽度和高度都比这个信封大的时候，这个信封就可以放进另一个信封里，如同俄罗斯套娃一样。
#
# 请计算最多能有多少个信封能组成一组 “俄罗斯套娃” 信封（即可以把一个信封放到另一个信封里面）。
#
# 说明:
# 不允许旋转信封。
#
# 示例:
#
# 输入: envelopes = [[5,4],[6,4],[6,7],[2,3]]
# 输出: 3
# 解释: 最多信封的个数为 3, 组合为: [2,3] => [5,4] => [6,7]。

class Solution(object):
        def maxEnvelopes(self, envelopes) :
            if not envelopes:
                return 0
            n = len(envelopes)
            envelopes.sort(key=lambda x: (x[0], -x[1]))
            print(envelopes)
            dp = [1] * n
            res = 1
            for i in range(1, n):
                for j in range(i):
                    if envelopes[i][1] > envelopes[j][1]:
                        dp[i] = max(dp[i], dp[j] + 1)
                res = max(res, dp[i])
            return res


if __name__ == '__main__':
    nums=[[5,4],[6,4],[6,7],[2,3],[6,5]]
    print(Solution().maxEnvelopes(nums))