use std::collections::HashMap;

pub struct Solution {}

impl Solution {
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        let mut map: HashMap<i32, i32> = HashMap::new();
        let mut res: Vec<i32> = Vec::new();
        for i in 0..nums.len() {
            let remains = target - nums[i];
            if map.contains_key(&nums[i]) {
                res.push(i as i32);
                res.push(map[&nums[i]]);
            } else {
                map.insert(remains, i as i32);
            }
        }

        return res;
    }

    pub fn two_sum2(nums: Vec<i32>, target: i32) -> Vec<i32> {
        let mut map: HashMap<i32, i32> = HashMap::new();
        let mut res: Vec<i32> = Vec::new();
        for i in 0..nums.len() {
            let remains = target - nums[i];
            match map.get(&remains) {
                Some(index) => {
                    res.push(*index);
                    res.push(i as i32);
                }
                None => {
                    map.insert(nums[i], i as i32);
                }
            }
        }

        return res;
    }

    pub fn tests() {
        let nums = vec![2, 7, 11, 15];
        let target = 9;
        let mut res = Solution::two_sum(nums.clone(), target);
        res.sort_by(|a, b| a.cmp(b));
        let mut res2 = Solution::two_sum2(nums.clone(), target);
        res2.sort_by(|a, b| a.cmp(b));
        assert_eq!(res, vec![0, 1]);
        assert_eq!(res2, vec![0, 1]);
    }
}
