class Solution:
    def mergeKLists(
        self, lists: List[Optional[ListNode]]
    ) -> Optional[ListNode]:
        if not lists:
            return None

        def merge_two(left, right):
            dummy = ListNode()
            tail = dummy

            while left is not None and right is not None:
                # The smaller head is the smallest remaining node.
                if left.val <= right.val:
                    tail.next = left
                    left = left.next
                else:
                    tail.next = right
                    right = right.next

                tail = tail.next

            # The remaining suffix is already sorted.
            tail.next = left if left is not None else right
            return dummy.next

        while len(lists) > 1:
            merged_lists = []

            for index in range(0, len(lists), 2):
                left = lists[index]
                right = (
                    lists[index + 1]
                    if index + 1 < len(lists)
                    else None
                )

                merged_lists.append(merge_two(left, right))

            lists = merged_lists

        return lists[0]
