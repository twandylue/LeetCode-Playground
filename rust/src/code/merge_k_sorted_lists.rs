use super::models::list_node::ListNode;

struct Solution {}

impl Solution {
    pub fn merge_k_lists(mut lists: Vec<Option<Box<ListNode>>>) -> Option<Box<ListNode>> {
        if lists.len() == 0 {
            return None;
        }

        while lists.len() > 1 {
            let mut merged_lists: Vec<Option<Box<ListNode>>> = Vec::new();
            for i in (0..lists.len()).step_by(2) {
                if i + 1 < lists.len() {
                    merged_lists.push(Self::merge_two_lists(
                        lists[i].clone(),
                        lists[i + 1].clone(),
                    ));
                } else {
                    merged_lists.push(Self::merge_two_lists(lists[i].clone(), None));
                }
            }

            lists = merged_lists;
        }

        return lists[0].clone();

        // NOTE: This would cause Time Limit Exceeded
        // let mut dummy_head = ListNode::new(0);
        // let mut pointer = &mut dummy_head;

        // for i in 0..lists.len() {
        //     if lists[i].is_none() {
        //         continue;
        //     }

        //     pointer.next = Self::merge_two_lists(pointer.next.clone(), lists[i].clone());
        // }

        // return dummy_head.next;
    }

    fn merge_two_lists(
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
                        next: Self::merge_two_lists(Some(l1), l2.next),
                    }))
                } else {
                    Some(Box::new(ListNode {
                        val: l1.val,
                        next: Self::merge_two_lists(l1.next, Some(l2)),
                    }))
                }
            }
        }
    }
}

#[cfg(test)]
mod tests {
    use super::Solution;
    use crate::code::utils::convert_to_linked_list::convert_vec_to_linked_list;

    #[test]
    fn merge_k_lists_case_1() {
        // arrange
        let lists = vec![
            convert_vec_to_linked_list(vec![1, 4, 5]),
            convert_vec_to_linked_list(vec![1, 3, 4]),
            convert_vec_to_linked_list(vec![2, 6]),
        ];
        let expected = convert_vec_to_linked_list(vec![1, 1, 2, 3, 4, 4, 5, 6]);

        // act
        let actual = Solution::merge_k_lists(lists);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn merge_k_lists_case_2() {
        // arrange
        let lists = vec![];
        let expected = convert_vec_to_linked_list(vec![]);

        // act
        let actual = Solution::merge_k_lists(lists);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn merge_k_lists_case_3() {
        // arrange
        let lists = vec![convert_vec_to_linked_list(vec![])];
        let expected = convert_vec_to_linked_list(vec![]);

        // act
        let actual = Solution::merge_k_lists(lists);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn merge_k_lists_case_4() {
        // arrange
        let lists = vec![
            convert_vec_to_linked_list(vec![1]),
            convert_vec_to_linked_list(vec![0]),
        ];
        let expected = convert_vec_to_linked_list(vec![0, 1]);

        // act
        let actual = Solution::merge_k_lists(lists);

        // assert
        assert_eq!(expected, actual);
    }
}
