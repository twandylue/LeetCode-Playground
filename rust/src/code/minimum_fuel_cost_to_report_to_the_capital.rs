use std::collections::HashMap;

struct Solution;

impl Solution {
    pub fn minimum_fuel_cost(roads: Vec<Vec<i32>>, seats: i32) -> i64 {
        let mut result: i64 = 0;
        let mut graph: HashMap<i32, Vec<i32>> = HashMap::new();
        for road in roads {
            graph
                .entry(road[0])
                .and_modify(|x| x.push(road[1]))
                .or_insert(vec![road[1]]);
            graph
                .entry(road[1])
                .and_modify(|x| x.push(road[0]))
                .or_insert(vec![road[0]]);
        }
        Self::dfs(0, -1, seats as i64, &mut result, &graph);
        result
    }

    fn dfs(
        node: i32,
        parent: i32,
        seats: i64,
        result: &mut i64,
        graph: &HashMap<i32, Vec<i32>>,
    ) -> i64 {
        let mut passengers: i64 = 0;
        if let Some(childs) = graph.get(&node) {
            for child in childs {
                if *child != parent {
                    let p: i64 = Self::dfs(*child, node, seats, result, graph);
                    passengers += p as i64;
                    *result += (p as f64 / seats as f64).ceil() as i64;
                }
            }
        }
        passengers + 1
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_minimum_fuel_cost_case_1() {
        // arrange
        let roads: Vec<Vec<i32>> = vec![vec![0, 1], vec![0, 2], vec![0, 3]];
        let seats: i32 = 5;
        let expected: i64 = 3;

        // act
        let actual = Solution::minimum_fuel_cost(roads, seats);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn test_minimum_fuel_cost_case_2() {
        // arrange
        let roads: Vec<Vec<i32>> = vec![
            vec![3, 1],
            vec![3, 2],
            vec![1, 0],
            vec![0, 4],
            vec![0, 5],
            vec![4, 6],
        ];
        let seats: i32 = 2;
        let expected: i64 = 7;

        // act
        let actual = Solution::minimum_fuel_cost(roads, seats);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn test_minimum_fuel_cost_case_3() {
        // arrange
        let roads: Vec<Vec<i32>> = vec![];
        let seats: i32 = 1;
        let expected: i64 = 0;

        // act
        let actual = Solution::minimum_fuel_cost(roads, seats);

        // assert
        assert_eq!(expected, actual);
    }
}
