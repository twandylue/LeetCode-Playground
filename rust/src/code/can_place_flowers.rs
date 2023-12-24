struct Solution {}

impl Solution {
    // NOTE: time complexity: O(n)
    pub fn can_place_flowers(mut flowerbed: Vec<i32>, mut n: i32) -> bool {
        if n == 0 {
            return true;
        }

        for i in 0..flowerbed.len() {
            if flowerbed[i] == 1 {
                if i > 0 {
                    flowerbed[i - 1] = -1;
                }
                if i < flowerbed.len() - 1 {
                    flowerbed[i + 1] = -1;
                }
            }
        }

        let mut i: usize = 0;
        while i < flowerbed.len() {
            if flowerbed[i] == 0 {
                n -= 1;
                if n == 0 {
                    return true;
                }
                i += 2;
                continue;
            }

            i += 1;
        }

        return if n > 0 { false } else { true };
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_can_place_flowers_case_1() {
        // arrange
        let flowerbed: Vec<i32> = vec![1, 0, 0, 0, 1];
        let n: i32 = 1;
        let expected: bool = true;

        // act
        let actual = Solution::can_place_flowers(flowerbed, n);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn test_can_place_flowers_case_2() {
        // arrange
        let flowerbed: Vec<i32> = vec![1, 0, 0, 0, 1];
        let n: i32 = 2;
        let expected: bool = false;

        // act
        let actual = Solution::can_place_flowers(flowerbed, n);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn test_can_place_flowers_case_3() {
        // arrange
        let flowerbed: Vec<i32> = vec![1, 0, 1, 0, 1, 0, 1];
        let n: i32 = 1;
        let expected: bool = false;

        // act
        let actual = Solution::can_place_flowers(flowerbed, n);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn test_can_place_flowers_case_4() {
        // arrange
        let flowerbed: Vec<i32> = vec![1, 0, 0, 0, 0, 1];
        let n: i32 = 2;
        let expected: bool = false;

        // act
        let actual = Solution::can_place_flowers(flowerbed, n);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn test_can_place_flowers_case_5() {
        // arrange
        let flowerbed: Vec<i32> = vec![1, 0, 0, 0, 1, 0, 0];
        let n: i32 = 2;
        let expected: bool = true;

        // act
        let actual = Solution::can_place_flowers(flowerbed, n);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn test_can_place_flowers_case_6() {
        // arrange
        let flowerbed: Vec<i32> = vec![0, 1, 0];
        let n: i32 = 1;
        let expected: bool = false;

        // act
        let actual = Solution::can_place_flowers(flowerbed, n);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn test_can_place_flowers_case_7() {
        // arrange
        let flowerbed: Vec<i32> = vec![0, 1, 0, 1, 0, 1, 0, 0];
        let n: i32 = 1;
        let expected: bool = true;

        // act
        let actual = Solution::can_place_flowers(flowerbed, n);

        // assert
        assert_eq!(expected, actual);
    }
}
