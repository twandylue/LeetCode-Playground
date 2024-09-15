use std::collections::{HashMap, VecDeque};

struct LockingTree {
    parent: Vec<i32>,
    child: HashMap<i32, Vec<i32>>,
    locked: Vec<Option<i32>>,
}

/**
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl LockingTree {
    fn new(parent: Vec<i32>) -> Self {
        let mut child: HashMap<i32, Vec<i32>> = HashMap::new();
        for i in 0..parent.len() {
            child.entry(i as i32).or_insert(vec![]);
        }
        for i in 1..parent.len() {
            child
                .entry(parent[i] as i32)
                .and_modify(|x| x.push(i as i32));
        }
        let locked: Vec<Option<i32>> = vec![None; parent.len()];

        Self {
            parent: parent,
            child: child,
            locked: locked,
        }
    }

    // NOTE: time complexity: O(1)
    fn lock(&mut self, num: i32, user: i32) -> bool {
        let num: usize = num as usize;
        if self.locked[num].is_some() {
            return false;
        }
        self.locked[num] = Some(user);
        true
    }

    // NOTE: time complexity: O(1)
    fn unlock(&mut self, num: i32, user: i32) -> bool {
        let num: usize = num as usize;
        if let Some(u) = self.locked[num] {
            if u == user {
                self.locked[num] = None;
                return true;
            }
        }
        false
    }

    // NOTE: time complexity: O(n)
    fn upgrade(&mut self, num: i32, user: i32) -> bool {
        let mut i: i32 = num;
        while i != -1 {
            if self.locked[i as usize].is_some() {
                return false;
            }
            i = self.parent[i as usize];
        }
        let mut locked_count: i32 = 0;
        let mut queue: VecDeque<i32> = VecDeque::from([num]);
        while let Some(n) = queue.pop_front() {
            if self.locked[n as usize].is_some() {
                self.locked[n as usize] = None;
                locked_count += 1;
            }
            if let Some(childs) = self.child.get(&n) {
                for child in childs {
                    queue.push_back(*child);
                }
            }
        }
        if locked_count > 0 {
            self.locked[num as usize] = Some(user);
        }
        locked_count > 0
    }
}

#[cfg(test)]
mod tests {
    use super::LockingTree;

    #[test]
    fn test_locking_tree_case_1() {
        let mut lockingTree: LockingTree = LockingTree::new(vec![-1, 0, 0, 1, 1, 2, 2]);
        assert!(lockingTree.lock(2, 2)); // return true because node 2 is unlocked.
                                         // Node 2 will now be locked by user 2.
        assert!(!lockingTree.unlock(2, 3)); // return false because user 3 cannot unlock a node locked by user 2.
        assert!(lockingTree.unlock(2, 2)); // return true because node 2 was previously locked by user 2.
                                           // Node 2 will now be unlocked.
        assert!(lockingTree.lock(4, 5)); // return true because node 4 is unlocked.
                                         // Node 4 will now be locked by user 5.
        assert!(lockingTree.upgrade(0, 1)); // return true because node 0 is unlocked and has at least one locked descendant (node 4).
                                            // Node 0 will now be locked by user 1 and node 4 will now be unlocked.
        assert!(!lockingTree.lock(0, 1)); // return false because node 0 is already locked.
    }
}
