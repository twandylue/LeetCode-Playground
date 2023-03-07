use std::{
    cell::RefCell,
    collections::HashMap,
    rc::{Rc, Weak},
};

struct ListNode {
    prev: Option<Weak<RefCell<ListNode>>>,
    next: Option<Rc<RefCell<ListNode>>>,
    key: i32,
    value: i32,
}

impl ListNode {
    pub fn new(key: i32, value: i32) -> Self {
        ListNode {
            prev: None,
            next: None,
            key,
            value,
        }
    }

    fn pop(node: Rc<RefCell<ListNode>>) -> Rc<RefCell<ListNode>> {
        match (node.borrow().next.is_some(), node.borrow().prev.is_some()) {
            (true, true) => {
                let next = Rc::clone(node.borrow().next.as_ref().unwrap());
                let prev = Rc::clone(&node.borrow().prev.as_ref().unwrap().upgrade().unwrap());
                next.borrow_mut().prev = Some(Rc::downgrade(&prev));
                prev.borrow_mut().next = Some(Rc::clone(&next));
            }
            (true, false) => {
                node.borrow_mut().prev = None;
            }
            (false, true) => {
                node.borrow_mut().next = None;
            }
            _ => (),
        }

        node
    }
}

struct LRUCache {
    map: HashMap<i32, Option<Rc<RefCell<ListNode>>>>,
    head: Rc<RefCell<ListNode>>,
    tail: Rc<RefCell<ListNode>>,
    capacity: usize,
}

/**
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl LRUCache {
    fn new(capacity: i32) -> Self {
        // head and tail are markers and thus would not change, like a dummy head.
        let head = Rc::new(RefCell::new(ListNode::new(0, 0)));
        let tail = Rc::new(RefCell::new(ListNode::new(0, 0)));
        head.borrow_mut().next = Some(Rc::clone(&tail));
        tail.borrow_mut().prev = Some(Rc::downgrade(&head));

        LRUCache {
            map: HashMap::new(),
            head,
            tail,
            capacity: capacity as usize,
        }
    }

    fn get(&mut self, key: i32) -> i32 {
        match self.map.get(&key) {
            Some(value) => {
                if let Some(n) = value {
                    let node = ListNode::pop(Rc::clone(n));
                    let result = node.borrow().value;
                    Self::insert_after_head(self, node);

                    return result;
                } else {
                    -1
                }
            }
            None => -1,
        }
    }

    fn put(&mut self, key: i32, value: i32) {
        if let Some(v) = self.map.get(&key) {
            let node = v.as_ref().unwrap();
            let node = ListNode::pop(Rc::clone(node));
            node.borrow_mut().value = value;
            Self::insert_after_head(self, node);
        } else {
            if self.map.len() >= self.capacity {
                let del_node = self.tail.borrow().prev.as_ref().unwrap().upgrade().unwrap();
                let del_node = ListNode::pop(del_node);
                self.map.remove(&del_node.borrow().key);
            }

            let new_node = Rc::new(RefCell::new(ListNode::new(key, value)));
            self.map.insert(key, Some(Rc::clone(&new_node)));
            Self::insert_after_head(self, new_node);
        }
    }

    fn insert_after_head(&self, node: Rc<RefCell<ListNode>>) {
        let next = self.head.borrow_mut().next.take();
        next.as_ref().unwrap().borrow_mut().prev = Some(Rc::downgrade(&node));
        node.borrow_mut().next = next;
        node.borrow_mut().prev = Some(Rc::downgrade(&self.head));

        self.head.borrow_mut().next = Some(node);
    }
}

/**
 * Your LRUCache object will be instantiated and called as such:
 * let obj = LRUCache::new(capacity);
 * let ret_1: i32 = obj.get(key);
 * obj.put(key, value);
 */
#[cfg(test)]
mod tests {
    use super::LRUCache;

    #[test]
    fn case_1() {
        // arrange
        let mut cache = LRUCache::new(2);

        // act
        cache.put(1, 1); // cache is {1=1}
        cache.put(2, 2); // cache is {1=1, 2=2}
        let actual1 = cache.get(1); // return 1
        cache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
        let actual2 = cache.get(2); // returns -1 (not found)
        cache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
        let actual3 = cache.get(1); // return -1 (not found)
        let actual4 = cache.get(3); // return 3
        let actual5 = cache.get(4); // return 4

        // assert
        assert_eq!(actual1, 1);
        assert_eq!(actual2, -1);
        assert_eq!(actual3, -1);
        assert_eq!(actual4, 3);
        assert_eq!(actual5, 4);
    }
}
