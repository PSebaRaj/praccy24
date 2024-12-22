from typing import List

class Solution:
    def longestPalindrome(self, s: str) -> str:
        #We want to return the longest palindromic substring in s
        #Two pointer method
        #First initialize the string to hold the palindrome and the length of the longest palindrome
        palindrome = ""
        palin_length = 0

        #Now we need to loop through all the indices of s
        for i in range(len(s)):
            #Define the pointers for the odd case
            l = i - 1
            r = i + 1

            #Define a candidate palindrome
            candidate_palindrome = s[i]
            candidate_length = 0

            #We have two instances. The first is if we have an odd palindrome and the second is if we have an even palindrome
            while l >= 0 and r < len(s) and s[l] == s[r]:
                #Then we have a valid addition to our palindrome and we get the new length
                candidate_palindrome = s[l] + candidate_palindrome + s[r]
                candidate_length = len(candidate_palindrome)

                #Update l and r
                l -= 1
                r += 1

            #Now we check to see if our candidate's length is shorter than our palindrome's length
            if candidate_length > palin_length:
                palindrome = candidate_palindrome
                palin_length = candidate_length
            

            #Now we define the pointers for the even case and the candidate palindrome and length
            l = i - 1
            r = i
            candidate_palindrome = ""
            candidate_length = 0

            while l >= 0 and r < len(s) and s[l] == s[r]:
                candidate_palindrome = s[l] + candidate_palindrome + s[r]
                candidate_length = len(candidate_palindrome)
                #Update our pointers
                l -= 1
                r += 1
            
            #Now we check to see if our candidate's length is shorter than our palindrome's length
            if candidate_length > palin_length:
                palindrome = candidate_palindrome
                palin_length = candidate_length

        #Deal with the edge case of only having one character and having no palindrome so we return the first character
        if len(s) == 1:
            return(s)
        elif len(palindrome) == 0 and len(s) != 0:
            return(s[0])

        return(palindrome)






        



#Let's implement the test cases
solution = Solution()

case_1 = "babad"
case_2 = "cbbd"
case_3 = "s"
case_4 = "ac"
print(solution.longestPalindrome(case_4))

