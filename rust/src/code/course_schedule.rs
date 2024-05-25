use std::collections::{HashMap, HashSet};

struct Solution {}

impl Solution {
    // NOTE: time complexity is O(n + m), where n is the number of courses and m is the number of prerequisites
    pub fn can_finish(num_courses: i32, prerequisites: Vec<Vec<i32>>) -> bool {
        let mut course_graph: HashMap<i32, Vec<i32>> = HashMap::new();
        for i in 0..num_courses {
            course_graph.entry(i).or_insert(Vec::new());
        }
        for item in prerequisites {
            let course: i32 = item[0];
            let pre: i32 = item[1];
            course_graph.entry(course).and_modify(|x| x.push(pre));
        }
        let mut visiting_set: HashSet<i32> = HashSet::new();
        let mut completed_set: HashSet<i32> = HashSet::new();
        for c in 0..num_courses {
            if Self::dfs(c, &course_graph, &mut visiting_set, &mut completed_set) {
                continue;
            }
            return false;
        }
        true
    }

    fn dfs(
        course: i32,
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
        for pre in course_graph.get(&course).unwrap().iter() {
            if Self::dfs(*pre, course_graph, visiting_set, completed_set) {
                continue;
            }
            return false;
        }
        completed_set.insert(course);
        visiting_set.remove(&course);
        true
    }
}

#[cfg(test)]
mod test {
    use super::Solution;

    #[test]
    fn test_can_finish_case_1() {
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
    fn test_can_finish_case_2() {
        // arrange
        let num_courses = 2;
        let prerequisites = vec![vec![1, 0], vec![0, 1]];
        let expected = false;

        // act
        let actual = Solution::can_finish(num_courses, prerequisites);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn test_can_finish_case_3() {
        // arrange
        let num_courses = 100;
        let prerequisites = vec![
            vec![1, 0],
            vec![2, 0],
            vec![2, 1],
            vec![3, 1],
            vec![3, 2],
            vec![4, 2],
            vec![4, 3],
            vec![5, 3],
            vec![5, 4],
            vec![6, 4],
            vec![6, 5],
            vec![7, 5],
            vec![7, 6],
            vec![8, 6],
            vec![8, 7],
            vec![9, 7],
            vec![9, 8],
            vec![10, 8],
            vec![10, 9],
            vec![11, 9],
            vec![11, 10],
            vec![12, 10],
            vec![12, 11],
            vec![13, 11],
            vec![13, 12],
            vec![14, 12],
            vec![14, 13],
            vec![15, 13],
            vec![15, 14],
            vec![16, 14],
            vec![16, 15],
            vec![17, 15],
            vec![17, 16],
            vec![18, 16],
            vec![18, 17],
            vec![19, 17],
            vec![19, 18],
            vec![20, 18],
            vec![20, 19],
            vec![21, 19],
            vec![21, 20],
            vec![22, 20],
            vec![22, 21],
            vec![23, 21],
            vec![23, 22],
            vec![24, 22],
            vec![24, 23],
            vec![25, 23],
            vec![25, 24],
            vec![26, 24],
            vec![26, 25],
            vec![27, 25],
            vec![27, 26],
            vec![28, 26],
            vec![28, 27],
            vec![29, 27],
            vec![29, 28],
            vec![30, 28],
            vec![30, 29],
            vec![31, 29],
            vec![31, 30],
            vec![32, 30],
            vec![32, 31],
            vec![33, 31],
            vec![33, 32],
            vec![34, 32],
            vec![34, 33],
            vec![35, 33],
            vec![35, 34],
            vec![36, 34],
            vec![36, 35],
            vec![37, 35],
            vec![37, 36],
            vec![38, 36],
            vec![38, 37],
            vec![39, 37],
            vec![39, 38],
            vec![40, 38],
            vec![40, 39],
            vec![41, 39],
            vec![41, 40],
            vec![42, 40],
            vec![42, 41],
            vec![43, 41],
            vec![43, 42],
            vec![44, 42],
            vec![44, 43],
            vec![45, 43],
            vec![45, 44],
            vec![46, 44],
            vec![46, 45],
            vec![47, 45],
            vec![47, 46],
            vec![48, 46],
            vec![48, 47],
            vec![49, 47],
            vec![49, 48],
            vec![50, 48],
            vec![50, 49],
            vec![51, 49],
            vec![51, 50],
            vec![52, 50],
            vec![52, 51],
            vec![53, 51],
            vec![53, 52],
            vec![54, 52],
            vec![54, 53],
            vec![55, 53],
            vec![55, 54],
            vec![56, 54],
            vec![56, 55],
            vec![57, 55],
            vec![57, 56],
            vec![58, 56],
            vec![58, 57],
            vec![59, 57],
            vec![59, 58],
            vec![60, 58],
            vec![60, 59],
            vec![61, 59],
            vec![61, 60],
            vec![62, 60],
            vec![62, 61],
            vec![63, 61],
            vec![63, 62],
            vec![64, 62],
            vec![64, 63],
            vec![65, 63],
            vec![65, 64],
            vec![66, 64],
            vec![66, 65],
            vec![67, 65],
            vec![67, 66],
            vec![68, 66],
            vec![68, 67],
            vec![69, 67],
            vec![69, 68],
            vec![70, 68],
            vec![70, 69],
            vec![71, 69],
            vec![71, 70],
            vec![72, 70],
            vec![72, 71],
            vec![73, 71],
            vec![73, 72],
            vec![74, 72],
            vec![74, 73],
            vec![75, 73],
            vec![75, 74],
            vec![76, 74],
            vec![76, 75],
            vec![77, 75],
            vec![77, 76],
            vec![78, 76],
            vec![78, 77],
            vec![79, 77],
            vec![79, 78],
            vec![80, 78],
            vec![80, 79],
            vec![81, 79],
            vec![81, 80],
            vec![82, 80],
            vec![82, 81],
            vec![83, 81],
            vec![83, 82],
            vec![84, 82],
            vec![84, 83],
            vec![85, 83],
            vec![85, 84],
            vec![86, 84],
            vec![86, 85],
            vec![87, 85],
            vec![87, 86],
            vec![88, 86],
            vec![88, 87],
            vec![89, 87],
            vec![89, 88],
            vec![90, 88],
            vec![90, 89],
            vec![91, 89],
            vec![91, 90],
            vec![92, 90],
            vec![92, 91],
            vec![93, 91],
            vec![93, 92],
            vec![94, 92],
            vec![94, 93],
            vec![95, 93],
            vec![95, 94],
            vec![96, 94],
            vec![96, 95],
            vec![97, 95],
            vec![97, 96],
            vec![98, 96],
            vec![98, 97],
            vec![99, 97],
        ];
        let expected = true;

        // act
        let actual = Solution::can_finish(num_courses, prerequisites);

        // assert
        assert_eq!(expected, actual);
    }
}
