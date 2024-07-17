struct Solution;

impl Solution {
    pub fn find_smallest_set_of_vertices(n: i32, edges: Vec<Vec<i32>>) -> Vec<i32> {
        use std::collections::HashMap;

        let mut incoming: HashMap<i32, Vec<i32>> = HashMap::new();
        for edge in edges {
            let src: i32 = edge[0];
            let dst: i32 = edge[1];
            incoming
                .entry(dst)
                .and_modify(|x| x.push(src))
                .or_insert(vec![src]);
        }
        let mut result: Vec<i32> = Vec::new();
        for i in 0..n {
            if !incoming.contains_key(&i) {
                result.push(i);
            }
        }
        result
    }
}

#[cfg(test)]
mod tests {
    use super::Solution;

    #[test]
    fn test_find_smallest_set_of_vertices_case_1() {
        // arrange
        let n: i32 = 6;
        let edges: Vec<Vec<i32>> = vec![vec![0, 1], vec![0, 2], vec![2, 5], vec![3, 4], vec![4, 2]];
        let expected: Vec<i32> = vec![0, 3];

        // act
        let actual = Solution::find_smallest_set_of_vertices(n, edges);

        // assert
        assert_eq!(actual, expected);
    }
}
