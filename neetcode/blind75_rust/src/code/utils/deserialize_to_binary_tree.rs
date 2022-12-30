use std::{cell::RefCell, collections::VecDeque, rc::Rc};

use crate::code::tree::binary_tree_node::TreeNode;

pub fn deserialize_to_BT(vector: Vec<Option<i32>>) -> Option<Rc<RefCell<TreeNode>>> {
    if vector.len() == 0 {
        return None;
    }

    println!("{:?}", vector);

    let nodes: Vec<Option<Rc<RefCell<TreeNode>>>> = vector
        .into_iter()
        .map(|x| match x {
            Some(val) => Some(Rc::new(RefCell::new(TreeNode::new(val)))),
            None => None,
        })
        .collect();

    let mut index: usize = 0;
    let mut queue: VecDeque<Rc<Option<Rc<RefCell<TreeNode>>>>> = VecDeque::new();
    let root = Rc::new(nodes[index].clone());
    let head = Rc::clone(&root);
    index += 1;
    queue.push_back(root);
    while queue.len() > 0 {
        if let Some(n) = &*(queue.pop_front()).unwrap() {
            if index == nodes.len() {
                break;
            }
            n.borrow_mut().left = nodes[index].clone();
            index += 1;
            if index == nodes.len() {
                break;
            }
            n.borrow_mut().right = nodes[index].clone();
            index += 1;

            if n.borrow().left != None {
                queue.push_back(Rc::new(n.borrow_mut().left.clone()));
            }

            if n.borrow().right != None {
                queue.push_back(Rc::new(n.borrow_mut().right.clone()));
            }
        }
    }

    return (*head).clone();
}
