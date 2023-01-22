pub struct Solution {}

impl Solution {
    pub fn combination_sum(candidates: Vec<i32>, target: i32) -> Vec<Vec<i32>> {
        let mut res: Vec<Vec<i32>> = Vec::new();
        Solution::bfs(0, Vec::<i32>::new(), 0, target, candidates, &mut res);

        return res;
    }

    fn bfs(
        i: usize,
        mut cur: Vec<i32>,
        total: i32,
        target: i32,
        candidates: Vec<i32>,
        res: &mut Vec<Vec<i32>>,
    ) {
        if total == target {
            res.push(cur);
            return;
        } else if total > target || i >= candidates.len() {
            return;
        }

        cur.push(candidates[i]);
        Solution::bfs(
            i,
            cur.clone(),
            total + candidates[i],
            target,
            candidates.clone(),
            res,
        );
        cur.pop();
        Solution::bfs(i + 1, cur, total, target, candidates, res);

        return;
    }
}

#[cfg(test)]
pub mod test {
    use super::Solution;

    #[test]
    fn case_1() {
        let candidates = vec![2, 3, 5];
        let target = 8;
        let actual = Solution::combination_sum(candidates, target);
        let expected = vec![vec![2, 2, 2, 2], vec![2, 3, 3], vec![3, 5]];
        assert_eq!(expected, actual);
    }

    #[test]
    fn case_2() {
        let candidates = vec![2];
        let target = 1;
        let actual = Solution::combination_sum(candidates, target);
        let expected: Vec<Vec<i32>> = Vec::new();
        assert_eq!(expected, actual);
    }
}
