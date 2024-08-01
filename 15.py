from typing import List

#Sorting is nlogn
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #Sort the list
        nums.sort()

        #Create a seen list
        seen = []

        #Let us have two pointers and use a for loop to run through the list
        for i, num in enumerate(nums):
            if i > 0 and num == nums[i-1]:
                continue
            else:
                head = i+1
                tail = len(nums) - 1

                while head < tail:
                    sum = num + nums[head] + nums[tail]
                    if sum == 0:
                        seen.append([num, nums[head], nums[tail]])
                        head += 1

                        while nums[head] == nums[head - 1] and head < tail:
                            head += 1
                    elif sum < 0:
                        head += 1
                    else:
                        tail -= 1
                    
        return seen

test_1 = [-1,0,1,2,-1,-4]
test_2 = [0,1,1]
test_3 = [0,0,0]

solution = Solution()

print(solution.threeSum(test_1))
print(solution.threeSum(test_2))
print(solution.threeSum(test_3))