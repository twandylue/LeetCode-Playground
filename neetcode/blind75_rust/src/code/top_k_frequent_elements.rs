use std::collections::HashMap;

pub struct Solution {}

impl Solution {
    pub fn top_k_frequent(nums: Vec<i32>, k: i32) -> Vec<i32> {
        let mut map: HashMap<i32, i32> = HashMap::new();
        let mut bucket: Vec<Vec<i32>> = vec![Vec::new(); nums.len() + 1];
        let mut res: Vec<i32> = Vec::new();

        nums.iter().for_each(|x| {
            map.entry(*x)
                .and_modify(|counter| *counter += 1)
                .or_insert(1);
        });

        map.iter().for_each(|(k, v)| {
            bucket[*v as usize].push(*k);
        });

        let mut count = k;
        let mut index = nums.len();
        loop {
            if !bucket[index].is_empty() {
                bucket[index].iter().for_each(|x| {
                    res.push(*x);
                    count -= 1;
                });
            }

            index -= 1;
            if count == 0 || index == 0 {
                break;
            }
        }

        return res;
    }

    pub fn tests() {
        let input = vec![1, 1, 1, 2, 2, 3];
        let k = 2;
        let mut actual = Solution::top_k_frequent(input, k);
        actual.sort();
        let expected = vec![1, 2];

        assert_eq!(actual, expected);

        let input2 = vec![4, 1, -1, 2, -1, 2, 3];
        let k2 = 2;
        let mut actual2 = Solution::top_k_frequent(input2, k2);
        actual2.sort();
        let expected2 = vec![-1, 2];

        assert_eq!(actual2, expected2);
    }
}
