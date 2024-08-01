class Solution:
    def isValid(self, s: str) -> bool:
        #We want to use a stack
        stack = []

        for i, paren in enumerate(s):
            if paren == "(" or paren == "{" or paren == "[":
                stack.append(paren)
            else:
                if paren == ")":
                    if len(stack) == 0 or stack.pop() != "(":
                        return False
                elif paren == "}":
                    if len(stack) == 0 or stack.pop() != "{":
                        return False
                else:
                    if len(stack) == 0 or stack.pop() != "[":
                        return False

        
        if len(stack) == 0:
            return True
        else:
            return False

test_1 = "()"
test_2 = "()[]{}"
test_3 = "(]"
test_4 = "["

solution = Solution()

print(solution.isValid(test_1))
print(solution.isValid(test_2))
print(solution.isValid(test_3))
print(solution.isValid(test_4))
