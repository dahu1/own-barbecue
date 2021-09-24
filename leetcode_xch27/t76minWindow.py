# 76.
# 最小覆盖子串
# 给你一个字符串
# s 、一个字符串
# t 。返回
# s
# 中涵盖
# t
# 所有字符的最小子串。如果
# s
# 中不存在涵盖
# t
# 所有字符的子串，则返回空字符串
# "" 。
#
# 注意：如果
# s
# 中存在这样的子串，我们保证它是唯一的答案。
#
#
#
# 示例
# 1：
#
# 输入：s = "ADOBECODEBANC", t = "ABC"
# 输出："BANC"
# 示例
# 2：
#
# 输入：s = "a", t = "a"
# 输出："a"
#
# 提示：
#
# 1 <= s.length, t.length <= 105
# s
# 和
# t
# 由英文字母组成
#
# 进阶：你能设计一个在
# o(n)
# 时间内解决此问题的算法吗？

# 1.要全覆盖t ，2.子串长度尽可能小

# l 和 r 都初始化为 0
# r 指针移动一步
# 判断窗口内的连续元素是否满足题目限定的条件
# 4.1 如果满足，再判断是否需要更新最优解，如果需要则更新最优解。并尝试通过移动 l 指针缩小窗口大小。循环执行 4.1
# 4.2 如果不满足，则继续。

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        left=0
        n=len(s)
        tdict={i:0 for i in t}
        have={}
        minlen=n
        curlen=0
        print(tdict)
        print(len(tdict))
        def check_contain(tdict,have):
            if(len(have)<len(tdict)):
                return False
            s=1
            for x in have.values():
                s*=x
            if s>=1:
                return True
            else:
                return False
        for i in range(n):
            curlen+=1
            if s[i] in tdict:
                have[s[i]]+=1
            if check_contain(tdict,have):
                minlen=min(minlen,curlen)
            while check_contain(tdict,have):

        pass
if __name__ == '__main__':
    s='a'
    t='a'
    s = "ADOBECODEBANC"
    t = "ABC"
    print(Solution().minWindow(s,t))