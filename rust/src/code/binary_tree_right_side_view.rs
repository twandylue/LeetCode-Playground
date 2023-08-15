use crate::code::models::binary_tree_node::TreeNode;
use std::cell::RefCell;
use std::collections::VecDeque;
use std::rc::Rc;

struct Solution {}
impl Solution {
    pub fn right_side_view(root: Option<Rc<RefCell<TreeNode>>>) -> Vec<i32> {
        let mut result: Vec<i32> = Vec::new();
        let mut queue: VecDeque<Option<Rc<RefCell<TreeNode>>>> = VecDeque::from([root]);

        while !queue.is_empty() {
            let curr_queue_len: usize = queue.len();
            let mut right_node: Option<Rc<RefCell<TreeNode>>> = None;
            for _ in 0..curr_queue_len {
                if let Some(node) = queue.pop_front() {
                    if let Some(e) = node.clone() {
                        right_node = node;
                        queue.push_back(e.borrow().left.clone());
                        queue.push_back(e.borrow().right.clone());
                    }
                }
            }

            if let Some(r) = right_node {
                result.push(r.borrow().val);
            }
        }

        result
    }
}

#[cfg(test)]
mod tests {
    use super::Solution;
    use crate::code::utils::deserialize_to_binary_tree::deserialize_to_BT;

    #[test]
    fn test_right_side_view_case_1() {
        // arrange
        let root = deserialize_to_BT(vec![
            Some(1),
            Some(2),
            Some(3),
            None,
            Some(5),
            None,
            Some(4),
        ]);
        let expected = vec![1, 3, 4];

        // act
        let actual = Solution::right_side_view(root);

        // assert
        assert_eq!(actual, expected);
    }

    #[test]
    fn test_right_side_view_case_2() {
        // arrange
        let root = deserialize_to_BT(vec![Some(1), None, Some(3)]);
        let expected = vec![1, 3];

        // act
        let actual = Solution::right_side_view(root);

        // assert
        assert_eq!(actual, expected);
    }

    #[test]
    fn test_right_side_view_case_3() {
        // arrange
        let root = deserialize_to_BT(vec![]);
        let expected = vec![];

        // act
        let actual = Solution::right_side_view(root);

        // assert
        assert_eq!(actual, expected);
    }

    #[test]
    fn test_right_side_view_case_4() {
        // arrange
        let root = deserialize_to_BT(vec![Some(1), Some(2)]);
        let expected = vec![1, 2];

        // act
        let actual = Solution::right_side_view(root);

        // assert
        assert_eq!(actual, expected);
    }

    #[test]
    fn test_right_side_view_case_5() {
        // arrange
        let root = deserialize_to_BT(vec![
            Some(0),
            Some(1),
            Some(2),
            None,
            Some(3),
            Some(4),
            None,
            None,
            Some(5),
            Some(9),
            None,
            None,
            Some(6),
            Some(10),
            None,
        ]);
        let expected = vec![0, 2, 4, 9, 10];

        // act
        let actual = Solution::right_side_view(root);

        // assert
        assert_eq!(actual, expected);
    }
}
