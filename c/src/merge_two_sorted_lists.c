#include <stdio.h>

struct ListNode {
	int val;
	struct ListNode *next;
};

/**
 * By using indirect pointer, merge two sorted linked lists and return it as a new list.
 */
struct ListNode *mergeTwoLists(struct ListNode *list1, struct ListNode *list2)
{
	struct ListNode *head = NULL;
	struct ListNode **ptr = &head;
	struct ListNode **node = NULL;

	while (list1 != NULL && list2 != NULL) {
		node = (list1->val < list2->val) ? &list1 : &list2;
		*ptr = *node;
		ptr = &(*ptr)->next;
		*node = (*node)->next;
	}
	if (list1 == NULL) {
		*ptr = list2;
	} else {
		*ptr = list1;
	}
	return head;
}

int main(void)
{
	return 0;
}
