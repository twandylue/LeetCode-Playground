struct Solution {}

impl Solution {
    /// NOTE: time complexity O(nlogn)
    pub fn last_stone_weight(stones: Vec<i32>) -> i32 {
        use std::collections::BinaryHeap;

        let mut min_heap = BinaryHeap::from(stones);
        while min_heap.len() > 1 {
            let f: i32 = min_heap.pop().unwrap();
            let s: i32 = min_heap.pop().unwrap();
            min_heap.push(f - s);
        }
        return *min_heap.peek().unwrap();
    }
}

#[cfg(test)]
mod test {
    use super::Solution;

    #[test]
    fn last_stone_weight_case_1() {
        // arrange
        let stones = vec![2, 7, 4, 1, 8, 1];
        let expected = 1;

        // act
        let actual = Solution::last_stone_weight(stones);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn last_stone_weight_case_2() {
        // arrange
        let stones = vec![1];
        let expected = 1;

        // act
        let actual = Solution::last_stone_weight(stones);

        // assert
        assert_eq!(expected, actual);
    }
}
