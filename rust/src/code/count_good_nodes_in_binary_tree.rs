use crate::code::models::binary_tree_node::TreeNode;
use std::cell::RefCell;
use std::cmp::max;
use std::rc::Rc;

struct Solution {}

impl Solution {
    pub fn good_nodes(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
        let mut count = 0;
        if let Some(r) = root {
            Self::dfs(&mut count, r.borrow().val, Some(r.clone()));
        }

        count
    }

    fn dfs(count: &mut i32, mut max_val: i32, node: Option<Rc<RefCell<TreeNode>>>) {
        if let Some(n) = node {
            if n.borrow().val >= max_val {
                *count += 1;
            }
            max_val = max(n.borrow().val, max_val);
            Self::dfs(count, max_val, n.borrow().left.clone());
            Self::dfs(count, max_val, n.borrow().right.clone());
        }
    }
}

#[cfg(test)]
mod tests {
    use super::Solution;
    use crate::code::utils::deserialize_to_binary_tree::deserialize_to_BT;

    #[test]
    fn test_good_nodes_case_1() {
        // arrange
        let root = deserialize_to_BT(vec![
            Some(3),
            Some(1),
            Some(4),
            Some(3),
            None,
            Some(1),
            Some(5),
        ]);
        let expected = 4;

        // act
        let actual = Solution::good_nodes(root);

        // assert
        assert_eq!(actual, expected);
    }

    #[test]
    fn test_good_nodes_case_2() {
        // arrange
        let root = deserialize_to_BT(vec![Some(3), Some(3), None, Some(4), Some(2)]);
        let expected = 3;

        // act
        let actual = Solution::good_nodes(root);

        // assert
        assert_eq!(actual, expected);
    }

    #[test]
    fn test_good_nodes_case_3() {
        // arrange
        let root = deserialize_to_BT(vec![Some(1)]);
        let expected = 1;

        // act
        let actual = Solution::good_nodes(root);

        // assert
        assert_eq!(actual, expected);
    }

    #[test]
    fn test_good_nodes_case_4() {
        // arrange
        let root = deserialize_to_BT(vec![Some(9), None, Some(3), Some(6)]);
        let expected = 1;

        // act
        let actual = Solution::good_nodes(root);

        // assert
        assert_eq!(actual, expected);
    }

    #[test]
    fn test_good_nodes_case_5() {
        // arrange
        let root = deserialize_to_BT(vec![
            Some(-1),
            Some(5),
            Some(-2),
            Some(4),
            Some(4),
            Some(2),
            Some(-2),
            None,
            None,
            Some(-4),
            None,
            Some(-2),
            Some(3),
            None,
            Some(-2),
            Some(0),
            None,
            Some(-1),
            None,
            Some(-3),
            None,
            Some(-4),
            Some(-3),
            Some(3),
            None,
            None,
            None,
            None,
            None,
            None,
            None,
            Some(3),
            Some(-3),
        ]);
        let expected = 5;

        // act
        let actual = Solution::good_nodes(root);

        // assert
        assert_eq!(actual, expected);
    }
}
