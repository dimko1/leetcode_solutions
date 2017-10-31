# url: https://leetcode.com/problems/reorder-list/description/
# Given a singly linked list L: L0→L1→…→Ln-1→Ln,
# reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…
#
# You must do this in-place without altering the nodes' values.
#
# For example,
# Given {1,2,3,4}, reorder it to {1,4,2,3}.
#
# Comment:
# Solution very straight forward: splitting list on two, reverting second part of list, merging two lists


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    # split list with "runner algorithm"
    def splitList(self, head):
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        middle = slow.next
        slow.next = None

        return head, middle

    # reverting
    def reverseList(self, head):
        currentNode = head
        last = None

        while currentNode:
            nextNode = currentNode.next
            currentNode.next = last
            last = currentNode
            currentNode = nextNode

        return last

    # merging
    def mergeList(self, l, r):
        tail = l
        head = l

        l = l.next
        while r:
            tail.next = r
            tail = tail.next
            r = r.next
            if l:
                l, r = r, l

        return head

    def reorderList(self, head):
        if not head: return head

        head, middle = self.splitList(head)

        middle = self.reverseList(middle)
        
        # tadaaaaam
        head = self.mergeList(head, middle)
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """