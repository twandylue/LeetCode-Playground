use std::collections::VecDeque;

struct Solution {}

impl Solution {
    pub fn max_sliding_window(nums: Vec<i32>, k: i32) -> Vec<i32> {
        let mut results = Vec::<i32>::new();
        // NOTE: store index
        let mut deq = VecDeque::<usize>::new();

        let mut l = 0;
        for r in 0..nums.len() {
            while let Some(&v) = deq.iter().last() {
                if nums[r] > nums[v] {
                    let _ = deq.pop_back().unwrap();
                    continue;
                }
                break;
            }

            deq.push_back(r);

            if let Some(&i) = deq.front() {
                if l > i {
                    let _ = deq.pop_front().unwrap();
                }
            }

            if r + 1 >= (k as usize) {
                if let Some(&i) = deq.front() {
                    results.push(nums[i]);
                }
                l += 1;
            }
        }

        results
    }
}

#[cfg(test)]
mod tests {
    use super::Solution;

    #[test]
    fn sliding_window_maximum_case_1() {
        // arrange
        let nums = vec![1, 3, -1, -3, 5, 3, 6, 7];
        let k = 3;
        let expected = vec![3, 3, 5, 5, 6, 7];

        // act
        let actual = Solution::max_sliding_window(nums, k);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn sliding_window_maximum_case_2() {
        // arrange
        let nums = vec![1];
        let k = 1;
        let expected = vec![1];

        // act
        let actual = Solution::max_sliding_window(nums, k);

        // assert
        assert_eq!(expected, actual);
    }
}
