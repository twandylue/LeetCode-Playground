use std::collections::HashMap;

pub struct Solution {}

impl Solution {
    // NOTE: Another way can work
    // pub fn top_k_frequent(nums: Vec<i32>, k: i32) -> Vec<i32> {
    //     let mut result: Vec<i32> = Vec::new();
    //     let mut occur_map: HashMap<i32, i32> = HashMap::new();
    //     let mut bucket: Vec<Vec<i32>> = Vec::new();
    //     for _ in 0..nums.len() + 1 {
    //         bucket.push(Vec::new());
    //     }
    //     for num in nums.iter() {
    //         occur_map.entry(*num).and_modify(|x| *x += 1).or_insert(1);
    //     }
    //     for (key, val) in occur_map.iter() {
    //         bucket[*val as usize].push(*key);
    //     }
    //     let mut i: usize = 0;
    //     let mut k: i32 = k;
    //     while k > 0 && i < nums.len() {
    //         let idx: usize = nums.len() - i;
    //         if bucket[idx].len() > 0 {
    //             k -= bucket[idx].len() as i32;
    //             result.append(&mut bucket[idx]);
    //         }
    //         i += 1;
    //     }
    //     result
    // }

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

        let mut count: i32 = k;
        let mut i: usize = 0;
        loop {
            if count <= 0 || i > nums.len() {
                break;
            }

            let index: usize = nums.len() - i;
            if bucket[index].len() != 0 {
                count -= bucket[index].len() as i32;
                res.append(&mut bucket[index]);
            }
            i += 1;
        }

        return res;
    }
}

#[cfg(test)]
mod test {
    use super::Solution;

    #[test]
    fn top_k_frequent_case_1() {
        // arrange
        let input = vec![1, 1, 1, 2, 2, 3];
        let k = 2;
        let expected = vec![1, 2];

        // act
        let mut actual = Solution::top_k_frequent(input, k);

        // assert
        actual.sort();
        assert_eq!(actual, expected);
    }

    #[test]
    fn top_k_frequent_case_2() {
        // arrange
        let input = vec![4, 1, -1, 2, -1, 2, 3];
        let k = 2;
        let expected = vec![-1, 2];

        // act
        let mut actual = Solution::top_k_frequent(input, k);

        // assert
        actual.sort();
        assert_eq!(actual, expected);
    }
}
