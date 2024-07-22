struct Solution;

impl Solution {
    pub fn find_judge(n: i32, trust: Vec<Vec<i32>>) -> i32 {
        use std::collections::HashMap;

        let mut incoming: HashMap<i32, Vec<i32>> = HashMap::new();
        let mut outgoing: HashMap<i32, Vec<i32>> = HashMap::new();
        for i in 1..n + 1 {
            incoming.entry(i).or_insert(Vec::new());
            outgoing.entry(i).or_insert(Vec::new());
        }
        for t in trust {
            let src: i32 = t[0];
            let dst: i32 = t[1];
            incoming.entry(dst).and_modify(|x| x.push(src));
            outgoing.entry(src).and_modify(|x| x.push(dst));
        }
        for i in 1..n + 1 {
            if incoming[&i].len() as i32 == n - 1 && outgoing[&i].len() == 0 {
                return i;
            }
        }
        -1
    }
}

#[cfg(test)]
mod tests {
    use super::Solution;

    #[test]
    fn test_find_judge_case_1() {
        // arrange
        let n: i32 = 2;
        let trust: Vec<Vec<i32>> = vec![vec![1, 2]];
        let expected: i32 = 2;

        // act
        let actual = Solution::find_judge(n, trust);

        // assert
        assert_eq!(actual, expected);
    }

    #[test]
    fn test_find_judge_case_2() {
        // arrange
        let n: i32 = 3;
        let trust: Vec<Vec<i32>> = vec![vec![1, 3], vec![2, 3]];
        let expected: i32 = 3;

        // act
        let actual = Solution::find_judge(n, trust);

        // assert
        assert_eq!(actual, expected);
    }

    #[test]
    fn test_find_judge_case_3() {
        // arrange
        let n: i32 = 3;
        let trust: Vec<Vec<i32>> = vec![vec![1, 3], vec![2, 3], vec![3, 1]];
        let expected: i32 = -1;

        // act
        let actual = Solution::find_judge(n, trust);

        // assert
        assert_eq!(actual, expected);
    }
}
