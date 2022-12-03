// Definition for a binary tree node.
#[derive(Debug, PartialEq, Eq)]
pub struct TreeNode {
    pub val: i32,
    pub left: Option<Rc<RefCell<TreeNode>>>,
    pub right: Option<Rc<RefCell<TreeNode>>>,
}

impl TreeNode {
    #[inline]
    pub fn new(val: i32) -> Self {
        TreeNode {
            val,
            left: None,
            right: None,
        }
    }
}

use std::cell::RefCell;
use std::rc::Rc;

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
    use super::{Solution, TreeNode};
    use std::{cell::RefCell, rc::Rc};

    #[test]
    fn case_1() {
        let p = vec![Some(1), Some(2), Some(3)];
        let p_tree = self::convert_to_tree_bfs(&p, 0);
        let q = vec![Some(1), Some(2), Some(3)];
        let q_tree = self::convert_to_tree_bfs(&q, 0);
        let expected = true;
        let actual = Solution::is_same_tree(p_tree, q_tree);

        assert_eq!(expected, actual);
    }

    #[test]
    fn case_2() {
        let p = vec![Some(1), Some(2)];
        let p_tree = self::convert_to_tree_bfs(&p, 0);
        let q = vec![Some(1), None, Some(3)];
        let q_tree = self::convert_to_tree_bfs(&q, 0);
        let expected = false;
        let actual = Solution::is_same_tree(p_tree, q_tree);

        assert_eq!(expected, actual);
    }

    #[test]
    fn case_3() {
        let p = vec![Some(1), Some(2), Some(1)];
        let p_tree = self::convert_to_tree_bfs(&p, 0);
        let q = vec![Some(1), Some(1), Some(2)];
        let q_tree = self::convert_to_tree_bfs(&q, 0);
        let expected = false;
        let actual = Solution::is_same_tree(p_tree, q_tree);

        assert_eq!(expected, actual);
    }

    #[test]
    fn case_4() {
        let p = vec![Some(1), Some(2), Some(3)];
        let p_tree = self::convert_to_tree_bfs(&p, 0);
        let q = vec![Some(1), Some(2), Some(3)];
        let q_tree = self::convert_to_tree_bfs(&q, 0);
        let expected = true;
        let actual = Solution::is_same_tree_2(p_tree, q_tree);

        assert_eq!(expected, actual);
    }

    #[test]
    fn case_5() {
        let p = vec![Some(1), Some(2)];
        let p_tree = self::convert_to_tree_bfs(&p, 0);
        let q = vec![Some(1), None, Some(3)];
        let q_tree = self::convert_to_tree_bfs(&q, 0);
        let expected = false;
        let actual = Solution::is_same_tree_2(p_tree, q_tree);

        assert_eq!(expected, actual);
    }

    #[test]
    fn case_6() {
        let p = vec![Some(1), Some(2), Some(1)];
        let p_tree = self::convert_to_tree_bfs(&p, 0);
        let q = vec![Some(1), Some(1), Some(2)];
        let q_tree = self::convert_to_tree_bfs(&q, 0);
        let expected = false;
        let actual = Solution::is_same_tree_2(p_tree, q_tree);

        assert_eq!(expected, actual);
    }

    fn convert_to_tree_bfs(input: &Vec<Option<i32>>, index: i32) -> Option<Rc<RefCell<TreeNode>>> {
        if index > input.len() as i32 - 1 {
            return None;
        }
        if let Some(n) = input[index as usize] {
            let mut node = TreeNode::new(n);
            node.left = self::convert_to_tree_bfs(input, 2 * index + 1);
            node.right = self::convert_to_tree_bfs(input, 2 * index + 2);
            Some(Rc::new(RefCell::new(node)))
        } else {
            None
        }
    }
}
