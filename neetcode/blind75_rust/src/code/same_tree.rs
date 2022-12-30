use std::cell::RefCell;
use std::rc::Rc;

use super::model::binary_tree_node::TreeNode;

pub struct Solution {}

impl Solution {
    pub fn is_same_tree_2(
        p: Option<Rc<RefCell<TreeNode>>>,
        q: Option<Rc<RefCell<TreeNode>>>,
    ) -> bool {
        if p == None && q == None {
            return true;
        }
        match (p, q) {
            (Some(a), Some(b)) => {
                if a.borrow().val == b.borrow().val {
                    return Solution::is_same_tree_2(
                        a.borrow().left.clone(),
                        b.borrow().left.clone(),
                    ) && Solution::is_same_tree_2(
                        a.borrow().right.clone(),
                        b.borrow().right.clone(),
                    );
                }
                return false;
            }
            (_, _) => false,
        }
    }

    pub fn is_same_tree(
        p: Option<Rc<RefCell<TreeNode>>>,
        q: Option<Rc<RefCell<TreeNode>>>,
    ) -> bool {
        let mut p_result: Vec<Option<Rc<RefCell<TreeNode>>>> = Vec::new();
        let mut q_result: Vec<Option<Rc<RefCell<TreeNode>>>> = Vec::new();
        Solution::helper(&p, &mut p_result);
        Solution::helper(&q, &mut q_result);
        p_result == q_result
    }

    fn helper(root: &Option<Rc<RefCell<TreeNode>>>, v: &mut Vec<Option<Rc<RefCell<TreeNode>>>>) {
        if let Some(n) = root {
            v.push(Some(n.clone()));
            Solution::helper(&n.borrow().left, v);
            Solution::helper(&n.borrow().right, v);
        } else {
            v.push(None)
        }
    }
}

#[cfg(test)]
mod tests {
    use crate::code::utils::deserialize_to_binary_tree::deserialize_to_BT;

    use super::Solution;

    #[test]
    fn case_1() {
        let p = vec![Some(1), Some(2), Some(3)];
        let p_tree = deserialize_to_BT(p);
        let q = vec![Some(1), Some(2), Some(3)];
        let q_tree = deserialize_to_BT(q);
        let expected = true;
        let actual = Solution::is_same_tree(p_tree, q_tree);

        assert_eq!(expected, actual);
    }

    #[test]
    fn case_2() {
        let p = vec![Some(1), Some(2)];
        let p_tree = deserialize_to_BT(p);
        let q = vec![Some(1), None, Some(3)];
        let q_tree = deserialize_to_BT(q);
        let expected = false;
        let actual = Solution::is_same_tree(p_tree, q_tree);

        assert_eq!(expected, actual);
    }

    #[test]
    fn case_3() {
        let p = vec![Some(1), Some(2), Some(1)];
        let p_tree = deserialize_to_BT(p);
        let q = vec![Some(1), Some(1), Some(2)];
        let q_tree = deserialize_to_BT(q);
        let expected = false;
        let actual = Solution::is_same_tree(p_tree, q_tree);

        assert_eq!(expected, actual);
    }

    #[test]
    fn case_4() {
        let p = vec![Some(1), Some(2), Some(3)];
        let p_tree = deserialize_to_BT(p);
        let q = vec![Some(1), Some(2), Some(3)];
        let q_tree = deserialize_to_BT(q);
        let expected = true;
        let actual = Solution::is_same_tree_2(p_tree, q_tree);

        assert_eq!(expected, actual);
    }

    #[test]
    fn case_5() {
        let p = vec![Some(1), Some(2)];
        let p_tree = deserialize_to_BT(p);
        let q = vec![Some(1), None, Some(3)];
        let q_tree = deserialize_to_BT(q);
        let expected = false;
        let actual = Solution::is_same_tree_2(p_tree, q_tree);

        assert_eq!(expected, actual);
    }

    #[test]
    fn case_6() {
        let p = vec![Some(1), Some(2), Some(1)];
        let p_tree = deserialize_to_BT(p);
        let q = vec![Some(1), Some(1), Some(2)];
        let q_tree = deserialize_to_BT(q);
        let expected = false;
        let actual = Solution::is_same_tree_2(p_tree, q_tree);

        assert_eq!(expected, actual);
    }
}
