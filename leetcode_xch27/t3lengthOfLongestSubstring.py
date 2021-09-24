'''
3. 无重复字符的最长子串
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

示例 1:

输入: "abcabcbb"
输出: 3 
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
示例 2:

输入: "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
示例 3:

输入: "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
'''
class Solution1(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic=dict()
        max_length=0
        used_start=-1
        for i,c in enumerate(s):
            if c in dic and dic[c]> used_start:
                used_start=dic[c]
                dic[c]=i
            else:
                max_length=max(max_length,i-used_start)
                dic[c]=i
        return max_length
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        mydict={}
        pstart=-1
        maxlen=0
        for i,c in enumerate(s):
            # if c in mydict :
            if c in mydict and mydict[c]>pstart:
                pstart=mydict[c]
                mydict[c]=i
            else:
                mydict[c]=i
                maxlen=max(maxlen,i-pstart)
        return maxlen
class Solution2:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:return 0
        left = 0
        lookup = set()
        n = len(s)
        max_len = 0
        cur_len = 0
        for i in range(n):
            cur_len += 1
            while s[i] in lookup:
                lookup.remove(s[left])
                left += 1
                cur_len -= 1
            if cur_len > max_len:
                max_len = cur_len
            lookup.add(s[i])
        return max_len
class Solution22:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        left=0
        lookup=set()
        n=len(s)
        maxlen=0
        curlen=0
        for i in range(n):
            curlen+=1
            while s[i] in lookup:
                lookup.remove(s[left])
                left+=1
                curlen-=1
            maxlen=max(maxlen,curlen)
            lookup.add(s[i])
        return maxlen
class Solution1224(object):
    def lengthOfLongestSubstring(self, s):
        maxlen=0
        curlen=0
        left=0
        n=len(s)
        myset=set()
        for i in range(n):
            curlen+=1
            while s[i] in myset:
                myset.remove(s[left])
                curlen-=1
                left+=1
            maxlen=max(curlen,maxlen)
            myset.add(s[i])
        return maxlen

class Solution1225(object):
    def lengthOfLongestSubstring(self, s):
        curlen=0
        maxlen=0
        left=0
        myset=set()
        n=len(s)
        for i in range(n):
            curlen+=1
            while s[i] in myset:
                myset.remove(s[left])
                curlen-=1
                left+=1
            maxlen=max(curlen,maxlen)
            myset.add(s[i])
        return maxlen
class Solution1226(object):
    def lengthOfLongestSubstring(self,s):
        curlen=0
        maxlen=0
        n=len(s)
        left=0
        myset=set()
        for i in range(n):
            curlen+=1
            while s[i] in myset:
                myset.remove(s[left])
                curlen-=1
                left+=1
            maxlen=max(maxlen,curlen)
            myset.add(s[i])
        return maxlen

class Solution1228(object):
    def lengthOfLongestSubstring(self,s):
        n=len(s)
        curlen=0
        maxlen=0
        myset=set()
        left=0
        for i in range(n):
            curlen+=1
            while s[i] in myset:
                myset.remove(s[left])
                left+=1
                curlen-=1
            maxlen=max(curlen,maxlen)
            myset.add(s[i])
        return maxlen
if __name__ == '__main__':
    s="pwwkew"
    s="bbbb"
    #s="abcabcbb"
    #s=""
    #s="au"
    #print(Solution().lengthOfLongestSubstring(s))
    # 3 1 3 0 2 5
    for s in ["pwwkew","bbbb","abcabcbb","","au","tmmzuxt"]:
        print(Solution1228().lengthOfLongestSubstring(s))