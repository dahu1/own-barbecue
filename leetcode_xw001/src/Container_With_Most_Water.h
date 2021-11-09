//
// Created by Wangxin.Colin on 2021/10/27.
//

#include <vector>
#include <iostream>

namespace ContainerWithMostWater {
  class Solution {
   public:
    int maxArea(const std::vector<int>& height) {
      int size = height.size();
      int max_front{0};
      int area{-1};
      for (int i = 0; i < size - 1; ++i) {
        if (height[i] < max_front) continue;
        max_front = height[i];
        int max_back{0};
        for (int j = size - 1; j > i; --j) {
          if (height[j] < max_back) continue;
          max_back = height[j];

          area = std::max(area, (j - i) * std::min(height[j], height[i]));
        }
      }
      return area;
    }
  };

  void test() {
    Solution so;
    assert(so.maxArea({1,8,6,2,5,4,8,3,7}) == 49);
    assert(so.maxArea({1, 1}) == 1);
    assert(so.maxArea({4,3,2,1,4}) == 16);
    assert(so.maxArea({1, 2, 1}) == 2);

    std::cout << __FILE_NAME__ << " tests passed\n";
}

}