use std::cell::RefCell;
use std::rc::Rc;

use super::models::binary_tree_node::TreeNode;
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
    use crate::code::utils::deserialize_to_binary_tree::deserialize_to_BT;

    use super::{Codec, TreeNode};
    use std::{cell::RefCell, rc::Rc};

    #[test]
    fn case_1() {
        let strs = deserialize_to_BT(vec![
            Some(1),
            Some(2),
            Some(3),
            None,
            None,
            Some(4),
            Some(5),
        ]);
        let expected = deserialize_to_BT(vec![
            Some(1),
            Some(2),
            Some(3),
            None,
            None,
            Some(4),
            Some(5),
        ]);
        let obj = Codec::new();
        let data: String = obj.serialize(strs);
        let ans: Option<Rc<RefCell<TreeNode>>> = obj.deserialize(data);

        assert_eq!(expected, ans);
    }

    #[test]
    fn case_2() {
        let strs = deserialize_to_BT(vec![]);
        let expected = deserialize_to_BT(vec![]);
        let obj = Codec::new();
        let data: String = obj.serialize(strs);
        let ans: Option<Rc<RefCell<TreeNode>>> = obj.deserialize(data);

        assert_eq!(expected, ans);
    }
}
