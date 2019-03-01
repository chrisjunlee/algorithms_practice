class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1

        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (right + left)//2

            if nums[mid] == target:
                return mid

            if nums[left] <= nums[mid]:
                # left side ordered
                if nums[left] <= target < nums[mid]:
                    # go left
                    right = mid - 1
                else:
                    # go right
                    left = mid + 1
            else:
                # right side ordered
                if nums[mid] < target <= nums[right]:
                    # go right
                    left = mid + 1
                else:
                    # go left
                    right = mid - 1

        return -1

