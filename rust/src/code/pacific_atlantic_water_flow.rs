use std::collections::HashSet;

struct Solution {}

type COL = usize;
type ROW = usize;

impl Solution {
    // NOTE: time complexity O(n * m), where n is the number of rows and m is the number of columns
    pub fn pacific_atlantic(heights: Vec<Vec<i32>>) -> Vec<Vec<i32>> {
        let mut pac: HashSet<(ROW, COL)> = HashSet::new();
        let mut alt: HashSet<(ROW, COL)> = HashSet::new();
        let rows = heights.len();
        let cols = heights[0].len();

        for r in 0..rows {
            Self::dfs(r, 0, &mut pac, &heights, heights[r][0]);
            Self::dfs(r, cols - 1, &mut alt, &heights, heights[r][cols - 1]);
        }

        for c in 0..cols {
            Self::dfs(0, c, &mut pac, &heights, heights[0][c]);
            Self::dfs(rows - 1, c, &mut alt, &heights, heights[rows - 1][c]);
        }

        let mut result: Vec<Vec<i32>> = Vec::new();
        for r in 0..rows {
            for c in 0..cols {
                if pac.contains(&(r, c)) && alt.contains(&(r, c)) {
                    result.push(vec![r as i32, c as i32]);
                }
            }
        }

        return result;
    }

    fn dfs(
        r: ROW,
        c: COL,
        visited: &mut HashSet<(ROW, COL)>,
        heights: &Vec<Vec<i32>>,
        pre_height: i32,
    ) {
        if visited.contains(&(r, c))
            || r >= heights.len()
            || c >= heights[0].len()
            || heights[r][c] < pre_height
        {
            return;
        }

        visited.insert((r, c));
        if r.checked_sub(1).is_some() {
            Self::dfs(r - 1, c, visited, heights, heights[r][c]);
        }
        Self::dfs(r + 1, c, visited, heights, heights[r][c]);

        if c.checked_sub(1).is_some() {
            Self::dfs(r, c - 1, visited, heights, heights[r][c]);
        }
        Self::dfs(r, c + 1, visited, heights, heights[r][c]);
    }
}

#[cfg(test)]
mod tests {
    use super::Solution;

    #[test]
    fn pacific_atlantic_case_1() {
        // arrange
        let heights = vec![
            vec![1, 2, 2, 3, 5],
            vec![3, 2, 3, 4, 4],
            vec![2, 4, 5, 3, 1],
            vec![6, 7, 1, 4, 5],
            vec![5, 1, 1, 2, 4],
        ];
        let expected = vec![
            vec![0, 4],
            vec![1, 3],
            vec![1, 4],
            vec![2, 2],
            vec![3, 0],
            vec![3, 1],
            vec![4, 0],
        ];

        // act
        let actual = Solution::pacific_atlantic(heights);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn pacific_atlantic_case_2() {
        // arrange
        let heights = vec![vec![1]];
        let expected = vec![vec![0, 0]];

        // act
        let actual = Solution::pacific_atlantic(heights);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn pacific_atlantic_case_3() {
        // arrange
        let heights = vec![vec![1, 1], vec![1, 1], vec![1, 1]];
        let expected = vec![
            vec![0, 0],
            vec![0, 1],
            vec![1, 0],
            vec![1, 1],
            vec![2, 0],
            vec![2, 1],
        ];

        // act
        let actual = Solution::pacific_atlantic(heights);

        // assert
        assert_eq!(expected, actual);
    }
}
