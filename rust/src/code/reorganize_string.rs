pub struct Solution {}

impl Solution {
    // NOTE: time complexity O(nlogn), space complexity O(n)
    // 1. Most frequent character should be placed first
    // 2. Use prev to store the previous character and skip it in the next iteration
    pub fn reorganize_string(s: String) -> String {
        use std::collections::{BinaryHeap, HashMap};

        let s: Vec<char> = s.chars().collect();
        let mut counter: HashMap<char, i32> = HashMap::new();
        for c in s {
            counter.entry(c).and_modify(|x| *x += 1).or_insert(1);
        }
        let mut max_heap: BinaryHeap<(i32, char)> = BinaryHeap::new();
        for (c, cnt) in counter.into_iter() {
            max_heap.push((cnt, c));
        }
        let mut result: Vec<char> = Vec::new();
        let mut prev: (i32, char) = (-1, ' ');
        while max_heap.len() > 0 || prev.1 != ' ' {
            if prev.1 != ' ' && max_heap.len() == 0 {
                return "".to_string();
            }
            if let Some((mut cnt, c)) = max_heap.pop() {
                result.push(c);
                cnt -= 1;
                if prev.1 != ' ' {
                    max_heap.push(prev);
                    prev = (-1, ' ');
                }
                if cnt > 0 {
                    prev = (cnt, c);
                }
            }
        }
        result.iter().collect::<String>()
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_get_order_case_1() {
        // arrange
        let s: String = "aab".to_string();
        let expected: String = "aba".to_string();

        // act
        let actual = Solution::reorganize_string(s);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn test_get_order_case_2() {
        // arrange
        let s: String = "aaab".to_string();
        let expected: String = "".to_string();

        // act
        let actual = Solution::reorganize_string(s);

        // assert
        assert_eq!(expected, actual);
    }
}
