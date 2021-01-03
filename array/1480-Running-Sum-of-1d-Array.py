'''
Problem Discription:
Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
Return the running sum of nums.

Example:
Input: nums = [1,2,3,4]
Output: [1,3,6,10]
'''

## self solution
### 利用切片的思想
## Runtime: 15.76%; Memory Usage: 11.26%
def runningSum(self, nums: List[int]) -> List[int]:
    result = []
    for i in range(len(nums)):
        result.append(sum(nums[:i+1]))
    return result

## opimal solution
### 考虑修改已有数组为己用
## Runtime: 23.11%; Memory Usage: 99.85%
def runningSum(self, nums: List[int]) -> List[int]:
    i = 1
    while i<len(nums):
        nums[i]+=nums[i-1]
        i+=1
    return nums