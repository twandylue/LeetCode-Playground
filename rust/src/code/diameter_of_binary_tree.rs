use std::cell::RefCell;
use std::rc::Rc;

use super::models::binary_tree_node::TreeNode;

struct Solution {}

impl Solution {
    pub fn diameter_of_binary_tree(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
        let mut max: i32 = 0;
        Self::get_diameter(&root, &mut max);

        max
    }

    fn get_diameter(root: &Option<Rc<RefCell<TreeNode>>>, max: &mut i32) -> i32 {
        if let Some(node) = root {
            let left = Self::get_diameter(&node.borrow().left, max);
            let right = Self::get_diameter(&node.borrow().right, max);
            *max = std::cmp::max(left + right, *max);
            std::cmp::max(left, right) + 1
        } else {
            0
        }
    }
}

#[cfg(test)]
mod tests {
    use super::Solution;
    use crate::code::utils::deserialize_to_binary_tree::deserialize_to_BT;

    #[test]
    fn diameter_of_binary_tree_case_1() {
        // arrange
        let root = vec![Some(1), Some(2), Some(3), Some(4), Some(5)];
        let expected = 3;

        // act
        let actual = Solution::diameter_of_binary_tree(deserialize_to_BT(root));

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn diameter_of_binary_tree_case_2() {
        // arrange
        let root = vec![Some(1), Some(2)];
        let expected = 1;

        // act
        let actual = Solution::diameter_of_binary_tree(deserialize_to_BT(root));

        // assert
        assert_eq!(expected, actual);
    }
}
