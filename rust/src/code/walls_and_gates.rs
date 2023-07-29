use std::collections::{HashSet, VecDeque};

struct Solution {}

type ROW = usize;
type COL = usize;

// NOTE: Time complexity: O(n * m)
impl Solution {
    pub fn walls_and_gates(mut rooms: &mut Vec<Vec<i32>>) {
        let mut queue: VecDeque<(ROW, COL)> = VecDeque::new();
        let mut visited: HashSet<(ROW, COL)> = HashSet::new();
        for row in 0..rooms.len() {
            for col in 0..rooms[0].len() {
                if rooms[row][col] == 0 {
                    queue.push_back((row, col));
                    visited.insert((row, col));
                }
            }
        }

        let mut distance: i32 = 0;
        while !queue.is_empty() {
            for _ in 0..queue.len() {
                if let Some((r, c)) = queue.pop_front() {
                    rooms[r][c] = distance;
                    Self::walk_room(r + 1, c, &mut queue, &mut rooms, &mut visited);
                    if r.checked_sub(1).is_some() {
                        Self::walk_room(r - 1, c, &mut queue, &mut rooms, &mut visited);
                    }

                    Self::walk_room(r, c + 1, &mut queue, &mut rooms, &mut visited);
                    if c.checked_sub(1).is_some() {
                        Self::walk_room(r, c - 1, &mut queue, &mut rooms, &mut visited);
                    }
                }
            }
            distance += 1;
        }
    }

    fn walk_room(
        row: usize,
        col: usize,
        queue: &mut VecDeque<(ROW, COL)>,
        rooms: &mut Vec<Vec<i32>>,
        visited: &mut HashSet<(ROW, COL)>,
    ) {
        if row >= rooms.len()
            || col >= rooms[0].len()
            || visited.contains(&(row, col))
            || rooms[row][col] == -1
        {
            return;
        }
        visited.insert((row, col));
        queue.push_back((row, col));
    }
}

#[cfg(test)]
mod tests {
    use super::Solution;

    #[test]
    fn walls_and_gates_case_1() {
        // arrange
        let mut rooms: Vec<Vec<i32>> = vec![
            vec![2147483647, -1, 0, 2147483647],
            vec![2147483647, 2147483647, 2147483647, -1],
            vec![2147483647, -1, 2147483647, -1],
            vec![0, -1, 2147483647, 2147483647],
        ];

        let expected = vec![
            vec![3, -1, 0, 1],
            vec![2, 2, 1, -1],
            vec![1, -1, 2, -1],
            vec![0, -1, 3, 4],
        ];

        // act
        Solution::walls_and_gates(&mut rooms);

        // assert
        assert_eq!(expected, rooms);
    }

    #[test]
    fn walls_and_gates_case_2() {
        // arrange
        let mut rooms: Vec<Vec<i32>> = vec![vec![0, -1], vec![2147483647, 2147483647]];
        let expected = vec![vec![0, -1], vec![1, 2]];

        // act
        Solution::walls_and_gates(&mut rooms);

        // assert
        assert_eq!(expected, rooms);
    }
}
