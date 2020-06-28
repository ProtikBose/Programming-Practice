# wihout extra space and in O(n) runtime
# https://www.geeksforgeeks.org/find-duplicates-in-on-time-and-constant-extra-space/

'''
Given an array of integers, 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.

Find all the elements that appear twice in this array.

Could you do it without extra space and in O(n) runtime?

'''

class Solution(object):

    def findDuplicates(self, nums):

        result =[]
        for i in nums :
            n = abs(i)
            nums[n-1] = - nums[n-1]
            if nums[n-1] > 0 :
                result.append(n)
        return result


sol = Solution()
print(sol.findDuplicates([1, 2, 3, 4 ,3]))