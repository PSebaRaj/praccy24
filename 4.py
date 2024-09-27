from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        #Why can't we just create an array ourselves and then loop through both nums1 and nums2 simultaneously
        #Since both arrays are sorted, we will consistently compare the values
        merge_array = []

        #Let's get the lengths of both arrays
        len_1 = len(nums1)
        len_2 = len(nums2)

        #Get the full length of the merged array
        full_length = len_1 + len_2

        #Now let's create two pointers
        p1 = 0
        p2 = 0

        while p1 < len_1 or p2 < len_2:
            #Three different scenarios
            if p1 < len_1 and p2 < len_2:
                #If the element from the first list is larger than the element from the second, add the element from the second
                if nums1[p1] >= nums2[p2]:
                    merge_array.append(nums2[p2])
                    #Now increment p2
                    p2 += 1
                else:
                    #The element from the first list is smaller so we add the element to the merge_array
                    merge_array.append(nums1[p1])
                    p1 += 1
            
            #Then we have reached the end of the second list
            elif p1 < len_1 and p2 == len_2:
                merge_array.append(nums1[p1])
                p1 += 1

            #Then we have reached the end of the first list
            elif p1 == len_1 and p2 < len_2:
                merge_array.append(nums2[p2])
                p2 += 1
        
        #Nice so it seems like our merging works correctly
        #return(merge_array)

        #Then at the end, once we have the merged array, we can take the median by taking the length of the array
        #If the length is even, then we take the two middle elements and average them.
        #Handle the edge case of empty array
        if full_length != 0:
            if full_length % 2 == 0:
                #Then the length is even so we take the average
                p1 = int((full_length / 2) - 1)
                p2 = p1 + 1
                return((merge_array[p1] + merge_array[p2]) / 2)

            else:
            #Else if the length is odd, then we divide by 2, and subtract by .5 to get the correct index
                median_index = full_length // 2
                return(merge_array[median_index])



solution = Solution()

nums1 = [1,3]
nums2 = [2]
print(solution.findMedianSortedArrays(nums1, nums2))

nums3 = [1, 2]
nums4 = [3,4]
print(solution.findMedianSortedArrays(nums3, nums4))

nums5 = []
nums6 = []
print(solution.findMedianSortedArrays(nums5, nums6))

# #Determine which length is longer
#         if len_1 > len_2:
#             len_long = len_1
#             #Keep as nums1 and nums2
#         else:
#             #Length of list 2 is longer
#             len_long = len_2

#             #Switch nums1 and nums2. Probably really bad practice 
#             nums3 = nums1
#             nums1 = nums2
#             nums2 = nums3
            
#         #An indexing of the shorter length list
#         short_index = 0

#         #Now we know that nums1 is the longer list
#         for i in range(len_long):
#             #First check if the length of the shorter list is exceeded
#             if short_index < len(nums2):
#                 print(short_index)
#                 #Then we can run our algorithm
#                 if nums1[i] >= nums2[short_index]:
#                     #If the nums1 value is larger than the nums2 value, we will append nums2 to the merge_array and increment the short_index
#                     #We must also deincrement the i by 1 since we are not adding it
#                     merge_array.append(nums2[short_index])
#                     short_index += 1 
#                 else:
#                     #We must keep short_index the same and add nums1
#                     merge_array.append(nums1[i])
#             else:
#                 print(nums1[i])
#                 #Then we can just keep adding nums1 values since nums2 has been exceeded
#                 merge_array.append(nums1[i])


#         return merge_array