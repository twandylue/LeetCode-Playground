use std::cmp::Reverse;
use std::collections::{BinaryHeap, HashMap};

struct Solution {}

impl Solution {
    // NOTE: time complexity O(nlogn)
    pub fn is_n_straight_hand(hand: Vec<i32>, group_size: i32) -> bool {
        if hand.len() % group_size as usize != 0 {
            return false;
        }

        let mut count: HashMap<i32, i32> = HashMap::new();
        for i in hand {
            count.entry(i).and_modify(|x| *x += 1).or_insert(1);
        }

        let mut min_heap: BinaryHeap<Reverse<i32>> = BinaryHeap::new();
        for k in count.keys() {
            min_heap.push(Reverse(*k));
        }

        while let Some(Reverse(first)) = min_heap.peek() {
            for number in *first..(*first + group_size) {
                if let Some(v) = count.get_mut(&number) {
                    *v -= 1;
                    if *v == 0 {
                        if let Some(Reverse(f)) = min_heap.peek() {
                            if number != *f {
                                return false;
                            }
                            min_heap.pop();
                        }
                    }
                } else {
                    return false;
                }
            }
        }

        true
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_is_n_straight_hand_case_1() {
        // arrange
        let hand = vec![1, 2, 3, 6, 2, 3, 4, 7, 8];
        let group_size = 3;
        let expected = true;

        // act
        let actual = Solution::is_n_straight_hand(hand, group_size);

        // assert
        assert_eq!(actual, expected);
    }

    #[test]
    fn test_is_n_straight_hand_case_2() {
        // arrange
        let hand = vec![1, 2, 3, 4, 5];
        let group_size = 4;
        let expected = false;

        // act
        let actual = Solution::is_n_straight_hand(hand, group_size);

        // assert
        assert_eq!(actual, expected);
    }
}
