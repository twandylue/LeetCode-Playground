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
        let time_map = Self {
            store: HashMap::new(),
        };

        time_map
    }

    fn set(&mut self, key: String, value: String, timestamp: i32) {
        self.store
            .entry(key)
            .and_modify(|l| l.push((value.clone(), timestamp)))
            .or_insert(vec![(value, timestamp)]);
    }

    fn get(&self, key: String, timestamp: i32) -> String {
        let mut result = String::new();
        if let Some(list) = self.store.get(&key) {
            let mut l = 0;
            let mut r = list.len() - 1;
            while l <= r {
                let mid = (l + r) / 2;
                if timestamp == list[mid].1 {
                    result = list[mid].0.clone();
                    return result;
                } else if timestamp > list[mid].1 {
                    result = list[mid].0.clone();
                    l = mid + 1;
                } else {
                    if mid > 0 {
                        r = mid - 1;
                    } else {
                        break;
                    }
                }
            }
        }

        return result;
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
