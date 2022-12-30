use std::cell::RefCell;
use std::cmp;
use std::rc::Rc;

use super::model::binary_tree_node::TreeNode;

pub struct Solution {}

impl Solution {
    pub fn lowest_common_ancestor(
        root: Option<Rc<RefCell<TreeNode>>>,
        p: Option<Rc<RefCell<TreeNode>>>,
        q: Option<Rc<RefCell<TreeNode>>>,
    ) -> Option<Rc<RefCell<TreeNode>>> {
        match (root, p, q) {
            (Some(a), Some(r), Some(l)) => {
                if a.borrow().val > cmp::max(r.borrow().val, l.borrow().val) {
                    return Solution::lowest_common_ancestor(
                        a.borrow().left.clone(),
                        Some(r.clone()),
                        Some(l.clone()),
                    );
                } else if a.borrow().val < cmp::min(r.borrow().val, l.borrow().val) {
                    return Solution::lowest_common_ancestor(
                        a.borrow().right.clone(),
                        Some(r.clone()),
                        Some(l.clone()),
                    );
                } else {
                    Some(a.clone())
                }
            }
            (_, _, _) => None,
        }
    }
}

#[cfg(test)]
mod tests {
    use crate::code::utils::deserialize_to_binary_tree::deserialize_to_BT;

    use super::{Solution, TreeNode};
    use std::{cell::RefCell, rc::Rc};

    #[test]
    fn case_1() {
        let root = vec![
            Some(6),
            Some(2),
            Some(8),
            Some(0),
            Some(4),
            Some(7),
            Some(9),
            None,
            None,
            Some(3),
            Some(5),
        ];

        let input = deserialize_to_BT(root);
        let p = Some(Rc::new(RefCell::new(TreeNode {
            val: 2,
            left: None,
            right: None,
        })));
        let q = Some(Rc::new(RefCell::new(TreeNode {
            val: 8,
            left: None,
            right: None,
        })));
        let expected = 6;

        let actual = Solution::lowest_common_ancestor(input, p, q);

        assert_eq!(expected, actual.unwrap().borrow().val);
    }

    #[test]
    fn case_2() {
        let root = vec![
            Some(6),
            Some(2),
            Some(8),
            Some(0),
            Some(4),
            Some(7),
            Some(9),
            None,
            None,
            Some(3),
            Some(5),
        ];

        let input = deserialize_to_BT(root);
        let p = Some(Rc::new(RefCell::new(TreeNode {
            val: 2,
            left: None,
            right: None,
        })));
        let q = Some(Rc::new(RefCell::new(TreeNode {
            val: 4,
            left: None,
            right: None,
        })));
        let expected = 2;

        let actual = Solution::lowest_common_ancestor(input, p, q);

        assert_eq!(expected, actual.unwrap().borrow().val);
    }

    #[test]
    fn case_3() {
        let root = vec![Some(2), Some(1)];

        let input = deserialize_to_BT(root);
        let p = Some(Rc::new(RefCell::new(TreeNode {
            val: 2,
            left: None,
            right: None,
        })));
        let q = Some(Rc::new(RefCell::new(TreeNode {
            val: 1,
            left: None,
            right: None,
        })));
        let expected = 2;

        let actual = Solution::lowest_common_ancestor(input, p, q);

        assert_eq!(expected, actual.unwrap().borrow().val);
    }

    // fn convert_to_tree_bfs(input: &Vec<Option<i32>>, index: i32) -> Option<Rc<RefCell<TreeNode>>> {
    //     if index > input.len() as i32 - 1 {
    //         return None;
    //     }
    //     if let Some(n) = input[index as usize] {
    //         let mut node = TreeNode::new(n);
    //         node.left = self::convert_to_tree_bfs(input, 2 * index + 1);
    //         node.right = self::convert_to_tree_bfs(input, 2 * index + 2);
    //         Some(Rc::new(RefCell::new(node)))
    //     } else {
    //         None
    //     }
    // }
}
