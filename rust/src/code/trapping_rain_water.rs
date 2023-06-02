struct Solution {}

impl Solution {
    pub fn trap(height: Vec<i32>) -> i32 {
        let mut result = 0;
        let mut max_lefts: Vec<i32> = Vec::new();
        let mut max_rights: Vec<i32> = Vec::new();

        for i in 0..height.len() {
            if i == 0 {
                max_lefts.push(height[i]);
                continue;
            }

            let prev = *max_lefts.iter().last().unwrap();
            let max = std::cmp::max(prev, height[i]);
            max_lefts.push(max);
        }

        for i in (0..height.len()).rev() {
            if i == (height.len() - 1) {
                max_rights.push(height[i]);
                continue;
            }

            let prev = *max_rights.iter().last().unwrap();
            let max = std::cmp::max(prev, height[i]);
            max_rights.push(max);
        }
        let max_rights: Vec<i32> = max_rights.into_iter().rev().collect();

        for i in 0..height.len() {
            let val = std::cmp::min(max_lefts[i], max_rights[i]) - height[i];
            if val < 0 {
                continue;
            } else {
                result += val;
            }
        }

        return result;
    }
}

#[cfg(test)]
mod test {
    use super::Solution;

    #[test]
    fn trapping_rain_water_case_1() {
        // arrange
        let height = vec![0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1];
        let expected = 6;

        // act
        let actual = Solution::trap(height);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn trapping_rain_water_case_2() {
        // arrange
        let height = vec![4, 2, 0, 3, 2, 5];
        let expected = 9;

        //  act
        let actual = Solution::trap(height);

        // assert
        assert_eq!(expected, actual);
    }
}
