#Import optional
from typing import Optional

#Construct the definition for a singly-linked list
class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        #We will use strings to hold the values and then convert them into ints
        str_1 = ""
        str_2 = ""

        #Loop through the two to get the strings
        while l1 or l2:
            if l1:
                str_1 = str(l1.val) + str_1
                l1 = l1.next

            if l2:
                str_2 = str(l2.val) + str_2
                l2 = l2.next

        #Now we cast them
        int_1 = int(str_1)
        int_2 = int(str_2)

        #And we add them
        twoSum = int_1 + int_2

        #Now we convert back into a string
        twoString = str(twoSum)

        #And we start from the end and slowly convert it into a linked list, but we must initialize the head first
        head = ListNode(val = int(twoString[len(twoString)-1]))
        current = head
        for i in range(len(twoString) - 2, -1, -1):
            #Convert the char into an int
            val_3 = int(twoString[i])

            #Now add it to the linked list
            current.next = ListNode(val = val_3)
            current = current.next

        return head

#So we need a helper function to turn the list into a linked list
def helper_link(elements):
    head = ListNode(val = elements[0])
    current = head

    for value in elements[1:]:
        current.next = ListNode(val = value)
        current = current.next

    return head

#Need another helper function to print the linked list
def print_list(node):
    final_list = []
    while node:
        final_list.append(node.val)
        node = node.next
    
    print(final_list)
        
    
solution = Solution()


l1 = [2,4,3]
l1 = helper_link(l1)
l2 = [5,6,4]
l2 = helper_link(l2)
print_list(solution.addTwoNumbers(l1, l2))


l1 = [0]
l1 = helper_link(l1)
l2 = [0]
l2 = helper_link(l2)
print_list(solution.addTwoNumbers(l1, l2))

l1 = [9,9,9,9,9,9,9]
l1 = helper_link(l1)
l2 = [9,9,9,9]
l2 = helper_link(l2)
print_list(solution.addTwoNumbers(l1,l2))