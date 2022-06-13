class Solution:
	def middleNode(self,head):
		middle=breaker=head
		while breaker and breaker.next:middle=middle.next;breaker=breaker.next.next
		return middle