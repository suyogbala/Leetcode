# 1. Sum of two number
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for x in range(len(nums)-1):
            for y in range(x+1, len(nums)):
                if nums[x] + nums[y] == target:
                    return x, y

# 3. Longest Substring Without Repeating Characters
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        temp = 1
        chemp = 1
        for x in range(len(s)):
            temp = 1
            for y in range(x+1, len(s)):
                if s[y] not in s[x:y]:
                    temp += 1
                else:
                    break
            
            if temp > chemp:
                chemp = temp

        return chemp


# 4. Median of Two Sorted Arrays
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        array = nums1 + nums2
        array.sort()
        if (len(array) + 1) % 2 == 0:
            value = (len(array)+ 1) // 2
            return array[value - 1]

        else:
            value = (len(array) + 1) / 2
            org_value = value - 1
            first = int(org_value - 0.5)
            second = int(org_value + 0.5)
            median = (array[first] + array[second]) / 2
        return median

# 7. Reverse Integer
class Solution:
    def reverse(self, x: int) -> int:
        value = 0
        if x >= 0:
            num = 1
        else:
            num = -1
        x *= num

        while x > 0:
            value = value * 10 + x % 10
            x //= 10

        if -2**31 <= value <= 2**31 - 1:
            return value * num
        else:
            return 0

# 28. Find the Index of the First Occurrence in a String
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle not in haystack:
            return -1

        else:
            return haystack.index(needle)

# 215. Kth Largest Element in an Array
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        number = len(nums) - k 
        value = nums[number]

        return value

# 66. Plus One
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        temp = 0
        for x in digits:
            temp = temp * 10 + x

        temp += 1
        value = []
        while temp > 0:
            reminder = temp % 10
            temp = temp // 10
            value.append(reminder)

        return value[::-1]

# 69. Sqrt(x)
class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0

        if x <= 3:
            return 1

        for i in range(x):
            if i * i > x:
                return i - 1
                break
            





                
                