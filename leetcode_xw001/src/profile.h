//
// Created by Wangxin.Colin on 2021/11/9.
//

#ifndef BARBECUE_LEETCODE_XW001_SRC_PROFILE_H_
#define BARBECUE_LEETCODE_XW001_SRC_PROFILE_H_

#include <functional>
#include <chrono>
#include <map>
#include <iostream>

class Profile {
 public:
  Profile() = default;

  void add_function(std::string name, std::function<void()> function) {
    function_.emplace(name, function);
  }

  void run_all() {
    for (auto& item : function_) {
      run(item.first, item.second);
    }
  }

 private:
  void run(const std::string& name, const std::function<void()>& function) {
    auto start = std::chrono::high_resolution_clock::now();
    function();
    auto end = std::chrono::high_resolution_clock::now();
    auto els = std::chrono::duration_cast<std::chrono::milliseconds>(end - start).count();
    std::cerr << "function " << name << " cost " << els << " ms" << std::endl;
  }

 private:
  std::map<std::string, std::function<void()>> function_;
};

#endif //BARBECUE_LEETCODE_XW001_SRC_PROFILE_H_
