//
// Created by Wangxin.Colin on 2021/10/27.
//

#include <iostream>

#include "src/profile.h"

#include "src/Container_With_Most_Water.h"
#include "src/Remove_Duplicates_from_Sorted_Array.h"
#include "src/Three_Sum.h"


int main() {
  Profile profile;
  profile.add_function("ContainerWithMostWater", ContainerWithMostWater::test);
  profile.add_function("RemoveDuplicatesfromSortedArray", RemoveDuplicatesfromSortedArray::test);
  profile.add_function("ThreeSum", ThreeSum::test);
  profile.run_all();


  std::cout << "All tests passed" << std::endl;
  return 0;
}

