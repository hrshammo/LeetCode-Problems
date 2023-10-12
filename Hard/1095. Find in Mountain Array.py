# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        # Step 1: Find the peak
        left, right = 0, mountain_arr.length() - 1

        while left < right:
            mid = left + (right - left) // 2
            if mountain_arr.get(mid) < mountain_arr.get(mid + 1):
                left = mid + 1
            else:
                right = mid

        peak_index = left

        # Step 2: Binary search in the increasing part
        left, right = 0, peak_index

        while left <= right:
            mid = left + (right - left) // 2
            mid_value = mountain_arr.get(mid)
            if mid_value == target:
                return mid
            elif mid_value < target:
                left = mid + 1
            else:
                right = mid - 1

        # Step 3: Binary search in the decreasing part
        left, right = peak_index, mountain_arr.length() - 1

        while left <= right:
            mid = left + (right - left) // 2
            mid_value = mountain_arr.get(mid)
            if mid_value == target:
                return mid
            elif mid_value > target:
                left = mid + 1
            else:
                right = mid - 1

        return -1
