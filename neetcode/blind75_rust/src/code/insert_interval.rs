pub struct Solution {}

impl Solution {
    pub fn insert(intervals: Vec<Vec<i32>>, mut new_interval: Vec<i32>) -> Vec<Vec<i32>> {
        let mut res: Vec<Vec<i32>> = Vec::new();
        for i in 0..intervals.len() {
            if new_interval[1] < intervals[i][0] {
                res.push(new_interval.clone());
                res.append(&mut intervals[i..].to_vec());
                return res;
            } else if new_interval[0] > intervals[i][1] {
                res.push(intervals[i].clone());
            } else {
                new_interval = Vec::from([
                    std::cmp::min(new_interval[0], intervals[i][0]),
                    std::cmp::max(new_interval[1], intervals[i][1]),
                ]);
            }
        }

        res.push(new_interval);
        return res;
    }
}

#[cfg(test)]
mod tests {
    use super::Solution;

    #[test]
    fn case_1() {
        let intervals = vec![vec![1, 3], vec![6, 9]];
        let new_interval = vec![2, 5];
        let expected = vec![vec![1, 5], vec![6, 9]];
        let actual = Solution::insert(intervals, new_interval);

        assert_eq!(expected, actual);
    }

    #[test]
    fn case_2() {
        let intervals = vec![
            vec![1, 2],
            vec![3, 5],
            vec![6, 7],
            vec![8, 10],
            vec![12, 16],
        ];
        let new_interval = vec![4, 8];
        let expected = vec![vec![1, 2], vec![3, 10], vec![12, 16]];
        let actual = Solution::insert(intervals, new_interval);

        assert_eq!(expected, actual);
    }
}
