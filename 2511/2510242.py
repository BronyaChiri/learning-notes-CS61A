# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        class ListNode:
            def __init__(self,val=0,next=None):
                self.val = val
                self.next = next

            def reverse(self,done):
                t = ListNode(self.val,self.next)
                while(t.next!=0):
                    t = t.next
                  
                return ListNode(t.val,reverse(self))
                
                               

        def link_add(link1,link2):
            valn = ad(link1.val,link2.val)
            if link1.next != None:
                nextn = link_add(link1.next,link2.next)
            else:
                nextn = None
            return ListNode(valn,nextn)



        def ad(x,y):
            t = x + y
            return t%10 

        return link_add(l1,l2)  