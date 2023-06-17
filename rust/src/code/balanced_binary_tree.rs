use super::models::binary_tree_node::TreeNode;
use std::cell::RefCell;
use std::rc::Rc;

struct Solution {}

impl Solution {
    pub fn is_balanced(root: Option<Rc<RefCell<TreeNode>>>) -> bool {
        Self::helper(&root).0
    }

    fn helper(root: &Option<Rc<RefCell<TreeNode>>>) -> (bool, i32) {
        if let Some(node) = root {
            let left = Self::helper(&node.borrow().left);
            let right = Self::helper(&node.borrow().right);
            let balanced = left.0 && right.0 && (left.1 - right.1).abs() <= 1;

            (balanced, std::cmp::max(left.1, right.1) + 1)
        } else {
            (true, 0)
        }
    }
}

#[cfg(test)]
mod test {
    use super::Solution;
    use crate::code::utils::deserialize_to_binary_tree::deserialize_to_BT;

    #[test]
    fn balanced_binary_tree_case_1() {
        // arrange
        let root = vec![Some(3), Some(9), Some(20), None, None, Some(15), Some(7)];
        let expected = true;

        // act
        let actual = Solution::is_balanced(deserialize_to_BT(root));

        // assert
        assert_eq!(expected, actual)
    }

    #[test]
    fn balanced_binary_tree_case_2() {
        // arrange
        let root = vec![
            Some(1),
            Some(2),
            Some(2),
            Some(3),
            Some(3),
            None,
            None,
            Some(4),
            Some(4),
        ];
        let expected = false;

        // act
        let actual = Solution::is_balanced(deserialize_to_BT(root));

        // assert
        assert_eq!(expected, actual)
    }

    #[test]
    fn balanced_binary_tree_case_3() {
        // arrange
        let root = vec![];
        let expected = true;

        // act
        let actual = Solution::is_balanced(deserialize_to_BT(root));

        // assert
        assert_eq!(expected, actual)
    }
}
