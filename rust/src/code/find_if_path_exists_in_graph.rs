struct Solution;

impl Solution {
    // time complexity: O(V + E)
    pub fn valid_path(n: i32, edges: Vec<Vec<i32>>, source: i32, destination: i32) -> bool {
        use std::collections::{HashMap, HashSet, VecDeque};

        let mut adj: HashMap<i32, Vec<i32>> = HashMap::new();
        for edge in edges {
            let u: i32 = edge[0];
            let v: i32 = edge[1];
            adj.entry(u).and_modify(|x| x.push(v)).or_insert(vec![v]);
            adj.entry(v).and_modify(|x| x.push(u)).or_insert(vec![u]);
        }
        let mut visited: HashSet<i32> = HashSet::from([source]);
        let mut queue: VecDeque<i32> = VecDeque::from([source]);
        while let Some(node) = queue.pop_front() {
            if node == destination {
                return true;
            }
            for nei in adj[&node].iter() {
                if visited.contains(nei) {
                    continue;
                }
                visited.insert(*nei);
                queue.push_back(*nei);
            }
        }

        false
    }
}

#[cfg(test)]
mod tests {
    use super::Solution;

    #[test]
    fn test_valid_path_case_1() {
        // arrange
        let n: i32 = 3;
        let edges: Vec<Vec<i32>> = vec![vec![0, 1], vec![1, 2], vec![2, 0]];
        let source: i32 = 0;
        let destination: i32 = 2;
        let expected: bool = true;

        // act
        let actual = Solution::valid_path(n, edges, source, destination);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn test_first_palindrome_case_2() {
        // arrange
        let n: i32 = 6;
        let edges: Vec<Vec<i32>> = vec![vec![0, 1], vec![0, 2], vec![3, 5], vec![5, 4], vec![4, 3]];
        let source: i32 = 0;
        let destination: i32 = 5;
        let expected: bool = false;

        // act
        let actual = Solution::valid_path(n, edges, source, destination);

        // assert
        assert_eq!(expected, actual);
    }
}
