struct Solution {}

impl Solution {
    pub fn daily_temperatures(temperatures: Vec<i32>) -> Vec<i32> {
        let mut output: Vec<i32> = vec![0; temperatures.len()];
        let mut stack: Vec<usize> = Vec::new();

        for i in 0..temperatures.len() {
            while let Some(&index) = stack.last() {
                if temperatures[index] < temperatures[i] {
                    stack.pop().unwrap();
                    output[index] = (i - index) as i32;
                } else {
                    break;
                }
            }

            stack.push(i);
        }

        return output;
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn daily_temperatures_case_1() {
        // arrange
        let temperatures = vec![73, 74, 75, 71, 69, 72, 76, 73];
        let expected = vec![1, 1, 4, 2, 1, 1, 0, 0];

        // act
        let actual = Solution::daily_temperatures(temperatures);

        assert_eq!(expected, actual);
    }

    #[test]
    fn daily_temperatures_case_2() {
        // arrange
        let temperatures = vec![30, 40, 50, 60];
        let expected = vec![1, 1, 1, 0];

        // act
        let actual = Solution::daily_temperatures(temperatures);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn daily_temperatures_case_3() {
        // arrange
        let temperatures = vec![30, 60, 90];
        let expected = vec![1, 1, 0];

        // act
        let actual = Solution::daily_temperatures(temperatures);

        // assert
        assert_eq!(expected, actual);
    }
}
