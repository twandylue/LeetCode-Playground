struct Solution {}

impl Solution {
    // NOTE:
    // 1. time complexity: O(klogn), space complexity: O(n)
    // 2. double heap
    pub fn find_maximized_capital(k: i32, mut w: i32, profits: Vec<i32>, capital: Vec<i32>) -> i32 {
        use std::cmp::Reverse;
        use std::collections::BinaryHeap;

        let mut min_heap: BinaryHeap<Reverse<(i32, i32)>> = BinaryHeap::new();
        for (pro, cap) in profits
            .into_iter()
            .zip(capital.into_iter())
            .collect::<Vec<(i32, i32)>>()
        {
            min_heap.push(Reverse((cap, pro)));
        }
        let mut max_heap: BinaryHeap<i32> = BinaryHeap::new();
        for _ in 0..k {
            while min_heap
                .peek()
                .filter(|Reverse((min_w, _))| w >= *min_w)
                .is_some()
            {
                if let Some(Reverse((_, pro))) = min_heap.pop() {
                    max_heap.push(pro);
                }
            }
            if let Some(p) = max_heap.pop() {
                w += p;
            } else {
                break;
            }
        }
        w
    }
}

#[cfg(test)]
mod test {
    use super::Solution;

    #[test]
    fn test_find_maximized_capital_case_1() {
        // arrange
        let k: i32 = 2;
        let w: i32 = 0;
        let profits: Vec<i32> = vec![1, 2, 3];
        let capital: Vec<i32> = vec![0, 1, 1];
        let expected: i32 = 4;

        // act
        let actual = Solution::find_maximized_capital(k, w, profits, capital);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn test_find_maximized_capital_case_2() {
        // arrange
        let k: i32 = 3;
        let w: i32 = 0;
        let profits: Vec<i32> = vec![1, 2, 3];
        let capital: Vec<i32> = vec![0, 1, 2];
        let expected: i32 = 6;

        // act
        let actual = Solution::find_maximized_capital(k, w, profits, capital);

        // assert
        assert_eq!(expected, actual);
    }
}
