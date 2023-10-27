use rand::seq::SliceRandom;
use std::collections::HashMap;

type VALUE = i32;
type INDEX = usize;

struct RandomizedSet {
    pub map: HashMap<VALUE, INDEX>,
    pub values: Vec<VALUE>,
}

// `&self` means the method takes an immutable reference.
// If you need a mutable reference, change it to `&mut self` instead.
impl RandomizedSet {
    fn new() -> Self {
        RandomizedSet {
            map: HashMap::new(),
            values: Vec::new(),
        }
    }

    fn insert(&mut self, val: i32) -> bool {
        if self.map.contains_key(&val) {
            return false;
        }
        self.values.push(val);
        let index: usize = self.values.len() - 1;
        match self.map.insert(val, index) {
            Some(_) => false,
            None => true,
        }
    }

    // [ 1, 2, 5, 6]
    fn remove(&mut self, val: i32) -> bool {
        match self.map.get(&val) {
            Some(&index) => {
                let last_index: INDEX = self.values.len() - 1;
                let last_val: VALUE = self.values[last_index];
                self.values[last_index] = val;
                self.values[index] = last_val;
                if let Some(x) = self.map.get_mut(&last_val) {
                    *x = index;
                }
                self.values.pop().unwrap();
                self.map.remove(&val).unwrap();

                return true;
            }
            None => false,
        }
    }

    fn get_random(&self) -> i32 {
        *self.values.choose(&mut rand::thread_rng()).unwrap()
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn randomizedset_case_1() {
        let mut rand = RandomizedSet::new();
        assert!(rand.insert(1));
        assert!(!rand.remove(2));
        assert!(rand.insert(2));
        let _r1: i32 = rand.get_random();
        assert!(rand.remove(1));
        assert!(!rand.insert(2));
        let r2: i32 = rand.get_random();

        assert_eq!(2, r2);
    }
}
