class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #Let's go with the hashmap approach
        string_map = {}

        #Instantiate the max length
        max_length = 0

        #Now instantiate the pointers
        left = 0
        right = 0

        #Get the length of the string
        str_len = len(s)

        #Now we create the loop
        while right < str_len:
            if s[right] in string_map:
                #Then set the left pointer to be either the left pointer or the index of s[right] + 1
                #This allows us to "skip" to a new substring if there are unrepeated characters between the two repeating characters
                left = max(string_map.get(s[right]) + 1, left)
            
            #Now we want to input the current character s[right] into the substring with the corresponding index
            string_map[s[right]] = right

            #Now we see if the current max_length is larger than the current substring we are dealing with
            max_length = max(max_length, right - left + 1)

            #And we increment right
            right += 1
        
        return max_length


solution = Solution()
s1 = "abcabcbb"
s2 = "bbbbb"
s3 = "pwwkew"
s4 = "aab"
s5 = "dvdf"

print(solution.lengthOfLongestSubstring(s1))
print(solution.lengthOfLongestSubstring(s2))
print(solution.lengthOfLongestSubstring(s3))
print(solution.lengthOfLongestSubstring(s4))
print(solution.lengthOfLongestSubstring(s5))



# #We want to use two pointers, one to indicate the start of the substring and one to indicate the end
#         point_1 = 0
#         point_2 = 0

#         #Now we create a variable to store the max length
#         max_length = 0

#         #We will loop through a string
#         for i in range(len(s)):
#             #Set a boolean to keep track of repeats
#             repeat = False

#             #For each iteration through the string, we will loop over the current substring we have
#             for j in range(point_1, point_2):
#                 #If the new character is equal to any of the substring characters, we must now take the max length of the current string 
#                 #But on the condition that it is greater than the current max_length
#                 if s[i] == s[j]:
#                     #Set repeat to true
#                     repeat = True

#                     print(max_length)
#                     if max_length < point_2 - point_1:
#                         max_length = point_2 - point_1 + 1
#                     print(max_length)
                    
#             #If we have a repeat, then we need to increase the pointer index of pointer_1 and decrease the count of 1 to then loop over the new substring
#             if repeat == True:
#                 #print(repeat)
#                 point_1 += 1
#                 #point_2 += 1
#                 i -= 1
#                 print(point_1, point_2)
#             else:
#                 point_2 += 1

#         #Now what do I do when I have looped through the whole string? Check if my current substring is longer than the max
#         if point_2 - point_1 + 1 >= max_length:
#             return point_2 - point_1 + 1
#         else:
#             return max_length