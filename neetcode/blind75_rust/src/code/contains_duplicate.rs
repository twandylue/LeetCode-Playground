use std::collections::HashSet;

pub struct Solution {}

impl Solution {
    pub fn contains_duplicate1(nums: Vec<i32>) -> bool {
        let mut set: HashSet<i32> = HashSet::new();
        for i in nums {
            if set.contains(&i) {
                return true;
            } else {
                set.insert(i);
            }
        }
        return false;
    }

    pub fn contains_duplicate2(nums: Vec<i32>) -> bool {
        let mut set: HashSet<i32> = HashSet::new();
        let mut res = false;

        nums.iter().for_each(|x| {
            if set.contains(x) {
                res = true
            } else {
                set.insert(*x);
            }
        });

        return res;
    }

    pub fn tests() {
        let input1 = vec![1, 2, 32, 32];
        let res1 = Solution::contains_duplicate1(input1);
        let input2 = vec![1, 2, 32];
        let res2 = Solution::contains_duplicate1(input2);

        let input3 = vec![1, 2, 32, 32];
        let res3 = Solution::contains_duplicate2(input3);
        let input4 = vec![1, 2, 32];
        let res4 = Solution::contains_duplicate2(input4);

        assert_eq!(res1, true);
        assert_eq!(res2, false);
        assert_eq!(res3, true);
        assert_eq!(res4, false);
    }
}
