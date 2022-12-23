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
struct Codec {}

/**
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl Codec {
    fn new() -> Self {
        Codec {}
    }

    fn serialize(&self, root: Option<Rc<RefCell<TreeNode>>>) -> String {
        let mut ret = String::new();
        Codec::serialize_helper(root, &mut ret);
        ret
    }

    fn serialize_helper(node: Option<Rc<RefCell<TreeNode>>>, s: &mut String) {
        if let Some(n) = node {
            s.push_str(&n.borrow().val.to_string());
            s.push_str(",");
            Codec::serialize_helper(n.borrow().left.clone(), s);
            Codec::serialize_helper(n.borrow().right.clone(), s);
        } else {
            s.push_str("N");
            s.push_str(",");
        }
    }

    fn deserialize(&self, data: String) -> Option<Rc<RefCell<TreeNode>>> {
        let w = data.split(",").collect::<Vec<&str>>();
        let mut i: usize = 0;
        Codec::deserialize_helper(&mut i, &w)
    }

    fn deserialize_helper(index: &mut usize, w: &Vec<&str>) -> Option<Rc<RefCell<TreeNode>>> {
        if w[*index] == "N" {
            *index += 1;
            return None;
        } else {
            let node = Rc::new(RefCell::new(TreeNode::new(
                w[*index].parse::<i32>().unwrap(),
            )));
            *index += 1;
            node.borrow_mut().left = Codec::deserialize_helper(index, w);
            node.borrow_mut().right = Codec::deserialize_helper(index, w);
            return Some(node);
        }
    }
}

/**
 * Your Codec object will be instantiated and called as such:
 * let obj = Codec::new();
 * let data: String = obj.serialize(strs);
 * let ans: Option<Rc<RefCell<TreeNode>>> = obj.deserialize(data);
 */

#[cfg(test)]
mod tests {
    use super::{Codec, TreeNode};
    use std::{cell::RefCell, rc::Rc};

    #[test]
    fn case_1() {
        let strs = self::convert_to_tree_bfs(
            &vec![Some(1), Some(2), Some(3), None, None, Some(4), Some(5)],
            0,
        );
        let expected = self::convert_to_tree_bfs(
            &vec![Some(1), Some(2), Some(3), None, None, Some(4), Some(5)],
            0,
        );
        let obj = Codec::new();
        let data: String = obj.serialize(strs);
        let ans: Option<Rc<RefCell<TreeNode>>> = obj.deserialize(data);

        assert_eq!(expected, ans);
    }

    #[test]
    fn case_2() {
        let strs = self::convert_to_tree_bfs(&vec![], 0);
        let expected = self::convert_to_tree_bfs(&vec![], 0);
        let obj = Codec::new();
        let data: String = obj.serialize(strs);
        let ans: Option<Rc<RefCell<TreeNode>>> = obj.deserialize(data);

        assert_eq!(expected, ans);
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
