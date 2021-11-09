//
// Created by Wangxin.Colin on 2021/10/28.
//

#ifndef BARBECUE_LEETCODE_XW001_REMOVE_DUPLICATES_FROM_SORTED_ARRAY_H_
#define BARBECUE_LEETCODE_XW001_REMOVE_DUPLICATES_FROM_SORTED_ARRAY_H_
#include <vector>
namespace RemoveDuplicatesfromSortedArray {
class Solution {
 public:
  int removeDuplicates(std::vector<int> nums) {
    int size = nums.size();
    if (size <= 1)
      return size;

    int cur = 1;
    int prev = nums[0];
    for (int fast = 1; fast < size; ++fast) {
      if (nums[fast] != prev) {
        prev = nums[cur] = nums[fast];
        ++cur;
      }
    }
    return cur;
  }
};

void test() {
  Solution so;
  assert(so.removeDuplicates({1,1,2}) == 2);
  assert(so.removeDuplicates({0,0,1,1,1,2,2,3,3,4}) == 5);

  std::cout << __FILE_NAME__ << " tests passed\n";

  }
}
#endif //BARBECUE_LEETCODE_XW001_REMOVE_DUPLICATES_FROM_SORTED_ARRAY_H_
