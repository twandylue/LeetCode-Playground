use std::collections::VecDeque;

struct Solution;

impl Solution {
    pub fn is_bipartite(graph: Vec<Vec<i32>>) -> bool {
        let mut odd: Vec<i32> = vec![0; graph.len()];
        for i in 0..graph.len() {
            if !Self::bfs(i, &mut odd, &graph) {
                return false;
            }
        }
        true
    }

    fn bfs(node: usize, odd: &mut Vec<i32>, graph: &Vec<Vec<i32>>) -> bool {
        if odd[node] == 1 {
            return true;
        }
        odd[node] = -1;
        let mut queue: VecDeque<usize> = VecDeque::from([node]);
        while let Some(i) = queue.pop_front() {
            for nei in graph[i].iter() {
                let nei: usize = *nei as usize;
                if odd[i] == odd[nei] {
                    return false;
                } else if odd[nei] == 0 {
                    queue.push_back(nei);
                    odd[nei] = -1 * odd[i];
                }
            }
        }
        true
    }
}

#[cfg(test)]
mod tests {
    use super::Solution;

    #[test]
    fn test_is_bipartite_case_1() {
        // arrange
        let graph: Vec<Vec<i32>> = vec![vec![1, 2, 3], vec![0, 2], vec![0, 1, 3], vec![0, 2]];
        let expected: bool = false;

        // act
        let actual = Solution::is_bipartite(graph);

        // assert
        assert_eq!(actual, expected);
    }

    #[test]
    fn test_is_bipartite_case_2() {
        // arrange
        let graph: Vec<Vec<i32>> = vec![vec![1, 3], vec![0, 2], vec![1, 3], vec![0, 2]];
        let expected: bool = true;

        // act
        let actual = Solution::is_bipartite(graph);

        // assert
        assert_eq!(actual, expected);
    }
}
