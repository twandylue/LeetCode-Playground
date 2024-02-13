/**
 * Forward declaration of guess API.
 * @param  num   your guess
 * @return 	     -1 if num is higher than the picked number
 *			      1 if num is lower than the picked number
 *               otherwise return 0
 * unsafe fn guess(num: i32) -> i32 {}
 */
// NOTE: Temporary for compilation
unsafe fn guess(num: i32) -> i32 {
    return num;
}

struct Solution {}

impl Solution {
    unsafe fn guessNumber(n: i32) -> i32 {
        let mut result: i32 = 0;
        let mut l: usize = 0;
        let mut r: usize = n as usize;
        while l <= r {
            let mid: usize = (l + r) / 2;
            result = mid as i32;
            if guess(mid as i32) == 0 {
                return mid as i32;
            }
            if guess(mid as i32) == -1 {
                r = mid - 1;
            } else {
                l = mid + 1;
            }
        }

        result
    }
}
