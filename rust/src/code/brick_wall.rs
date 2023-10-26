use std::cmp;
use std::collections::HashMap;

struct Solution {}
impl Solution {
    pub fn least_bricks(wall: Vec<Vec<i32>>) -> i32 {
        let mut max_pass_count: usize = 0;
        let mut wallMap: HashMap<i32, i32> = HashMap::new();
        let mut width = 0;
        for i in 0..wall.len() {
            let mut accu: i32 = 0;
            for j in 0..wall[i].len() {
                accu += wall[i][j];
                wallMap.entry(accu).and_modify(|x| *x += 1).or_insert(1);
            }
            width = accu;
        }

        for (k, v) in wallMap {
            if k == width {
                continue;
            }
            max_pass_count = cmp::max(max_pass_count, v as usize);
        }

        return (wall.len() - max_pass_count) as i32;
    }
}

#[cfg(test)]
mod tests {
    use super::*;
    #[test]
    fn least_bricks_case_1() {
        // arrange
        let wall: Vec<Vec<i32>> = vec![
            vec![1, 2, 2, 1],
            vec![3, 1, 2],
            vec![1, 3, 2],
            vec![2, 4],
            vec![3, 1, 2],
            vec![1, 3, 1, 1],
        ];
        let expected: i32 = 2;

        // act
        let actual = Solution::least_bricks(wall);

        // assert
        assert_eq!(expected, actual);
    }
}
