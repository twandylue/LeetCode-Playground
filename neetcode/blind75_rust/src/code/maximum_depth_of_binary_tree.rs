use std::cell::RefCell;
use std::cmp;
use std::rc::Rc;

use super::model::binary_tree_node::TreeNode;

pub struct Solution {}

impl Solution {
    pub fn max_depth(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
        Solution::dfs(&root, 0)
    }

    fn dfs(root: &Option<Rc<RefCell<TreeNode>>>, mut count: i32) -> i32 {
        if let Some(n) = root {
            count += 1;
            let l = Solution::dfs(&n.borrow().left, count);
            let r = Solution::dfs(&n.borrow().right, count);
            cmp::max(l, r)
        } else {
            count
        }
    }
}

#[cfg(test)]
mod tests {
    use crate::code::utils::deserialize_to_binary_tree::deserialize_to_BT;

    use super::Solution;

    #[test]
    fn case_1() {
        let root = vec![Some(3), Some(9), Some(20), None, None, Some(15), Some(7)];
        let root_tree = deserialize_to_BT(root);
        let expected = 3;
        let actual = Solution::max_depth(root_tree);

        assert_eq!(expected, actual);
    }

    #[test]
    fn case_2() {
        let root = vec![Some(1), None, Some(2)];
        let root_tree = deserialize_to_BT(root);
        let expected = 2;
        let actual = Solution::max_depth(root_tree);

        assert_eq!(expected, actual);
    }

    #[test]
    fn case_3() {
        let root = vec![Some(0)];
        let root_tree = deserialize_to_BT(root);
        let expected = 1;
        let actual = Solution::max_depth(root_tree);

        assert_eq!(expected, actual);
    }

    #[test]
    fn case_4() {
        let root = vec![];
        let root_tree = deserialize_to_BT(root);
        let expected = 0;
        let actual = Solution::max_depth(root_tree);

        assert_eq!(expected, actual);
    }
}
