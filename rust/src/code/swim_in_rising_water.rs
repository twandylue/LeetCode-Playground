use std::cmp::{max, Reverse};
use std::collections::{BinaryHeap, HashSet};

type X = usize;
type Y = usize;

struct Solution;

impl Solution {
    // NOTE: time complexity O((n^2) * log n)
    pub fn swim_in_water(grid: Vec<Vec<i32>>) -> i32 {
        let n: usize = grid.len();
        let mut min_heap: BinaryHeap<Reverse<(i32, X, Y)>> =
            BinaryHeap::from([Reverse((grid[0][0], 0, 0))]);
        let mut visited: HashSet<(X, Y)> = HashSet::from([(0, 0)]);
        let directions: Vec<(isize, isize)> = vec![(1, 0), (0, 1), (-1, 0), (0, -1)];

        while let Some(Reverse((h, x, y))) = min_heap.pop() {
            if x == n - 1 && y == n - 1 {
                return h;
            }

            for (dx, dy) in directions.iter() {
                let nx: isize = (x as isize + *dx) as isize;
                let ny: isize = (y as isize + *dy) as isize;
                if nx >= 0
                    && ny >= 0
                    && (nx as usize) < n
                    && (ny as usize) < n
                    && !visited.contains(&(nx as usize, ny as usize))
                {
                    let nx = nx as usize;
                    let ny = ny as usize;
                    visited.insert((nx, ny));
                    min_heap.push(Reverse((max(grid[ny][nx], h), nx, ny)));
                } else {
                    continue;
                }
            }
        }

        unreachable!("should not reach here");
    }
}

#[cfg(test)]
mod tests {
    use super::Solution;

    #[test]
    fn test_swim_in_water_case_1() {
        // arrange
        let grid = vec![vec![0, 2], vec![1, 3]];
        let expected = 3;

        // act
        let actual = Solution::swim_in_water(grid);

        // assert
        assert_eq!(actual, expected);
    }

    #[test]
    fn test_swim_in_water_case_2() {
        // arrange
        let grid = vec![
            vec![0, 1, 2, 3, 4],
            vec![24, 23, 22, 21, 5],
            vec![12, 13, 14, 15, 16],
            vec![11, 17, 18, 19, 20],
            vec![10, 9, 8, 7, 6],
        ];
        let expected = 16;

        // act
        let actual = Solution::swim_in_water(grid);

        // assert
        assert_eq!(actual, expected);
    }
}
