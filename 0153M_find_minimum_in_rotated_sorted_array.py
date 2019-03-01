class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        mid = 0

        while left < right:
            mid = (left + right) // 2

            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                # nums[mid] < nums[right], mid can be pivot, so include
                right = mid
        # we return left, not mid! left takes advantage of mid being the floor
        return nums[left]
