use super::models::list_node::ListNode;

pub struct Solution {}

impl Solution {
    pub fn reorder_list(head: &mut Option<Box<ListNode>>) {
        let len = Self::get_length(head);
        let mut f = head.as_mut();

        for _ in 0..(len / 2) {
            if let Some(n) = f {
                f = n.next.as_mut();
            }
        }

        if let Some(node) = f {
            let rev = Self::reverse_linked_list(node.next.take(), None);

            if let Some(n) = head {
                n.next = Self::merge_two_list(rev, n.next.take());
            }
        }
    }

    fn merge_two_list(
        mut left: Option<Box<ListNode>>,
        right: Option<Box<ListNode>>,
    ) -> Option<Box<ListNode>> {
        match (left.as_mut(), right.as_ref()) {
            (None, None) => None,
            (Some(_), None) => left,
            (None, Some(_)) => right,
            (Some(l), Some(_)) => {
                l.next = Self::merge_two_list(right, l.next.take());
                left
            }
        }
    }

    fn reverse_linked_list(
        node: Option<Box<ListNode>>,
        prev: Option<Box<ListNode>>,
    ) -> Option<Box<ListNode>> {
        match node {
            None => prev,
            Some(mut n) => {
                let n_next = n.next;
                n.next = prev;
                Self::reverse_linked_list(n_next, Option::Some(n))
            }
        }
    }

    fn get_length(mut head: &Option<Box<ListNode>>) -> usize {
        let mut count: usize = 0;
        while let Some(n) = head {
            count += 1;
            head = &n.next;
        }

        count
    }
}

#[cfg(test)]
mod test {
    use super::super::utils::convert_to_linked_list::convert_vec_to_linked_list;
    use super::Solution;

    #[test]
    fn case_1() {
        let mut head = convert_vec_to_linked_list(vec![1, 2, 3, 4]);
        let expected = convert_vec_to_linked_list(vec![1, 4, 2, 3]);
        Solution::reorder_list(&mut head);

        assert_eq!(head, expected);

        let mut head2 = convert_vec_to_linked_list(vec![1, 2, 3, 4, 5]);
        let expected2 = convert_vec_to_linked_list(vec![1, 5, 2, 4, 3]);
        Solution::reorder_list(&mut head2);

        assert_eq!(head2, expected2);
    }
}
