use std::collections::{HashMap, HashSet};

struct Solution {}

impl Solution {
    // NOTE: time complexity is O(n + m), where n is the number of courses and m is the number of prerequisites
    pub fn find_order(num_courses: i32, prerequisites: Vec<Vec<i32>>) -> Vec<i32> {
        let mut result: Vec<i32> = Vec::new();
        let mut course_graph: HashMap<i32, Vec<i32>> = HashMap::new();
        for i in 0..num_courses {
            course_graph.entry(i).or_insert(vec![]);
        }
        for item in prerequisites {
            let course: i32 = item[0];
            let pre: i32 = item[1];
            course_graph.entry(course).and_modify(|x| x.push(pre));
        }
        let mut visiting_set: HashSet<i32> = HashSet::new();
        let mut completed_set: HashSet<i32> = HashSet::new();
        for i in 0..num_courses {
            if Self::dfs(
                i,
                &mut result,
                &course_graph,
                &mut visiting_set,
                &mut completed_set,
            ) {
                continue;
            }
            return vec![];
        }
        result
    }

    fn dfs(
        course: i32,
        result: &mut Vec<i32>,
        course_graph: &HashMap<i32, Vec<i32>>,
        visiting_set: &mut HashSet<i32>,
        completed_set: &mut HashSet<i32>,
    ) -> bool {
        if visiting_set.contains(&course) {
            return false;
        }
        if completed_set.contains(&course) {
            return true;
        }
        visiting_set.insert(course);
        for i in course_graph.get(&course).unwrap() {
            if Self::dfs(*i, result, course_graph, visiting_set, completed_set) {
                continue;
            }
            return false;
        }
        visiting_set.remove(&course);
        completed_set.insert(course);
        result.push(course);
        true
    }
}

#[cfg(test)]
mod tests {
    use super::Solution;

    #[test]
    fn test_find_order_case_1() {
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
    fn test_find_order_case_2() {
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
    fn test_find_order_case_3() {
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
