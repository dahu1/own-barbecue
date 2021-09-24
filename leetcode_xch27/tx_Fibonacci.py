# 题目描述
# 大家都知道斐波那契数列，现在要求输入一个整数 n，请你输出斐波那契数列的第 n 项（从 0 开始，第 0 项为 0，第 1 项是 1）。
# n\leq 39n≤39
#
# 示例 1
# 输入
# 复制
# 4
# 返回值
# 复制
# 3
class Solution:
    def Fibonacci(self, n):
        # write code here
        arr=[]
        arr=[0 for i in range(40)]
        arr[0]=0
        arr[1]=1
        if n >1 :
            for i in range(2,n+1):
                arr[i]=arr[i-1]+arr[i-2]
        return arr[n]

class Solution1228:
    def Fibonacci(self, n):
        if n==1 or n==0:
            return n
        a=[ 0 for _ in range(n+1)]
        a[0]=0
        a[1]=1
        for i in range(2,n+1):
            a[i]=a[i-1]+a[i-2]
        return a[n]
if __name__ == '__main__':
    for i in range(10):
        print("%d - %d \n"%(i,Solution1228().Fibonacci(i)))
