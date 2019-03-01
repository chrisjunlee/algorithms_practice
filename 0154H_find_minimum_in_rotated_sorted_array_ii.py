class Solution:
    def findMin(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1

        # min = pivot point. we search towards pivot side
        # insight: each iteration, we must cut from left or right
        # insight: mid biases towards low, so that in itself is a cut
        # insight: storing min in low, not mid; be careful when cutting low
        while low < high:
            mid = (low + high) // 2

            if nums[mid] == nums[high]:
                # cutting repeats from right
                high = high - 1
            elif nums[mid] > nums[high]:
                # go right
                # mid cannot be min, exclude
                low = mid + 1
            elif nums[low] >= nums[mid]:
                # left
                # mid can be min, include
                high = mid
            elif nums[low] < nums[mid] < nums[high]:
                # left
                # mid cannot be min, exclude
                high = mid - 1

        return nums[low]



