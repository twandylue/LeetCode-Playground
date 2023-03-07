pub struct Solution {}

impl Solution {
    pub fn erase_overlap_intervals(mut intervals: Vec<Vec<i32>>) -> i32 {
        let mut end = i32::MIN;
        let mut count = 0;
        intervals.sort_by_key(|x| x[1]);
        for i in intervals {
            if i[0] >= end {
                end = i[1];
            } else {
                count += 1;
            }
        }

        return count;
    }
}

#[cfg(test)]
mod tests {
    use super::Solution;

    #[test]
    fn case_1() {
        let intervals = vec![vec![1, 2], vec![2, 3], vec![3, 4], vec![1, 3]];
        let expected = 1;
        let actual = Solution::erase_overlap_intervals(intervals);

        assert_eq!(expected, actual);
    }

    #[test]
    fn case_2() {
        let intervals = vec![vec![1, 2], vec![1, 2], vec![1, 2]];
        let expected = 2;
        let actual = Solution::erase_overlap_intervals(intervals);

        assert_eq!(expected, actual);
    }

    #[test]
    fn case_3() {
        let intervals = vec![vec![1, 2], vec![2, 3]];
        let expected = 0;
        let actual = Solution::erase_overlap_intervals(intervals);

        assert_eq!(expected, actual);
    }
}
