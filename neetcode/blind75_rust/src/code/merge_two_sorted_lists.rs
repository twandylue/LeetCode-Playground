use std::mem;

// Definition for singly-linked list.
#[derive(PartialEq, Eq, Clone, Debug)]
pub struct ListNode {
    pub val: i32,
    pub next: Option<Box<ListNode>>,
}

impl ListNode {
    #[inline]
    fn new(val: i32) -> Self {
        ListNode { next: None, val }
    }
}

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

            mem::swap(ptr, &mut temp);
            mem::swap(temp, &mut ptr.as_mut().unwrap().next);
            ptr = &mut ptr.as_mut().unwrap().next;
        }

        mem::swap(ptr, if a.is_none() { &mut b } else { &mut a });

        head
    }

    pub fn tests() {
        let list1 = Self::convert_vec_to_linked_list(vec![1, 2, 4]);
        let list2 = Self::convert_vec_to_linked_list(vec![1, 3, 4]);
        let expected = Self::convert_vec_to_linked_list(vec![1, 1, 2, 3, 4, 4]);
        let actual = Self::merge_two_lists2(list1, list2);

        assert_eq!(actual, expected);

        let list1 = Self::convert_vec_to_linked_list(vec![]);
        let list2 = Self::convert_vec_to_linked_list(vec![]);
        let expected2 = Self::convert_vec_to_linked_list(vec![]);
        let actual2 = Self::merge_two_lists2(list1, list2);

        assert_eq!(actual2, expected2);

        let list1 = Self::convert_vec_to_linked_list(vec![]);
        let list2 = Self::convert_vec_to_linked_list(vec![0]);
        let expected3 = Self::convert_vec_to_linked_list(vec![0]);
        let actual3 = Self::merge_two_lists2(list1, list2);

        assert_eq!(actual3, expected3);
    }

    fn convert_vec_to_linked_list(vector: Vec<i32>) -> Option<Box<ListNode>> {
        if vector.len() == 0 {
            return None;
        } else {
            return Some(Box::new(ListNode {
                val: vector[0],
                next: Self::convert_vec_to_linked_list(vector[1..].to_vec()),
            }));
        }
    }
}
