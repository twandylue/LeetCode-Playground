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
    fn merge_two_lists_case_1() {
        // arrange
        let list1 = convert_vec_to_linked_list(vec![1, 2, 4]);
        let list2 = convert_vec_to_linked_list(vec![1, 3, 4]);
        let expected = convert_vec_to_linked_list(vec![1, 1, 2, 3, 4, 4]);

        // act
        let actual = Solution::merge_two_lists(list1, list2);

        // assert
        assert_eq!(actual, expected);
    }

    #[test]
    fn merge_two_lists_case_2() {
        // arrange
        let list1 = convert_vec_to_linked_list(vec![]);
        let list2 = convert_vec_to_linked_list(vec![]);
        let expected = convert_vec_to_linked_list(vec![]);

        // act
        let actual = Solution::merge_two_lists(list1, list2);

        // assert
        assert_eq!(actual, expected);
    }

    #[test]
    fn merge_two_lists_case_3() {
        // arrange
        let list1 = convert_vec_to_linked_list(vec![]);
        let list2 = convert_vec_to_linked_list(vec![0]);
        let expected = convert_vec_to_linked_list(vec![0]);

        // act
        let actual = Solution::merge_two_lists(list1, list2);

        // assert
        assert_eq!(actual, expected);
    }

    #[test]
    fn merge_two_lists_case_4() {
        // arrange
        let list1 = convert_vec_to_linked_list(vec![1, 2, 4]);
        let list2 = convert_vec_to_linked_list(vec![1, 3, 4]);
        let expected = convert_vec_to_linked_list(vec![1, 1, 2, 3, 4, 4]);

        // act
        let actual = Solution::merge_two_lists2(list1, list2);

        // assert
        assert_eq!(actual, expected);
    }

    #[test]
    fn merge_two_lists_case_5() {
        // arrange
        let list1 = convert_vec_to_linked_list(vec![]);
        let list2 = convert_vec_to_linked_list(vec![]);
        let expected = convert_vec_to_linked_list(vec![]);

        // act
        let actual = Solution::merge_two_lists2(list1, list2);

        // assert
        assert_eq!(actual, expected);
    }

    #[test]
    fn merge_two_lists_case_6() {
        // arrange
        let list1 = convert_vec_to_linked_list(vec![]);
        let list2 = convert_vec_to_linked_list(vec![0]);
        let expected = convert_vec_to_linked_list(vec![0]);

        // act
        let actual = Solution::merge_two_lists2(list1, list2);

        // assert
        assert_eq!(actual, expected);
    }
}
