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

    pub fn trap_2(height: Vec<i32>) -> i32 {
        let mut result = 0;
        let mut max_left = height[0];
        let mut max_right = height[height.len() - 1];
        let mut l = 0;
        let mut r = height.len() - 1;

        while l < r && r > 0 && l < height.len() {
            if height[l] <= height[r] {
                max_left = std::cmp::max(height[l], max_left);
                if max_left - height[l] > 0 {
                    result += max_left - height[l];
                }
                l += 1;
            } else {
                max_right = std::cmp::max(height[r], max_right);
                if max_right - height[r] > 0 {
                    result += max_right - height[r];
                }
                r -= 1;
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

    #[test]
    fn trapping_rain_water_case_3() {
        // arrange
        let height = vec![0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1];
        let expected = 6;

        //  act
        let actual = Solution::trap_2(height);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn trapping_rain_water_case_4() {
        // arrange
        let height = vec![4, 2, 0, 3, 2, 5];
        let expected = 9;

        //  act
        let actual = Solution::trap_2(height);

        // assert
        assert_eq!(expected, actual);
    }
}
