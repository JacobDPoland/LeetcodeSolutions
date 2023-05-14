# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        
        if (list1 == None) and (list2 == None):
            return None
        elif (list1 == None) and (not list2 == None):
            return list2
        elif (not list1 == None) and (list2 == None):
            return list1
        

        return_list = ListNode()  # empty node that will be thrown away at the end
        return_head = return_list  # save the head of the return_list for the very end
        
        # while at least one of them is not a None pointer, add nodes one at a time
        while (not list1 == None) or (not list2 == None):
            # check if one of the pointers is None
            if (list1 == None) and (not list2 == None):
                return_list.next = ListNode(list2.val)  # copy value that list2 points to
                list2 = list2.next  # advance list2 pointer
            elif (not list1 == None) and (list2 == None):
                return_list.next = ListNode(list1.val)
                list1 = list1.next
            
            # if neither them point to None, append the lesser value to return_list
            elif list1.val <= list2.val: 
                return_list.next = ListNode(list1.val)
                list1 = list1.next
            elif list2.val < list1.val:
                return_list.next = ListNode(list2.val)
                list2 = list2.next
           
            return_list = return_list.next  # advance return_list pointer for next iteration

        
        return_head = return_head.next  # discard empty node that was used for initialization
        return return_head