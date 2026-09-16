class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        curr = head
        count = 0

        while curr:
            count += 1
            curr = curr.next

        index_of_half = math.ceil(count / 2)

        secondary_list_head = head
        prev = None

        # Find start of second half
        for _ in range(index_of_half):
            prev = secondary_list_head
            secondary_list_head = secondary_list_head.next

        # Split the list
        prev.next = None

        # Reverse second half
        curr = secondary_list_head
        prev = None

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        second = prev
        first = head

        # Merge
        while second:
            first_next = first.next
            second_next = second.next

            first.next = second
            second.next = first_next

            first = first_next
            second = second_next