use std::collections::HashMap;

struct TimeMap {
    store: HashMap<String, Vec<(String, i32)>>,
}

/**
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl TimeMap {
    fn new() -> Self {
        Self {
            store: HashMap::new(),
        }
    }

    fn set(&mut self, key: String, value: String, timestamp: i32) {
        self.store
            .entry(key)
            .and_modify(|l| l.push((value.clone(), timestamp)))
            .or_insert(vec![(value, timestamp)]);
    }

    fn get(&self, key: String, timestamp: i32) -> String {
        if let Some(list) = self.store.get(&key) {
            let pos: i32 = Self::binary_search(&list, timestamp);
            if pos == -1 {
                return String::new();
            }
            return list[pos as usize].0.clone();
        }

        String::new()
    }

    fn binary_search(values: &Vec<(String, i32)>, time: i32) -> i32 {
        let mut result: i32 = -1;
        let mut l: usize = 0;
        let mut r: usize = values.len() - 1;
        while l <= r {
            let mid: usize = (l + r) / 2;
            if values[mid].1 == time {
                return mid as i32;
            }
            if values[mid].1 < time {
                l = mid + 1;
                result = mid as i32;
            } else {
                if mid.checked_sub(1).is_none() {
                    break;
                }
                r = mid - 1;
            }
        }

        result
    }
}

/**
 * Your TimeMap object will be instantiated and called as such:
 * let obj = TimeMap::new();
 * obj.set(key, value, timestamp);
 * let ret_2: String = obj.get(key, timestamp);
 */
#[cfg(test)]
mod test {
    use super::TimeMap;

    #[test]
    fn time_based_key_value_store_case_1() {
        let mut store = TimeMap::new();
        store.set("foo".to_string(), "bar".to_string(), 1);
        assert_eq!(store.get("foo".to_string(), 1), "bar".to_string());
        assert_eq!(store.get("foo".to_string(), 3), "bar".to_string());
        store.set("foo".to_string(), "bar2".to_string(), 4);
        assert_eq!(store.get("foo".to_string(), 4), "bar2".to_string());
        assert_eq!(store.get("foo".to_string(), 5), "bar2".to_string());
    }

    #[test]
    fn time_based_key_value_store_case_2() {
        let mut store = TimeMap::new();
        store.set("love".to_string(), "high".to_string(), 10);
        store.set("love".to_string(), "low".to_string(), 20);
        assert_eq!(store.get("love".to_string(), 5), "".to_string());
        assert_eq!(store.get("love".to_string(), 10), "high".to_string());
        assert_eq!(store.get("love".to_string(), 15), "high".to_string());
        assert_eq!(store.get("love".to_string(), 20), "low".to_string());
        assert_eq!(store.get("love".to_string(), 25), "low".to_string());
    }
}
