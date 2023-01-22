use std::collections::HashSet;

pub struct Solution {}

impl Solution {
    pub fn exist(board: Vec<Vec<char>>, word: String) -> bool {
        let mut path = HashSet::<(usize, usize)>::new();

        for r in 0..board.len() {
            for c in 0..board[r].len() {
                if Solution::bfs(r, c, 0, &word, &board, &mut path) {
                    return true;
                }
            }
        }

        return false;
    }

    fn bfs(
        r: usize,
        c: usize,
        i: usize,
        word: &str,
        board: &Vec<Vec<char>>,
        path: &mut HashSet<(usize, usize)>,
    ) -> bool {
        let rows = board.len();
        let cols = board[0].len();

        if i == word.len() {
            return true;
        }
        if r >= rows
            || c >= cols
            || word.chars().nth(i).unwrap() != board[r][c]
            || path.contains(&(r, c))
        {
            return false;
        }

        path.insert((r, c));
        let res = Solution::bfs(r + 1, c, i + 1, word, board, path)
            || (r != 0 && Solution::bfs(r - 1, c, i + 1, word, board, path))
            || Solution::bfs(r, c + 1, i + 1, word, board, path)
            || (c != 0 && Solution::bfs(r, c - 1, i + 1, word, board, path));
        path.remove(&(r, c));

        return res;
    }
}

#[cfg(test)]
pub mod tests {
    use super::Solution;

    #[test]
    fn case_1() {
        let board = vec![
            vec!['A', 'B', 'C', 'E'],
            vec!['S', 'F', 'C', 'S'],
            vec!['A', 'D', 'E', 'E'],
        ];
        let word = "ABCCED".to_string();
        let expected = true;
        let actual = Solution::exist(board, word);
        assert_eq!(expected, actual);
    }

    #[test]
    fn case_2() {
        let board = vec![
            vec!['A', 'B', 'C', 'E'],
            vec!['S', 'F', 'C', 'S'],
            vec!['A', 'D', 'E', 'E'],
        ];
        let word = "ABCB".to_string();
        let expected = false;
        let actual = Solution::exist(board, word);
        assert_eq!(expected, actual);
    }

    #[test]
    fn case_3() {
        let board = vec![
            vec!['A', 'B', 'C', 'E'],
            vec!['S', 'F', 'C', 'S'],
            vec!['A', 'D', 'E', 'E'],
        ];
        let word = "SEE".to_string();
        let expected = true;
        let actual = Solution::exist(board, word);
        assert_eq!(expected, actual);
    }

    #[test]
    fn case_4() {
        let board = vec![vec!['a', 'b']];
        let word = "ba".to_string();
        let expected = true;
        let actual = Solution::exist(board, word);
        assert_eq!(expected, actual);
    }
}
