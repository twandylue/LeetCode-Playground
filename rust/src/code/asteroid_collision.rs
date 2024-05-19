struct Solution {}

impl Solution {
    // NOTE: time complexity O(n)
    pub fn asteroid_collision(asteroids: Vec<i32>) -> Vec<i32> {
        let mut stack: Vec<i32> = Vec::new();
        let mut i: usize = 0;
        while i < asteroids.len() {
            if let Some(&last) = stack.last() {
                if last * asteroids[i] < 0 && last >= asteroids[i] {
                    if last + asteroids[i] == 0 {
                        stack.pop();
                        i += 1;
                    } else if last + asteroids[i] < 0 {
                        stack.pop();
                    } else {
                        i += 1;
                    }
                } else {
                    stack.push(asteroids[i]);
                    i += 1;
                }
            } else {
                stack.push(asteroids[i]);
                i += 1;
            }
        }
        stack
    }
}

#[cfg(test)]
mod tests {
    use super::Solution;

    #[test]
    fn test_asteroid_collision_case_1() {
        // arrange
        let asteroids: Vec<i32> = vec![5, 10, -5];
        let expected: Vec<i32> = vec![5, 10];

        // act
        let actual = Solution::asteroid_collision(asteroids);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn test_asteroid_collision_case_2() {
        // arrange
        let asteroids: Vec<i32> = vec![8, -8];
        let expected: Vec<i32> = vec![];

        // act
        let actual = Solution::asteroid_collision(asteroids);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn test_asteroid_collision_case_3() {
        // arrange
        let asteroids: Vec<i32> = vec![10, 2, -5];
        let expected: Vec<i32> = vec![10];

        // act
        let actual = Solution::asteroid_collision(asteroids);

        // assert
        assert_eq!(expected, actual);
    }
}
