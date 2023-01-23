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
    pub fn remove_nth_from_end(head: Option<Box<ListNode>>, mut n: i32) -> Option<Box<ListNode>> {
        let mut dummy = Box::new(ListNode {
            val: 0,
            next: head.clone(),
        });

        let mut fast = dummy.clone();
        let mut slow = dummy.as_mut();

        while let Some(node) = fast.next.take() {
            if n <= 0 {
                slow = slow.next.as_mut().unwrap();
            }
            fast = node.clone();
            n -= 1;
        }

        slow.next = slow.next.as_mut().unwrap().next.clone();
        return dummy.next;
    }

    // TODO: move to utils
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

/*
* Note:
* it will move Box<self>, which is allocated on heap, and Rust doesn't allow you to just move values away from heap unless you implement Copy, otherwise what's left there?
* The book uses Option::take() to move ownership out and leave None on the place.
*/

#[cfg(test)]
mod test {
    use super::Solution;

    #[test]
    fn case_1() {
        let head = Solution::convert_vec_to_linked_list(vec![1, 2, 3, 4, 5]);
        let n = 2;
        let expected = Solution::convert_vec_to_linked_list(vec![1, 2, 3, 5]);
        let actual = Solution::remove_nth_from_end(head, n);

        assert_eq!(actual, expected);

        let head2 = Solution::convert_vec_to_linked_list(vec![1]);
        let n2 = 1;
        let expected2 = Solution::convert_vec_to_linked_list(vec![]);
        let actual2 = Solution::remove_nth_from_end(head2, n2);

        assert_eq!(actual2, expected2);

        let head3 = Solution::convert_vec_to_linked_list(vec![1, 2]);
        let n3 = 1;
        let expected3 = Solution::convert_vec_to_linked_list(vec![1]);
        let actual3 = Solution::remove_nth_from_end(head3, n3);

        assert_eq!(actual3, expected3);
    }
}
