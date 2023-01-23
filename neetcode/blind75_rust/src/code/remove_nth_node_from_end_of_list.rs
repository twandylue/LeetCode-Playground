use super::models::list_node::ListNode;

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
}

/*
* Note:
* it will move Box<self>, which is allocated on heap, and Rust doesn't allow you to just move values away from heap unless you implement Copy, otherwise what's left there?
* The book uses Option::take() to move ownership out and leave None on the place.
*/

#[cfg(test)]
mod test {
    use super::super::utils::convert_to_linked_list::convert_vec_to_linked_list;
    use super::Solution;

    #[test]
    fn case_1() {
        let head = convert_vec_to_linked_list(vec![1, 2, 3, 4, 5]);
        let n = 2;
        let expected = convert_vec_to_linked_list(vec![1, 2, 3, 5]);
        let actual = Solution::remove_nth_from_end(head, n);

        assert_eq!(actual, expected);

        let head2 = convert_vec_to_linked_list(vec![1]);
        let n2 = 1;
        let expected2 = convert_vec_to_linked_list(vec![]);
        let actual2 = Solution::remove_nth_from_end(head2, n2);

        assert_eq!(actual2, expected2);

        let head3 = convert_vec_to_linked_list(vec![1, 2]);
        let n3 = 1;
        let expected3 = convert_vec_to_linked_list(vec![1]);
        let actual3 = Solution::remove_nth_from_end(head3, n3);

        assert_eq!(actual3, expected3);
    }
}
