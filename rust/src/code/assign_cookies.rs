struct Solution;

impl Solution {
    pub fn find_content_children(mut g: Vec<i32>, mut s: Vec<i32>) -> i32 {
        // NOTE: time complexity: O(nlogn + mlogm)
        g.sort();
        s.sort();
        let mut i: usize = 0;
        let mut j: usize = 0;
        while i < g.len() {
            while j < s.len() && g[i] > s[j] {
                j += 1;
            }
            if j == s.len() {
                break;
            }
            i += 1;
            j += 1;
        }
        i as i32
    }
}

#[cfg(test)]
mod tests {
    use super::Solution;

    #[test]
    fn test_find_content_children_case_1() {
        // arrange
        let g: Vec<i32> = vec![1, 2, 3];
        let s: Vec<i32> = vec![1, 1];
        let expected = 1;

        // act
        let actual = Solution::find_content_children(g, s);

        // assert
        assert_eq!(actual, expected);
    }

    #[test]
    fn test_find_content_children_case_2() {
        // arrange
        let g: Vec<i32> = vec![1, 2];
        let s: Vec<i32> = vec![1, 2, 3];
        let expected = 2;

        // act
        let actual = Solution::find_content_children(g, s);

        // assert
        assert_eq!(actual, expected);
    }
}
