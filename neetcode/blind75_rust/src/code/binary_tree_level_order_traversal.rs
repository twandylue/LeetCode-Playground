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
    pub fn level_order(root: Option<Rc<RefCell<TreeNode>>>) -> Vec<Vec<i32>> {
        let mut ret: Vec<Vec<i32>> = Vec::new();

        Solution::BFS(root, 0, &mut ret);
        return ret;
    }

    fn BFS(r: Option<Rc<RefCell<TreeNode>>>, d: i32, v: &mut Vec<Vec<i32>>) {
        match r {
            Some(n) => {
                while v.len() <= d as usize {
                    v.push(Vec::new());
                }
                v[d as usize].push(n.borrow().val as i32);
                Solution::BFS(n.borrow().left.clone(), d + 1, v);
                Solution::BFS(n.borrow().right.clone(), d + 1, v);
            }
            _ => (),
        }
    }
}

#[cfg(test)]
mod tests {
    use super::{Solution, TreeNode};
    use std::{cell::RefCell, rc::Rc};

    #[test]
    fn case_1() {
        let root = vec![Some(3), Some(9), Some(20), None, None, Some(15), Some(7)];
        let input = self::convert_to_tree_bfs(&root, 0);
        let expected = vec![vec![3], vec![9, 20], vec![15, 7]];

        let actual = Solution::level_order(input);

        assert_eq!(expected, actual);
    }

    #[test]
    fn case_2() {
        let root = vec![Some(1)];
        let input = self::convert_to_tree_bfs(&root, 0);
        let expected = vec![vec![1]];

        let actual = Solution::level_order(input);

        assert_eq!(expected, actual);
    }

    #[test]
    fn case_3() {
        let root = vec![];
        let input = self::convert_to_tree_bfs(&root, 0);
        let expected: Vec<Vec<i32>> = Vec::new();

        let actual = Solution::level_order(input);

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
