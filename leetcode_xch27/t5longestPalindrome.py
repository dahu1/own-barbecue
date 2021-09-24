# 输入: "babad"
# 输出: "bab"
# 注意: "aba" 也是一个有效答案。
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n=len(s)
        t="#"
        for i in range(n):
            t+=s[i]+"#"
        maxlen=0
        tlen=len(t)
        st=0
        for i in range(tlen):
            curlen=self.__center_len(t,i)
            if curlen> maxlen:
                maxlen=curlen
                st=(i-maxlen)//2
        return s[st:st+maxlen]
    def __center_len(self,s,center):
        i=center-1
        j=center+1
        n=len(s)
        res=0
        while i>=0 and j < n and s[i]==s[j]:
            i=i-1
            j=j+1
            res=res+1
        return res
class Solution1225(object):
    def longestPalindrome(self, s):

        pass
if __name__ == '__main__':
    s='babad'
    s='cbbd'
    print(Solution1225().longestPalindrome(s))