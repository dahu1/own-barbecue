# 原理
# 快速排序使用分治法（Divide and conquer）策略来把一个序列（list）分为两个子序列（sub-lists）。
#
# 步骤
#
# 从数列中挑出一个元素，称为” 基准”（pivot），
# 重新排序数列，所有元素比基准值小的摆放在基准前面，所有元素比基准值大的摆在基准的后面（相同的数可以到任一边）。在这个分区结束之后，该基准就处于数列的中间位置。这个称为分区（# partition）操作。
# 递归地（recursive）把小于基准值元素的子数列和大于基准值元素的子数列排序。
def quick_sort(list):
    less = []
    pivotList = []
    more = []
    # 递归出口
    if len(list) <= 1:
        return list
    else:
        # 将第一个值做为基准
        pivot = list[0]
        for i in list:
            # 将比基准小的值放到less数列
            if i < pivot:
                less.append(i)
            # 将比基准打的值放到more数列
            else :
                more.append(i)
            # 将和基准相同的值保存在基准数列
        # 对less数列和more数列继续进行排序
        less = quick_sort(less)
        more = quick_sort(more)
        return less + [pivot] + more
def qsort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x < pivot]
        greater = [x for x in arr[1:] if x >= pivot]
        return qsort(less) + [pivot] + qsort(greater)

def qsort1(nums):
    if len(nums)<=1:
        return nums
    else:
        num=nums[0]
        less=[x for x in nums[1:] if x < num]
        more=[x for x in nums[1:] if x>= num]
        return qsort1(less) + [num] + qsort1(more)
def qsort2(nums):
    n=len(nums)
    if n<=1:
        return nums
    nums0=nums[0]
    left=[ x for x in nums[1:] if x<nums0]
    right=[x for x in nums[1:] if x>=nums0]
    return qsort2(left) + [nums0] + qsort2(right)
if __name__ == '__main__':
    nums=[1,3,5,7,9,2,4,6,8,10]
    print(qsort(nums))
    print(qsort2(nums))
