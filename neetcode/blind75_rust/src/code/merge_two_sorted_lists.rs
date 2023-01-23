use super::models::list_node::ListNode;
use std::mem;

pub struct Solution {}

impl Solution {
    pub fn merge_two_lists(
        list1: Option<Box<ListNode>>,
        list2: Option<Box<ListNode>>,
    ) -> Option<Box<ListNode>> {
        match (list1, list2) {
            (None, None) => None,
            (Some(n), None) | (None, Some(n)) => Some(n),
            (Some(l1), Some(l2)) => {
                if l1.val >= l2.val {
                    Some(Box::new(ListNode {
                        val: l2.val,
                        next: Solution::merge_two_lists(Some(l1), l2.next),
                    }))
                } else {
                    Some(Box::new(ListNode {
                        val: l1.val,
                        next: Solution::merge_two_lists(l1.next, Some(l2)),
                    }))
                }
            }
        }
    }

    pub fn merge_two_lists2(
        list1: Option<Box<ListNode>>,
        list2: Option<Box<ListNode>>,
    ) -> Option<Box<ListNode>> {
        let mut head = None;
        let mut ptr = &mut head;
        let mut a = list1;
        let mut b = list2;

        while a.is_some() && b.is_some() {
            let l1 = &mut a;
            let l2 = &mut b;

            let mut temp = if l1.as_ref().unwrap().val < l2.as_ref().unwrap().val {
                l1
            } else {
                l2
            };

            // swap step 1
            mem::swap(ptr, &mut temp);
            // swap step 2
            mem::swap(temp, &mut ptr.as_mut().unwrap().next);
            // step 3
            ptr = &mut ptr.as_mut().unwrap().next;
        }

        mem::swap(ptr, if a.is_none() { &mut b } else { &mut a });

        head
    }
}

#[cfg(test)]
mod test {
    use super::super::utils::convert_to_linked_list::convert_vec_to_linked_list;
    use super::Solution;

    #[test]
    fn case_1() {
        let list1 = convert_vec_to_linked_list(vec![1, 2, 4]);
        let list2 = convert_vec_to_linked_list(vec![1, 3, 4]);
        let expected = convert_vec_to_linked_list(vec![1, 1, 2, 3, 4, 4]);
        let actual = Solution::merge_two_lists2(list1, list2);

        assert_eq!(actual, expected);

        let list1 = convert_vec_to_linked_list(vec![]);
        let list2 = convert_vec_to_linked_list(vec![]);
        let expected2 = convert_vec_to_linked_list(vec![]);
        let actual2 = Solution::merge_two_lists2(list1, list2);

        assert_eq!(actual2, expected2);

        let list1 = convert_vec_to_linked_list(vec![]);
        let list2 = convert_vec_to_linked_list(vec![0]);
        let expected3 = convert_vec_to_linked_list(vec![0]);
        let actual3 = Solution::merge_two_lists2(list1, list2);

        assert_eq!(actual3, expected3);
    }
}

// -- output:
// before:
// ptr: None
// temp: Some(ListNode { val: 1, next: Some(ListNode { val: 3, next: Some(ListNode { val: 4, next: None }) }) })
// swap step 1:
// ptr: Some(ListNode { val: 1, next: Some(ListNode { val: 3, next: Some(ListNode { val: 4, next: None }) }) })
// temp: None
// swap step 2:
// ptr: Some(ListNode { val: 1, next: None })
// temp: Some(ListNode { val: 3, next: Some(ListNode { val: 4, next: None }) })
// step 3:
// ptr: None
// temp: Some(ListNode { val: 3, next: Some(ListNode { val: 4, next: None }) })
// -----------------------------
// before:
// ptr: None
// temp: Some(ListNode { val: 1, next: Some(ListNode { val: 2, next: Some(ListNode { val: 4, next: None }) }) })
// swap step 1:
// ptr: Some(ListNode { val: 1, next: Some(ListNode { val: 2, next: Some(ListNode { val: 4, next: None }) }) })
// temp: None
// swap step 2:
// ptr: Some(ListNode { val: 1, next: None })
// temp: Some(ListNode { val: 2, next: Some(ListNode { val: 4, next: None }) })
// step 3:
// ptr: None
// temp: Some(ListNode { val: 2, next: Some(ListNode { val: 4, next: None }) })
// -----------------------------
// before:
// ptr: None
// temp: Some(ListNode { val: 2, next: Some(ListNode { val: 4, next: None }) })
// swap step 1:
// ptr: Some(ListNode { val: 2, next: Some(ListNode { val: 4, next: None }) })
// temp: None
// swap step 2:
// ptr: Some(ListNode { val: 2, next: None })
// temp: Some(ListNode { val: 4, next: None })
// step 3:
// ptr: None
// temp: Some(ListNode { val: 4, next: None })
// -----------------------------
// before:
// ptr: None
// temp: Some(ListNode { val: 3, next: Some(ListNode { val: 4, next: None }) })
// swap step 1:
// ptr: Some(ListNode { val: 3, next: Some(ListNode { val: 4, next: None }) })
// temp: None
// swap step 2:
// ptr: Some(ListNode { val: 3, next: None })
// temp: Some(ListNode { val: 4, next: None })
// step 3:
// ptr: None
// temp: Some(ListNode { val: 4, next: None })
// -----------------------------
// before:
// ptr: None
// temp: Some(ListNode { val: 4, next: None })
// swap step 1:
// ptr: Some(ListNode { val: 4, next: None })
// temp: None
// swap step 2:
// ptr: Some(ListNode { val: 4, next: None })
// temp: None
// step 3:
// ptr: None
// temp: None
// -----------------------------
