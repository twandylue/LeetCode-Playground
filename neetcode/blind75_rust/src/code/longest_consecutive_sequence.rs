use std::{cmp, collections::HashSet};

pub struct Solution {}

impl Solution {
    pub fn longest_consecutive(nums: Vec<i32>) -> i32 {
        let mut res = 0;
        let mut p = 0;
        // let set: HashSet<i32> = HashSet::from(nums); -- OK
        let set: HashSet<i32> = nums.clone().into_iter().collect();
        nums.iter().for_each(|x| {
            let mut num = *x;
            if !set.contains(&(num - 1)) {
                p = 0;
                while set.contains(&num) {
                    p += 1;
                    num += 1;
                }
                res = cmp::max(res, p);
            }
        });

        return res;
    }

    pub fn tests() {
        let input = vec![100, 4, 200, 1, 3, 2];
        let expected = 4;
        let actual = Solution::longest_consecutive(input);

        assert_eq!(actual, expected);

        let input2 = vec![1, 2, 3, 4, 5];
        let expected2 = 5;
        let actual2 = Solution::longest_consecutive(input2);

        assert_eq!(actual2, expected2);
    }
}
