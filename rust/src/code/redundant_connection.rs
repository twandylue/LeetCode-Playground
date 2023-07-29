struct Solution {}

impl Solution {
    pub fn find_redundant_connection(edges: Vec<Vec<i32>>) -> Vec<i32> {
        let mut parent: Vec<i32> = Vec::new();
        let mut rank: Vec<i32> = Vec::new();

        for i in 0..edges.len() + 1 {
            parent.push(i as i32);
            rank.push(1);
        }
        for edge in edges {
            let n1 = edge[0];
            let n2 = edge[1];
            if Self::union(n1, n2, &mut rank, &mut parent) {
                continue;
            }
            return vec![n1, n2];
        }

        return vec![];
    }

    fn find(n: i32, parent: &mut Vec<i32>) -> i32 {
        let mut p: usize = parent[n as usize] as usize;
        while p != parent[p] as usize {
            parent[p] = parent[parent[p] as usize];
            p = parent[p] as usize;
        }

        p as i32
    }

    fn union(n1: i32, n2: i32, rank: &mut Vec<i32>, parent: &mut Vec<i32>) -> bool {
        let p1: usize = Self::find(n1, parent) as usize;
        let p2: usize = Self::find(n2, parent) as usize;

        if p1 == p2 {
            return false;
        }

        if rank[p1] > rank[p2] {
            parent[p2] = p1 as i32;
            rank[p1] += rank[p2];
        } else {
            parent[p1] = p2 as i32;
            rank[p2] += rank[p1];
        }

        true
    }
}

#[cfg(test)]
mod tests {
    use super::Solution;

    #[test]
    fn find_redundant_connection_case_1() {
        // arrange
        let edges: Vec<Vec<i32>> = vec![vec![1, 2], vec![1, 3], vec![2, 3]];
        let expected: Vec<i32> = vec![2, 3];

        // act
        let actual = Solution::find_redundant_connection(edges);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn find_redundant_connection_case_2() {
        // arrange
        let edges: Vec<Vec<i32>> = vec![vec![1, 2], vec![2, 3], vec![3, 4], vec![1, 4], vec![1, 5]];
        let expected: Vec<i32> = vec![1, 4];

        // act
        let actual = Solution::find_redundant_connection(edges);

        // assert
        assert_eq!(expected, actual);
    }
}
