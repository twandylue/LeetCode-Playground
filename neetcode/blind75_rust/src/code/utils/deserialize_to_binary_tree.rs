use std::{cell::RefCell, collections::VecDeque, rc::Rc};

use crate::code::tree::binary_tree_node::TreeNode;

pub fn deserialize_to_BT(vector: Vec<Option<i32>>) -> Option<Rc<RefCell<TreeNode>>> {
    if vector.len() == 0 {
        return None;
    }

    let mut index: usize = 0;
    let mut queue: VecDeque<Option<Rc<RefCell<TreeNode>>>> = VecDeque::new();

    if let Some(val) = vector[index] {
        let mut root = Some(Rc::new(RefCell::new(TreeNode::new(val))));
        queue.push_back(root);
        index += 1;
        while queue.len() > 0 {
            // let mut node = queue.pop_front().unwrap();
            if let Some(n) = queue.pop_front().unwrap() {
                match vector[index] {
                    Some(v) => {
                        n.borrow_mut().left = Some(Rc::new(RefCell::new(TreeNode::new(v))));
                        index += 1;
                        n.borrow_mut().right = Some(Rc::new(RefCell::new(TreeNode::new(v))));
                        index += 1;
                    }
                    None => {
                        todo!()
                    }
                }
            }
        }

        return root.clone();
    } else {
        return None;
    }
}
