use std::{collections::HashMap, unreachable};

struct Solution {}

impl Solution {
    pub fn can_finish(num_courses: i32, prerequisites: Vec<Vec<i32>>) -> bool {
        let mut graph_cache: HashMap<i32, Vec<i32>> = HashMap::new();
        for i in prerequisites {
            let course = i[0];
            let pre = i[1];
            graph_cache
                .entry(course)
                .and_modify(|v| v.push(pre))
                .or_insert(vec![pre]);
        }

        let mut visited_cache: HashMap<i32, i32> = HashMap::new();
        for i in 0..num_courses {
            if Self::dfs(i, &graph_cache, &mut visited_cache) {
                continue;
            }

            return false;
        }

        return true;
    }

    fn dfs(
        course: i32,
        graph_cache: &HashMap<i32, Vec<i32>>,
        visited_cache: &mut HashMap<i32, i32>,
    ) -> bool {
        if !graph_cache.contains_key(&course) {
            return true;
        }

        if visited_cache.contains_key(&course) {
            let val = visited_cache.get(&course).unwrap();
            match val {
                1 => return false,
                0 => return true,
                _ => unreachable!(),
            };
        }

        visited_cache.insert(course, 1);
        for pre in graph_cache.get(&course).unwrap() {
            if Self::dfs(*pre, graph_cache, visited_cache) {
                continue;
            }

            return false;
        }

        visited_cache.entry(course).and_modify(|v| *v = 0);

        return true;
    }
}

#[cfg(test)]
mod test {
    use super::Solution;

    #[test]
    fn case_1() {
        // arrange
        let num_courses = 2;
        let prerequisites = vec![vec![1, 0]];
        let expected = true;

        // act
        let actual = Solution::can_finish(num_courses, prerequisites);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn case_2() {
        // arrange
        let num_courses = 2;
        let prerequisites = vec![vec![1, 0], vec![0, 1]];
        let expected = false;

        // act
        let actual = Solution::can_finish(num_courses, prerequisites);

        // assert
        assert_eq!(expected, actual);
    }
}
