use std::collections::BinaryHeap;

struct Solution {}

impl Solution {
    pub fn last_stone_weight(stones: Vec<i32>) -> i32 {
        let mut heap: BinaryHeap<i32> = BinaryHeap::from(stones);
        while heap.len() > 1 {
            let i = heap.pop().unwrap();
            let j = heap.pop().unwrap();
            if i == j {
                continue;
            } else {
                let remain = i - j;
                heap.push(remain);
            }
        }
        heap.push(0);

        return *heap.peek().unwrap();
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
