from typing import List


class Solution:

    def search(self, nums: List[int], target: int) -> bool:
        sort_nums = sorted(nums)
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if sort_nums[mid] == target:
                return True

            if sort_nums[left] < sort_nums[mid]:
                if sort_nums[left] == target:
                    return True
                elif sort_nums[left] < target < sort_nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if sort_nums[right] == target:
                    return right
                elif sort_nums[mid] < target < sort_nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return False