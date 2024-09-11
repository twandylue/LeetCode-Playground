use std::collections::HashSet;

struct Solution;

impl Solution {
    // NOTE: time complexity: O(n)
    pub fn validate_binary_tree_nodes(n: i32, left_child: Vec<i32>, right_child: Vec<i32>) -> bool {
        let mut has_parent: HashSet<i32> =
            HashSet::from_iter(vec![left_child.clone(), right_child.clone()].concat());
        has_parent.remove(&(-1));
        if has_parent.len() as i32 == n {
            return false;
        }
        let mut root: i32 = -1;
        for i in 0..n {
            if !has_parent.contains(&i) {
                root = i;
            }
        }
        let mut visited: HashSet<i32> = HashSet::new();
        Self::dfs(root, &left_child, &right_child, &mut visited) && visited.len() == n as usize
    }

    fn dfs(
        i: i32,
        left_child: &Vec<i32>,
        right_child: &Vec<i32>,
        visited: &mut HashSet<i32>,
    ) -> bool {
        if i == -1 {
            return true;
        }
        if visited.contains(&i) {
            return false;
        }
        visited.insert(i);
        let i: usize = i as usize;
        Self::dfs(left_child[i], left_child, right_child, visited)
            && Self::dfs(right_child[i], left_child, right_child, visited)
    }
}

#[cfg(test)]
mod tests {
    use super::Solution;

    #[test]
    fn test_validate_binary_tree_nodes_case_1() {
        // arrange
        let n: i32 = 4;
        let left_child: Vec<i32> = vec![1, -1, 3, -1];
        let right_child: Vec<i32> = vec![2, -1, -1, -1];
        let expected = true;

        // act
        let actual: bool = Solution::validate_binary_tree_nodes(n, left_child, right_child);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn test_validate_binary_tree_nodes_case_2() {
        // arrange
        let n: i32 = 4;
        let left_child: Vec<i32> = vec![1, -1, 3, -1];
        let right_child: Vec<i32> = vec![2, 3, -1, -1];
        let expected = false;

        // act
        let actual: bool = Solution::validate_binary_tree_nodes(n, left_child, right_child);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn test_validate_binary_tree_nodes_case_3() {
        // arrange
        let n: i32 = 2;
        let left_child: Vec<i32> = vec![1, 0];
        let right_child: Vec<i32> = vec![-1, -1];
        let expected = false;

        // act
        let actual: bool = Solution::validate_binary_tree_nodes(n, left_child, right_child);

        // assert
        assert_eq!(expected, actual);
    }
}
