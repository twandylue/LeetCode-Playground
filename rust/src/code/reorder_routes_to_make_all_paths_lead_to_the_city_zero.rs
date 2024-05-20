struct Solution {}

use std::collections::{HashMap, HashSet};

impl Solution {
    // NOTE: time complexity O(n)
    pub fn min_reorder(n: i32, connections: Vec<Vec<i32>>) -> i32 {
        let mut changes: i32 = 0;
        let mut edges: HashSet<(i32, i32)> = HashSet::new();
        let mut graph: HashMap<i32, Vec<i32>> = HashMap::new();
        let mut visited: HashSet<i32> = HashSet::new();
        for city in 0..n {
            graph.insert(city, vec![]);
        }
        for connection in connections {
            edges.insert((connection[0], connection[1]));
            graph
                .entry(connection[0])
                .and_modify(|x| x.push(connection[1]))
                .or_insert(vec![connection[1]]);
            graph
                .entry(connection[1])
                .and_modify(|x| x.push(connection[0]))
                .or_insert(vec![connection[0]]);
        }

        visited.insert(0);
        Self::dfs(0, &edges, &graph, &mut visited, &mut changes);
        changes
    }

    fn dfs(
        city: i32,
        edges: &HashSet<(i32, i32)>,
        graph: &HashMap<i32, Vec<i32>>,
        visited: &mut HashSet<i32>,
        changes: &mut i32,
    ) {
        for neighbor in graph[&city].iter() {
            if visited.contains(neighbor) {
                continue;
            }
            if !edges.contains(&(*neighbor, city)) {
                *changes += 1;
            }
            visited.insert(*neighbor);
            Self::dfs(*neighbor, edges, graph, visited, changes);
        }
    }
}

#[cfg(test)]
mod tests {
    use super::Solution;

    #[test]
    fn test_min_reorder_case_1() {
        // arrange
        let n: i32 = 6;
        let connections: Vec<Vec<i32>> =
            vec![vec![0, 1], vec![1, 3], vec![2, 3], vec![4, 0], vec![4, 5]];
        let expected: i32 = 3;

        // act
        let actual = Solution::min_reorder(n, connections);

        // assert
        assert_eq!(expected, actual);
    }
    #[test]
    fn test_min_reorder_case_2() {
        // arrange
        let n: i32 = 5;
        let connections: Vec<Vec<i32>> = vec![vec![1, 0], vec![1, 2], vec![3, 2], vec![3, 4]];
        let expected: i32 = 2;

        // act
        let actual = Solution::min_reorder(n, connections);

        // assert
        assert_eq!(expected, actual);
    }
}
