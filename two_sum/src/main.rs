use std::collections::HashMap;

fn main() {
    let nums = vec![2, 7, 11, 15];
    let target = 9;

    let ans = two_sum(nums, target);

    println!("{:#?}", ans)
}

fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
    let mut map: HashMap<i32, i32> = HashMap::new();
    for i in 0..nums.len() {
        let remain = target - nums[i];
        let ans = map.get(&remain);
        match ans {
            None => {
                map.insert(nums[i], i as i32);
                continue;
            }
            Some(k) => return vec![*k, i as i32],
        };
    }

    unreachable!()
}
