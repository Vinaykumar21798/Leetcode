from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        temp = len(nums) // 2
        dici = {}
        for i in nums:
            if i not in dici:
                dici[i] = 1
            else:
                dici[i] += 1

        for i in dici:
            if dici[i] > temp:
                return i
nums = list(map(int,input().split()))
obj = Solution()
print(obj.majorityElement(nums))
