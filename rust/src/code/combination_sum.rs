pub struct Solution {}

impl Solution {
    pub fn combination_sum(candidates: Vec<i32>, target: i32) -> Vec<Vec<i32>> {
        let mut res: Vec<Vec<i32>> = Vec::new();
        Solution::bfs(0, Vec::<i32>::new(), 0, target, &candidates, &mut res);

        return res;
    }

    fn bfs(
        pos: usize,
        mut subset: Vec<i32>,
        accu: i32,
        target: i32,
        candidates: &Vec<i32>,
        res: &mut Vec<Vec<i32>>,
    ) {
        if accu == target {
            res.push(subset.clone());
            return;
        } else if accu > target || pos > candidates.len() - 1 {
            return;
        }

        for i in pos..candidates.len() {
            subset.push(candidates[i]);
            Self::bfs(
                i,
                subset.clone(),
                accu + candidates[i],
                target,
                candidates,
                res,
            );
            subset.pop();
        }
    }
}

#[cfg(test)]
pub mod test {
    use super::Solution;

    #[test]
    fn combination_sum_case_1() {
        // arragne
        let candidates = vec![2, 3, 5];
        let target = 8;

        // act
        let actual = Solution::combination_sum(candidates, target);
        let expected = vec![vec![2, 2, 2, 2], vec![2, 3, 3], vec![3, 5]];

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn combination_sum_case_2() {
        // arrange
        let candidates = vec![2];
        let target = 1;

        // act
        let actual = Solution::combination_sum(candidates, target);
        let expected: Vec<Vec<i32>> = Vec::new();

        // assert
        assert_eq!(expected, actual);
    }
}
