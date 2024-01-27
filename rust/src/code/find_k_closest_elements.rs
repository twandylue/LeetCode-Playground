struct Solution {}

impl Solution {
    // NOTE: time complexity: O(logn)
    pub fn find_closest_elements2(arr: Vec<i32>, k: i32, x: i32) -> Vec<i32> {
        let k: usize = k as usize;
        let mut l: usize = 0;
        let mut r: usize = arr.len() - k;
        while l < r {
            let mid: usize = (l + r) / 2;
            if x - arr[mid] > arr[mid + k] - x {
                l = mid + 1;
            } else {
                r = mid;
            }
        }

        return arr[l..l + k].to_vec();
    }

    // NOTE: time complexity: O(logn + n) = O(n)
    pub fn find_closest_elements(arr: Vec<i32>, k: i32, x: i32) -> Vec<i32> {
        let center: usize = Self::binary_search(&arr, x);
        if k == 1 {
            return Vec::from([arr[center]]);
        }
        if center == 0 {
            return arr[..k as usize].to_vec();
        }
        if center == arr.len() - 1 {
            return arr[arr.len() - (k as usize)..].to_vec();
        }

        let mut l: usize = center;
        let mut r: usize = center;
        while l >= 0 && r < arr.len() {
            if r - l + 1 == k as usize {
                return arr[l..r + 1].to_vec();
            }
            if l == 0 {
                r += 1;
                continue;
            }
            if r == arr.len() - 1 {
                l -= 1;
                continue;
            }
            if x - arr[l - 1] <= arr[r + 1] - x {
                l -= 1;
            } else {
                r += 1;
            }
        }

        return arr[l..r + 1].to_vec();
    }

    fn binary_search(arr: &Vec<i32>, target: i32) -> usize {
        if arr.len() == 0 {
            return 0;
        }
        if target < arr[0] {
            return 0;
        }
        if target > arr[arr.len() - 1] {
            return arr.len() - 1;
        }

        let mut l: usize = 0;
        let mut r: usize = arr.len() - 1;
        let mut mid: usize = 0;
        while l <= r {
            mid = (l + r) / 2;
            if arr[mid] == target {
                return mid;
            }
            if arr[mid] > target {
                if target > arr[mid - 1] {
                    return Self::get_closest_pos(&arr, mid - 1, mid, target);
                }
                r = mid - 1;
            } else {
                if target < arr[mid + 1] {
                    return Self::get_closest_pos(&arr, mid, mid + 1, target);
                }
                l = mid + 1;
            }
        }

        mid
    }

    fn get_closest_pos(arr: &Vec<i32>, pos_1: usize, pos_2: usize, target: i32) -> usize {
        if target - arr[pos_1] > arr[pos_2] - target {
            return pos_2;
        }
        pos_1
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_find_closest_elements_case_1() {
        // arrange
        let arr: Vec<i32> = vec![1, 2, 3, 4, 5];
        let k: i32 = 4;
        let x: i32 = 3;
        let expected: Vec<i32> = vec![1, 2, 3, 4];

        // act
        let actual = Solution::find_closest_elements(arr, k, x);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn test_find_closest_elements_case_2() {
        // arrange
        let arr: Vec<i32> = vec![1, 2, 3, 4, 5];
        let k: i32 = 4;
        let x: i32 = -1;
        let expected: Vec<i32> = vec![1, 2, 3, 4];

        // act
        let actual = Solution::find_closest_elements(arr, k, x);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn test_find_closest_elements_case_3() {
        // arrange
        let arr: Vec<i32> = vec![1, 2, 3, 4, 5];
        let k: i32 = 4;
        let x: i32 = 6;
        let expected: Vec<i32> = vec![2, 3, 4, 5];

        // act
        let actual = Solution::find_closest_elements(arr, k, x);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn test_find_closest_elements_case_4() {
        // arrange
        let arr: Vec<i32> = vec![1, 1, 1, 10, 10, 10];
        let k: i32 = 1;
        let x: i32 = 9;
        let expected: Vec<i32> = vec![10];

        // act
        let actual = Solution::find_closest_elements(arr, k, x);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn test_find_closest_elements_case_5() {
        // arrange
        let arr: Vec<i32> = vec![1, 2, 3, 4, 5];
        let k: i32 = 4;
        let x: i32 = 4;
        let expected: Vec<i32> = vec![2, 3, 4, 5];

        // act
        let actual = Solution::find_closest_elements(arr, k, x);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn test_find_closest_elements_case_6() {
        // arrange
        let arr: Vec<i32> = vec![0, 1, 1, 1, 2, 3, 6, 7, 8, 9];
        let k: i32 = 9;
        let x: i32 = 4;
        let expected: Vec<i32> = vec![0, 1, 1, 1, 2, 3, 6, 7, 8];

        // act
        let actual = Solution::find_closest_elements(arr, k, x);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn test_find_closest_elements_case_7() {
        // arrange
        let arr: Vec<i32> = vec![-2, -1, 1, 2, 3, 4, 5];
        let k: i32 = 7;
        let x: i32 = 3;
        let expected: Vec<i32> = vec![-2, -1, 1, 2, 3, 4, 5];

        // act
        let actual = Solution::find_closest_elements(arr, k, x);

        // assert
        assert_eq!(expected, actual);
    }
}
