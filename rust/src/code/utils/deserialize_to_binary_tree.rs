use std::{cell::RefCell, collections::VecDeque, rc::Rc};

use crate::code::models::binary_tree_node::TreeNode;

#[allow(non_snake_case)]
/// Deserialize a vector to a binary tree by BFS
pub fn deserialize_to_BT(vector: Vec<Option<i32>>) -> Option<Rc<RefCell<TreeNode>>> {
    if vector.len() == 0 {
        return None;
    }

    let mut original_queue: VecDeque<Option<Rc<RefCell<TreeNode>>>> = VecDeque::new();
    let mut temp_queue: VecDeque<Option<Rc<RefCell<TreeNode>>>> = VecDeque::new();

    for i in 0..vector.len() {
        match vector[i] {
            Some(val) => {
                let node = Rc::new(RefCell::new(TreeNode::new(val)));
                original_queue.push_back(Some(node));
            }
            None => {
                original_queue.push_back(None);
            }
        }
    }

    if let Some(root) = original_queue.pop_front() {
        temp_queue.push_back(root.clone());
        while !temp_queue.is_empty() {
            if let Some(node) = temp_queue.pop_front() {
                if let Some(n) = node {
                    match original_queue.pop_front() {
                        Some(left) => {
                            n.borrow_mut().left = left.clone();
                            temp_queue.push_back(left.clone());
                        }
                        None => {
                            n.borrow_mut().left = None;
                        }
                    }
                    match original_queue.pop_front() {
                        Some(right) => {
                            n.borrow_mut().right = right.clone();
                            temp_queue.push_back(right.clone());
                        }
                        None => {
                            n.borrow_mut().right = None;
                        }
                    }
                }
            }
        }
        return root;
    }
    return None;
}
