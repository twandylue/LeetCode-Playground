use std::collections::HashSet;

struct Solution {}

impl Solution {
    // NOTE: time complexity: O(n)
    pub fn merge_triplets(triplets: Vec<Vec<i32>>, target: Vec<i32>) -> bool {
        let mut good: HashSet<i32> = HashSet::new();
        for t in triplets {
            if t[0] > target[0] || t[1] > target[1] || t[2] > target[2] {
                continue;
            }

            for i in 0..target.len() {
                if t[i] == target[i] {
                    good.insert(i as i32);
                }
            }
        }

        return good.len() == 3;
    }
}

#[cfg(test)]
mod tests {
    use super::Solution;

    #[test]
    fn test_merge_triplets_case_1() {
        // arrange
        let triplets = vec![vec![2, 5, 3], vec![1, 8, 4], vec![1, 7, 5]];
        let target = vec![2, 7, 5];
        let expected = true;

        // act
        let actual = Solution::merge_triplets(triplets, target);

        // assert
        assert_eq!(actual, expected);
    }

    #[test]
    fn test_merge_triplets_case_2() {
        // arrange
        let triplets = vec![vec![3, 4, 5], vec![4, 5, 6]];
        let target = vec![2, 5, 8];
        let expected = false;

        // act
        let actual = Solution::merge_triplets(triplets, target);

        // assert
        assert_eq!(actual, expected);
    }

    #[test]
    fn test_merge_triplets_case_3() {
        // arrange
        let triplets = vec![vec![2, 5, 3], vec![2, 3, 4], vec![1, 2, 5], vec![5, 2, 3]];
        let target = vec![5, 5, 5];
        let expected = true;

        // act
        let actual = Solution::merge_triplets(triplets, target);

        // assert
        assert_eq!(actual, expected);
    }

    #[test]
    fn test_merge_triplets_case_4() {
        // arrange
        let triplets = vec![vec![3, 5, 1], vec![10, 5, 7]];
        let target = vec![3, 5, 7];
        let expected = false;

        // act
        let actual = Solution::merge_triplets(triplets, target);

        // assert
        assert_eq!(actual, expected);
    }

    #[test]
    fn test_merge_triplets_case_5() {
        // arrange
        let triplets = vec![
            vec![4, 5, 2],
            vec![4, 2, 7],
            vec![5, 8, 6],
            vec![3, 6, 6],
            vec![4, 5, 2],
        ];
        let target = vec![4, 5, 7];
        let expected = true;

        // act
        let actual = Solution::merge_triplets(triplets, target);

        // assert
        assert_eq!(actual, expected);
    }
}
