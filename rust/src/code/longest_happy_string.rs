struct Solution {}

impl Solution {
    // NOTE:
    // Time complexity: O(n), space complexity: O(n), where n is the sum of a, b, and c.
    // Since the size of the heap is at most 3, the time complexity is O(1) for each operation.
    // So, the time complexity is O(n) in total, where n is the sum of a, b, and c.
    pub fn longest_diverse_string(a: i32, b: i32, c: i32) -> String {
        use std::collections::BinaryHeap;

        let mut max_heap: BinaryHeap<(i32, char)> = BinaryHeap::new();
        let mut result: Vec<char> = Vec::new();
        for (count, c) in vec![(a, 'a'), (b, 'b'), (c, 'c')] {
            if count > 0 {
                max_heap.push((count, c));
            }
        }

        while let Some((mut count, c)) = max_heap.pop() {
            let result_size = result.len();
            if result_size > 1 && c == result[result_size - 1] && c == result[result_size - 2] {
                if let Some((mut count_2, c_2)) = max_heap.pop() {
                    result.push(c_2);
                    count_2 -= 1;
                    if count_2 > 0 {
                        max_heap.push((count_2, c_2));
                    }
                } else {
                    break;
                }
            } else {
                result.push(c);
                count -= 1;
            }
            if count > 0 {
                max_heap.push((count, c));
            }
        }

        result.iter().collect::<String>()
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_longest_diverse_string_case_1() {
        // arrange
        let a: i32 = 1;
        let b: i32 = 1;
        let c: i32 = 7;
        let expected: String = "ccbccacc".to_string();

        // act
        let actual = Solution::longest_diverse_string(a, b, c);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn test_longest_diverse_string_case_2() {
        // arrange
        let a: i32 = 7;
        let b: i32 = 1;
        let c: i32 = 0;
        let expected: String = "aabaa".to_string();

        // act
        let actual = Solution::longest_diverse_string(a, b, c);

        // assert
        assert_eq!(expected, actual);
    }
}
