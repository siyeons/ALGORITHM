# List 사용
def isPalindrome(self, head: ListNode) -> bool:
    q: List[]
    
    if not head:
        return True
    
    node = head
    
    while node is not None:
        q.append(node.val)
        node = node.next
    
    while len(q) > 1:
        if q.pop(0) != q.pop():
            return False
    
    return True

# Deque 사용 
def isPalindrome(self, head: ListNode) -> bool:
    q: Deque = collections.deque()
    
    if not head:
        return True
    
    node = head
    while node is not None:
        q.append(node.val)
        node = node.next
    
    while len(q) > 1:
        if q.popleft() != q.pop():
            return False
    
    return True