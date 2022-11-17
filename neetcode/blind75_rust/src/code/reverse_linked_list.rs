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
    pub fn reverse_list3(head: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
        let mut curr = head;
        let mut prev = None;

        while let Some(mut node) = curr {
            let new_head = mem::replace(&mut node.next, prev);
            curr = new_head;
            prev = Some(node);
        }

        return prev;
    }

    pub fn reverse_list2(head: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
        let mut prev = None;
        let mut curr = head;

        while let Some(mut node) = curr {
            curr = node.next;
            node.next = prev;
            prev = Some(node);
        }

        return prev;
    }

    pub fn reverse_list(head: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
        // Self::reverse(head, None)
        Self::reverse2(head, None)
    }

    fn reverse(node: Option<Box<ListNode>>, prev: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
        match node {
            None => prev,
            Some(mut n) => {
                let n_next = n.next;
                n.next = prev;
                Self::reverse(n_next, Option::Some(n))
            }
        }
    }

    fn reverse2(node: Option<Box<ListNode>>, prev: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
        match node {
            None => prev,
            Some(mut n) => {
                // replace mem
                let new_h = mem::replace(&mut n.next, prev);
                Self::reverse(new_h, Some(n))
            }
        }
    }

    pub fn tests() {
        let head = Self::convert_vec_to_linked_list(vec![1, 2, 3, 4, 5]);
        let expected = Self::convert_vec_to_linked_list(vec![5, 4, 3, 2, 1]);
        let actual = Solution::reverse_list3(head);

        assert_eq!(actual, expected);

        let head2 = Self::convert_vec_to_linked_list(vec![1, 2]);
        let expected2 = Self::convert_vec_to_linked_list(vec![2, 1]);
        let actual2 = Solution::reverse_list3(head2);

        assert_eq!(actual2, expected2);

        let head3 = Self::convert_vec_to_linked_list(vec![]);
        let expected3 = Self::convert_vec_to_linked_list(vec![]);
        let actual3 = Solution::reverse_list3(head3);

        assert_eq!(actual3, expected3);
    }

    pub fn convert_vec_to_linked_list(vector: Vec<i32>) -> Option<Box<ListNode>> {
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
