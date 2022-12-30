use std::cell::RefCell;
use std::rc::Rc;

use super::models::binary_tree_node::TreeNode;

pub struct Solution {}

impl Solution {
    pub fn is_subtree(
        root: Option<Rc<RefCell<TreeNode>>>,
        sub_root: Option<Rc<RefCell<TreeNode>>>,
    ) -> bool {
        if Solution::same_tree(&root, &sub_root) {
            return true;
        }
        match (root, sub_root) {
            (Some(r), Some(s)) => {
                return Solution::is_subtree(r.borrow().left.clone(), Some(s.clone()))
                    || Solution::is_subtree(r.borrow().right.clone(), Some(s.clone()));
            }
            (_, None) => return true,
            (None, _) => return false,
        }
    }

    fn same_tree(s: &Option<Rc<RefCell<TreeNode>>>, t: &Option<Rc<RefCell<TreeNode>>>) -> bool {
        match (s, t) {
            (None, None) => true,
            (Some(a), Some(b)) => {
                if a.borrow().val == b.borrow().val {
                    return Solution::same_tree(&a.borrow().right, &b.borrow().right)
                        && Solution::same_tree(&a.borrow().left, &b.borrow().left);
                }
                return false;
            }
            (_, _) => false,
        }
    }
}

#[cfg(test)]
mod tests {
    use crate::code::utils::deserialize_to_binary_tree::deserialize_to_BT;

    use super::Solution;

    #[test]
    fn case_1() {
        let root = vec![Some(3), Some(4), Some(5), Some(1), Some(2)];
        let sub_root = vec![Some(4), Some(1), Some(2)];
        let expected = true;
        let actual = Solution::is_subtree(deserialize_to_BT(root), deserialize_to_BT(sub_root));

        assert_eq!(expected, actual);
    }

    #[test]
    fn case_2() {
        let root = vec![
            Some(3),
            Some(4),
            Some(5),
            Some(1),
            Some(2),
            None,
            None,
            None,
            None,
            Some(0),
        ];
        let sub_root = vec![Some(4), Some(1), Some(2)];
        let expected = false;
        let actual = Solution::is_subtree(deserialize_to_BT(root), deserialize_to_BT(sub_root));

        assert_eq!(expected, actual);
    }
}
