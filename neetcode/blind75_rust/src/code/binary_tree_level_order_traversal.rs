use std::cell::RefCell;
use std::collections::VecDeque;
use std::rc::Rc;

use super::models::binary_tree_node::TreeNode;

pub struct Solution {}

impl Solution {
    pub fn level_order_2(root: Option<Rc<RefCell<TreeNode>>>) -> Vec<Vec<i32>> {
        let mut ret: Vec<Vec<i32>> = Vec::new();
        let mut q: VecDeque<Option<Rc<RefCell<TreeNode>>>> = VecDeque::new();
        match root {
            Some(n) => {
                q.push_back(Some(n));
                while q.len() > 0 {
                    let q_len = q.len() as i32;
                    let mut level: Vec<i32> = Vec::new();
                    for _ in 0..q_len {
                        match q.pop_front() {
                            Some(node) => match node {
                                Some(a) => {
                                    level.push(a.borrow().val);
                                    q.push_back(a.borrow().left.clone());
                                    q.push_back(a.borrow().right.clone());
                                }
                                None => (),
                            },
                            None => (),
                        }
                    }

                    if level.len() > 0 {
                        ret.push(level.clone());
                    }
                }
            }
            None => (),
        }

        return ret;
    }

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
    use crate::code::utils::deserialize_to_binary_tree::deserialize_to_BT;

    use super::Solution;

    #[test]
    fn case_1() {
        let root = vec![Some(3), Some(9), Some(20), None, None, Some(15), Some(7)];
        let input = deserialize_to_BT(root);
        let expected = vec![vec![3], vec![9, 20], vec![15, 7]];

        let actual = Solution::level_order(input);

        assert_eq!(expected, actual);
    }

    #[test]
    fn case_2() {
        let root = vec![Some(1)];
        let input = deserialize_to_BT(root);
        let expected = vec![vec![1]];

        let actual = Solution::level_order(input);

        assert_eq!(expected, actual);
    }

    #[test]
    fn case_3() {
        let root = vec![];
        let input = deserialize_to_BT(root);
        let expected: Vec<Vec<i32>> = Vec::new();

        let actual = Solution::level_order(input);

        assert_eq!(expected, actual);
    }

    #[test]
    fn case_4() {
        let root = vec![Some(3), Some(9), Some(20), None, None, Some(15), Some(7)];
        let input = deserialize_to_BT(root);
        let expected = vec![vec![3], vec![9, 20], vec![15, 7]];

        let actual = Solution::level_order_2(input);

        assert_eq!(expected, actual);
    }

    #[test]
    fn case_5() {
        let root = vec![Some(1)];
        let input = deserialize_to_BT(root);
        let expected = vec![vec![1]];

        let actual = Solution::level_order_2(input);

        assert_eq!(expected, actual);
    }

    #[test]
    fn case_6() {
        let root = vec![];
        let input = deserialize_to_BT(root);
        let expected: Vec<Vec<i32>> = Vec::new();

        let actual = Solution::level_order_2(input);

        assert_eq!(expected, actual);
    }
}
