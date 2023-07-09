use super::models::list_node::ListNode;

struct Solution {}

impl Solution {
    pub fn add_two_numbers(
        mut l1: Option<Box<ListNode>>,
        mut l2: Option<Box<ListNode>>,
    ) -> Option<Box<ListNode>> {
        let mut carry: i32 = 0;
        let mut dummy_head: ListNode = ListNode::new(0);
        // NOTE: Important skill in dummy head
        let mut head: &mut ListNode = &mut dummy_head;

        while l1.is_some() || l2.is_some() || carry > 0 {
            let mut sum: i32 = 0;
            if let Some(l) = l1.clone() {
                sum += l.val;
                l1 = l.next
            }

            if let Some(l) = l2.clone() {
                sum += l.val;
                l2 = l.next
            }
            sum += carry;
            carry = sum / 10;
            head.next = Some(Box::new(ListNode::new(sum % 10)));
            head = head.next.as_mut().unwrap();
        }

        dummy_head.next
    }

    pub fn add_two_numbers_2(
        l1: Option<Box<ListNode>>,
        l2: Option<Box<ListNode>>,
    ) -> Option<Box<ListNode>> {
        match (l1, l2) {
            (None, None) => None,
            (Some(n), None) | (None, Some(n)) => Some(n),
            (Some(n1), Some(n2)) => {
                let sum: i32 = n1.val + n2.val;
                if sum >= 10 {
                    Some(Box::new(ListNode {
                        val: sum % 10,
                        next: Self::add_two_numbers_2(
                            Self::add_two_numbers_2(
                                Some(Box::new(ListNode {
                                    val: sum / 10,
                                    next: None,
                                })),
                                n1.next,
                            ),
                            n2.next,
                        ),
                    }))
                } else {
                    Some(Box::new(ListNode {
                        val: sum,
                        next: Self::add_two_numbers_2(n1.next, n2.next),
                    }))
                }
            }
        }
    }
}

#[cfg(test)]
mod test {
    use super::super::utils::convert_to_linked_list::convert_vec_to_linked_list;
    use super::Solution;

    #[test]
    fn add_two_numbers_case_1() {
        // arrange
        let l1 = convert_vec_to_linked_list(vec![2, 4, 3]);
        let l2 = convert_vec_to_linked_list(vec![5, 6, 4]);
        let expected = convert_vec_to_linked_list(vec![7, 0, 8]);

        // act
        let actual = Solution::add_two_numbers(l1, l2);

        // assert
        assert_eq!(actual, expected);
    }

    #[test]
    fn add_two_numbers_case_2() {
        // arrange
        let l1 = convert_vec_to_linked_list(vec![0]);
        let l2 = convert_vec_to_linked_list(vec![0]);
        let expected = convert_vec_to_linked_list(vec![0]);

        // act
        let actual = Solution::add_two_numbers(l1, l2);

        // assert
        assert_eq!(actual, expected);
    }

    #[test]
    fn add_two_numbers_case_3() {
        // arrange
        let l1 = convert_vec_to_linked_list(vec![9, 9, 9, 9, 9, 9, 9]);
        let l2 = convert_vec_to_linked_list(vec![9, 9, 9, 9]);
        let expected = convert_vec_to_linked_list(vec![8, 9, 9, 9, 0, 0, 0, 1]);

        // act
        let actual = Solution::add_two_numbers(l1, l2);

        // assert
        assert_eq!(actual, expected);
    }

    #[test]
    fn add_two_numbers_case_4() {
        // arrange
        let l1 = convert_vec_to_linked_list(vec![2, 4, 3]);
        let l2 = convert_vec_to_linked_list(vec![5, 6, 4]);
        let expected = convert_vec_to_linked_list(vec![7, 0, 8]);

        // act
        let actual = Solution::add_two_numbers_2(l1, l2);

        // assert
        assert_eq!(actual, expected);
    }

    #[test]
    fn add_two_numbers_case_5() {
        // arrange
        let l1 = convert_vec_to_linked_list(vec![0]);
        let l2 = convert_vec_to_linked_list(vec![0]);
        let expected = convert_vec_to_linked_list(vec![0]);

        // act
        let actual = Solution::add_two_numbers_2(l1, l2);

        // assert
        assert_eq!(actual, expected);
    }

    #[test]
    fn add_two_numbers_case_6() {
        // arrange
        let l1 = convert_vec_to_linked_list(vec![9, 9, 9, 9, 9, 9, 9]);
        let l2 = convert_vec_to_linked_list(vec![9, 9, 9, 9]);
        let expected = convert_vec_to_linked_list(vec![8, 9, 9, 9, 0, 0, 0, 1]);

        // act
        let actual = Solution::add_two_numbers_2(l1, l2);

        // assert
        assert_eq!(actual, expected);
    }
}
