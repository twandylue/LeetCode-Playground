struct Solution;

impl Solution {
    // NOTE: time complexity O(n + m) where n is the number of nodes and m is the number of nodes
    pub fn shortest_alternating_paths(
        n: i32,
        red_edges: Vec<Vec<i32>>,
        blue_edges: Vec<Vec<i32>>,
    ) -> Vec<i32> {
        use std::collections::{HashMap, HashSet, VecDeque};

        let mut answer: Vec<i32> = Vec::new();
        for _ in 0..n {
            answer.push(-1);
        }
        let mut red_graph: HashMap<i32, Vec<i32>> = HashMap::new();
        let mut blue_graph: HashMap<i32, Vec<i32>> = HashMap::new();
        for i in 0..n {
            red_graph.insert(i, Vec::new());
            blue_graph.insert(i, Vec::new());
        }
        for edges in red_edges {
            red_graph.entry(edges[0]).and_modify(|x| x.push(edges[1]));
        }
        for edges in blue_edges {
            blue_graph.entry(edges[0]).and_modify(|x| x.push(edges[1]));
        }
        let mut queue: VecDeque<(i32, i32, char)> = VecDeque::new();
        queue.push_back((0, 0, 'N'));
        let mut visited: HashSet<(i32, char)> = HashSet::new();
        visited.insert((0, 'N'));
        while let Some((node, length, prev)) = queue.pop_front() {
            if answer[node as usize] == -1 {
                answer[node as usize] = length;
            }
            if prev != 'R' {
                for nei in red_graph[&node].iter() {
                    if !visited.contains(&(*nei, 'R')) {
                        queue.push_back((*nei, length + 1, 'R'));
                        visited.insert((*nei, 'R'));
                    }
                }
            }
            if prev != 'B' {
                // TODO:
                for nei in blue_graph[&node].iter() {
                    if !visited.contains(&(*nei, 'B')) {
                        queue.push_back((*nei, length + 1, 'B'));
                        visited.insert((*nei, 'B'));
                    }
                }
            }
        }

        answer
    }
}

#[cfg(test)]
mod test {
    use super::Solution;

    #[test]
    fn test_shortest_alternating_paths_case_1() {
        // arrange
        let n: i32 = 3;
        let redEdges: Vec<Vec<i32>> = vec![vec![0, 1], vec![1, 2]];
        let blueEdges = vec![];
        let expected: Vec<i32> = vec![0, 1, -1];

        // act
        let actual = Solution::shortest_alternating_paths(n, redEdges, blueEdges);

        // assert
        assert_eq!(expected, actual);
    }
    #[test]
    fn test_shortest_alternating_paths_case_2() {
        // arrange
        let n: i32 = 3;
        let redEdges: Vec<Vec<i32>> = vec![vec![0, 1]];
        let blueEdges: Vec<Vec<i32>> = vec![vec![2, 1]];
        let expected: Vec<i32> = vec![0, 1, -1];

        // act
        let actual = Solution::shortest_alternating_paths(n, redEdges, blueEdges);

        // assert
        assert_eq!(expected, actual);
    }
}
