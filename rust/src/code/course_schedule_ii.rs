use std::collections::{HashMap, HashSet};

struct Solution {}

impl Solution {
    pub fn find_order(num_courses: i32, prerequisites: Vec<Vec<i32>>) -> Vec<i32> {
        let mut result: Vec<i32> = Vec::new();
        let mut visited: HashSet<i32> = HashSet::new();
        let mut cycle: HashSet<i32> = HashSet::new();
        let mut course_graph: HashMap<i32, Vec<i32>> = HashMap::new();
        for item in prerequisites {
            let course = item[0];
            let pre = item[1];
            course_graph
                .entry(course)
                .and_modify(|x| x.push(pre))
                .or_insert(vec![pre]);
        }

        for c in 0..num_courses {
            if !Self::dfs(c, &mut result, &mut visited, &mut cycle, &course_graph) {
                return vec![];
            }
        }

        result
    }

    fn dfs(
        course: i32,
        result: &mut Vec<i32>,
        visited: &mut HashSet<i32>,
        cycle: &mut HashSet<i32>,
        course_graph: &HashMap<i32, Vec<i32>>,
    ) -> bool {
        if visited.contains(&course) {
            return true;
        }
        if cycle.contains(&course) {
            return false;
        }

        cycle.insert(course);
        if let Some(pres) = course_graph.get(&course) {
            for pre in pres.iter() {
                if !Self::dfs(*pre, result, visited, cycle, course_graph) {
                    return false;
                }
            }
        }

        cycle.remove(&course);
        visited.insert(course);
        result.push(course);

        true
    }
}

#[cfg(test)]
mod tests {
    use super::Solution;

    #[test]
    fn find_order_case_1() {
        // arrange
        let num_courses: i32 = 2;
        let prerequisites: Vec<Vec<i32>> = vec![vec![1, 0]];
        let mut expected: Vec<i32> = vec![0, 1];

        // act
        let mut actual = Solution::find_order(num_courses, prerequisites);

        // assert
        expected.sort();
        actual.sort();
        assert_eq!(expected, actual);
    }

    #[test]
    fn find_order_case_2() {
        // arrange
        let num_courses: i32 = 4;
        let prerequisites: Vec<Vec<i32>> = vec![vec![1, 0], vec![2, 0], vec![3, 1], vec![3, 2]];
        let mut expected: Vec<i32> = vec![0, 2, 1, 3];

        // act
        let mut actual = Solution::find_order(num_courses, prerequisites);

        // assert
        expected.sort();
        actual.sort();
        assert_eq!(expected, actual);
    }

    #[test]
    fn find_order_case_3() {
        // arrange
        let num_courses: i32 = 1;
        let prerequisites: Vec<Vec<i32>> = vec![];
        let mut expected: Vec<i32> = vec![0];

        // act
        let mut actual = Solution::find_order(num_courses, prerequisites);

        // assert
        expected.sort();
        actual.sort();
        assert_eq!(expected, actual);
    }
}
