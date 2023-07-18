pub struct Solution {}

// NOTE: time complexity: O(n * m)
impl Solution {
    pub fn num_islands(mut grid: Vec<Vec<char>>) -> i32 {
        let h = grid.len();
        let w = grid[0].len();
        let mut count = 0;

        for y in 0..h {
            for x in 0..w {
                if grid[y][x] == '1' {
                    count += 1;
                    Self::walk(&mut grid, x, y);
                }
            }
        }

        count
    }

    fn walk(grid: &mut Vec<Vec<char>>, x: usize, y: usize) {
        if y >= grid.len() || x >= grid[0].len() || grid[y][x] == '0' {
            return;
        }

        grid[y][x] = '0';

        Self::walk(grid, x + 1, y);
        if x.checked_sub(1).is_some() {
            Self::walk(grid, x - 1, y);
        }
        Self::walk(grid, x, y + 1);
        if y.checked_sub(1).is_some() {
            Self::walk(grid, x, y - 1);
        }
    }
}

#[cfg(test)]
pub mod test {
    use super::Solution;

    #[test]
    fn case_1() {
        // arrange
        let grid: Vec<Vec<char>> = vec![
            vec!['1', '1', '1', '1', '0'],
            vec!['1', '1', '0', '1', '0'],
            vec!['1', '1', '0', '0', '0'],
            vec!['0', '0', '0', '0', '0'],
        ];
        let expected = 1;

        // act
        let actual = Solution::num_islands(grid);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn case_2() {
        // arrange
        let grid: Vec<Vec<char>> = vec![
            vec!['1', '1', '0', '0', '0'],
            vec!['1', '1', '0', '0', '0'],
            vec!['0', '0', '1', '0', '0'],
            vec!['0', '0', '0', '1', '1'],
        ];
        let expected = 3;

        // act
        let actual = Solution::num_islands(grid);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn t_case_3() {
        // arrange
        let grid: Vec<Vec<char>> = vec![vec!['1'], vec!['1']];
        let expected = 1;

        // act
        let actual = Solution::num_islands(grid);

        // assert
        assert_eq!(expected, actual);
    }
}
