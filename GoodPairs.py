class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count = 0
        j=0
        for i in range(len(nums)):
            while j != len(nums)-1:
                j += 1
                #print(nums[i], nums[j])
                if i < j and nums[i] == nums[j]:
                    count += 1
            j = 0
        return count
