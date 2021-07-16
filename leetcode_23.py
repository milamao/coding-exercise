import heapq

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    # solution 1 - Simple list
    '''
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists:
            return None

        if len(lists) == 1:
            return lists[0]

        nodes = []
        for i in range(len(lists)):
            node = lists[i]
            while node:
                nodes.append((node.val, node))
                node = node.next

        if not nodes:
            return None

        nodes.sort()
        for i in range(len(nodes)-1):
            nodes[i][1].next = nodes[i+1][1]
        nodes[-1][1].next = None

        return nodes[0][1]
    '''

    # solution 2 - heap
    def mergeKLists(self, lists):
        dummy = curr = ListNode(0)
        heap = []
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, lists[i]))
        while heap:
            val, node = heapq.heappop(heap)
            curr.next = node
            curr = node
            if node.next:
                heapq.heappush(heap, (node.next.val, node.next))
        return dummy.next