#include <stdio.h>

struct ListNode {
  int val;
  struct ListNode *next;
};

/**
 * @brief Remove all elements from a linked list of integers that have value
 * val by using indirect pointer.
 *
 * @param head
 * @param val
 *
 * @return the head of the linked list
 */
struct ListNode *removeElements(struct ListNode *head, int val) {
  if (head == NULL) {
    return NULL;
  }
  struct ListNode **indirect = &head;
  while (*indirect != NULL) {
    if ((*indirect)->val == val) {
      *indirect = (*indirect)->next;
    } else {
      indirect = &(*indirect)->next;
    }
  }
  return head;
}
