pub struct Solution {}

impl Solution {
    pub fn merge(mut intervals: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        intervals.sort_by_key(|x| x[1]);
        let mut stack: Vec<Vec<i32>> = Vec::new();
        for i in intervals {
            let mut l = i[0];
            let r = i[1];
            while stack.len() > 0 && l <= stack.last().unwrap()[1] {
                l = std::cmp::min(l, stack.last().unwrap()[0]);
                stack.pop();
            }

            stack.push(Vec::from([l, r]));
        }

        return stack;
    }
}

#[cfg(test)]
mod tests {
    use super::Solution;

    #[test]
    fn case_1() {
        let intervals = vec![vec![1, 3], vec![2, 6], vec![8, 10], vec![15, 18]];
        let expected = vec![vec![1, 6], vec![8, 10], vec![15, 18]];
        let actual = Solution::merge(intervals);

        assert_eq!(expected, actual);
    }

    #[test]
    fn case_2() {
        let intervals = vec![vec![1, 4], vec![4, 5]];
        let expected = vec![vec![1, 5]];
        let actual = Solution::merge(intervals);

        assert_eq!(expected, actual);
    }

    #[test]
    fn case_3() {
        let intervals = vec![vec![1, 4], vec![0, 1]];
        let expected = vec![vec![0, 4]];
        let actual = Solution::merge(intervals);

        assert_eq!(expected, actual);
    }

    #[test]
    fn case_4() {
        let intervals = vec![vec![1, 4], vec![2, 3]];
        let expected = vec![vec![1, 4]];
        let actual = Solution::merge(intervals);

        assert_eq!(expected, actual);
    }
}
