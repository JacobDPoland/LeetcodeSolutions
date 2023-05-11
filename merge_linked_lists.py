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
        return_head = return_list
        
        
        while (not list1 == None) or (not list2 == None):

            if (list1 == None) and (not list2 == None):
                return_list.next = ListNode(list2.val)
                list2 = list2.next
                
            elif (not list1 == None) and (list2 == None):
                return_list.next = ListNode(list1.val)
                list1 = list1.next
            
            elif list1.val <= list2.val:
                return_list.next = ListNode(list1.val)
                list1 = list1.next
                
            elif list2.val < list1.val:
                return_list.next = ListNode(list2.val)
                list2 = list2.next
           
            return_list = return_list.next

        
        return_head = return_head.next  # fix head
        return return_head