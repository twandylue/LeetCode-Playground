use std::cmp::max;
use std::collections::{HashMap, HashSet};

struct Solution;

impl Solution {
    // NOTE: time complexity O(n^2) where n is the number of bombs
    pub fn maximum_detonation(bombs: Vec<Vec<i32>>) -> i32 {
        let mut graph: HashMap<usize, Vec<usize>> = HashMap::new();
        for i in 0..bombs.len() {
            graph.entry(i).or_insert(Vec::new());
        }
        for i in 0..bombs.len() {
            for j in (i + 1)..bombs.len() {
                let x1: f32 = bombs[i][0] as f32;
                let y1: f32 = bombs[i][1] as f32;
                let r1: f32 = bombs[i][2] as f32;
                let x2: f32 = bombs[j][0] as f32;
                let y2: f32 = bombs[j][1] as f32;
                let r2: f32 = bombs[j][2] as f32;
                let d: f32 = ((x1 - x2).powf(2.0) + (y1 - y2).powf(2.0)).sqrt();
                if r1 >= d {
                    graph.entry(i).and_modify(|x| x.push(j));
                }
                if r2 >= d {
                    graph.entry(j).and_modify(|x| x.push(i));
                }
            }
        }
        let mut result: i32 = 0;
        let mut visited: HashSet<usize> = HashSet::new();
        for i in 0..bombs.len() {
            result = max(result, Self::dfs(i, &mut visited, &graph));
            visited.clear();
        }
        result
    }

    fn dfs(node: usize, visited: &mut HashSet<usize>, graph: &HashMap<usize, Vec<usize>>) -> i32 {
        if visited.contains(&node) {
            return 0;
        }
        visited.insert(node);
        let mut result: i32 = 1;
        for nei in graph[&node].iter() {
            result += Self::dfs(*nei, visited, graph);
        }
        result
    }
}

#[cfg(test)]
mod tests {
    use super::Solution;

    #[test]
    fn test_maximum_detonation_case_1() {
        // arrange
        let bombs: Vec<Vec<i32>> = vec![vec![2, 1, 3], vec![6, 1, 4]];
        let expected: i32 = 2;

        // act
        let actual = Solution::maximum_detonation(bombs);

        // assert
        assert_eq!(actual, expected);
    }

    #[test]
    fn test_maximum_detonation_case_2() {
        // arrange
        let bombs: Vec<Vec<i32>> = vec![vec![1, 1, 5], vec![10, 10, 5]];
        let expected: i32 = 1;

        // act
        let actual = Solution::maximum_detonation(bombs);

        // assert
        assert_eq!(actual, expected);
    }

    #[test]
    fn test_maximum_detonation_case_3() {
        // arrange
        let bombs: Vec<Vec<i32>> = vec![
            vec![1, 2, 3],
            vec![2, 3, 1],
            vec![3, 4, 2],
            vec![4, 5, 3],
            vec![5, 6, 4],
        ];
        let expected: i32 = 5;

        // act
        let actual = Solution::maximum_detonation(bombs);

        // assert
        assert_eq!(actual, expected);
    }

    #[test]
    fn test_maximum_detonation_case_4() {
        // arrange
        let bombs: Vec<Vec<i32>> = vec![
            vec![85024, 58997, 3532],
            vec![65196, 42043, 9739],
            vec![85872, 75029, 3117],
            vec![73014, 91183, 7092],
            vec![29098, 40864, 7624],
            vec![11469, 13607, 4315],
            vec![98722, 69681, 9656],
            vec![75140, 42250, 421],
            vec![92580, 44040, 4779],
            vec![58474, 78273, 1047],
            vec![27683, 4203, 6186],
            vec![10714, 24238, 6243],
            vec![60138, 81791, 3496],
            vec![16227, 92418, 5622],
            vec![60496, 64917, 2463],
            vec![59241, 62074, 885],
            vec![11961, 163, 5815],
            vec![37757, 43214, 3402],
            vec![21094, 98519, 1678],
            vec![49368, 22385, 1431],
            vec![6343, 53798, 159],
            vec![80129, 9282, 5139],
            vec![69565, 32036, 6827],
            vec![59372, 64978, 6575],
            vec![44948, 71199, 7095],
            vec![46390, 91701, 1667],
            vec![37144, 98691, 8128],
            vec![13558, 81505, 4653],
            vec![41234, 48161, 9304],
            vec![14852, 3206, 5369],
        ];
        let expected: i32 = 3;

        // act
        let actual = Solution::maximum_detonation(bombs);

        // assert
        assert_eq!(actual, expected);
    }
}
