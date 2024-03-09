#include <stdio.h>

struct ListNode {
  int val;
  struct ListNode *next;
};

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

int main(void) { return 0; }
