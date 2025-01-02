struct Solution;

impl Solution {
    // time complexity: O(n)
    pub fn interval_intersection(
        first_list: Vec<Vec<i32>>,
        second_list: Vec<Vec<i32>>,
    ) -> Vec<Vec<i32>> {
        let mut result: Vec<Vec<i32>> = Vec::new();
        let mut i: usize = 0;
        let mut j: usize = 0;
        while i < first_list.len() && j < second_list.len() {
            if first_list[i][0] <= second_list[j][1] && first_list[i][1] >= second_list[j][0] {
                result.push(vec![
                    std::cmp::max(first_list[i][0], second_list[j][0]),
                    std::cmp::min(first_list[i][1], second_list[j][1]),
                ]);
            }
            if first_list[i][1] <= second_list[j][1] {
                i += 1
            } else {
                j += 1
            }
        }
        result
    }
}

#[cfg(test)]
mod tests {
    use super::Solution;

    #[test]
    fn test_interval_intersection_case_1() {
        // arrange
        let firstList: Vec<Vec<i32>> = vec![vec![0, 2], vec![5, 10], vec![13, 23], vec![24, 25]];
        let secondList: Vec<Vec<i32>> = vec![vec![1, 5], vec![8, 12], vec![15, 24], vec![25, 26]];
        let expected: Vec<Vec<i32>> = vec![
            vec![1, 2],
            vec![5, 5],
            vec![8, 10],
            vec![15, 23],
            vec![24, 24],
            vec![25, 25],
        ];

        // act
        let actual = Solution::interval_intersection(firstList, secondList);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn test_interval_intersection_case_2() {
        // arrange
        let firstList: Vec<Vec<i32>> = vec![vec![0, 2], vec![5, 10], vec![13, 23], vec![24, 25]];
        let secondList: Vec<Vec<i32>> = vec![];
        let expected: Vec<Vec<i32>> = vec![];

        // act
        let actual = Solution::interval_intersection(firstList, secondList);

        // assert
        assert_eq!(expected, actual);
    }
}
