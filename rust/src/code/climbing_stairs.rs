pub struct Solution {}

impl Solution {
    pub fn climb_stairs(n: i32) -> i32 {
        if n <= 2 {
            return n;
        }
        let mut steps = Vec::<i32>::from([1, 2]);
        for i in 2..n {
            steps.push(steps[i as usize - 1] + steps[i as usize - 2]);
        }

        return *steps.last().unwrap();
    }

    pub fn climb_stairs_fab(n: i32) -> i32 {
        if n <= 2 {
            return n;
        }

        let mut curr = 1;
        let mut next = 1;
        for _ in 0..n {
            let temp = next;
            next = curr + next;
            curr = temp;
        }

        return curr;
    }
}

#[cfg(test)]
mod tests {
    use super::Solution;

    #[test]
    fn climb_stairs_case_1() {
        let n = 2;
        let expected = 2;
        let actual = Solution::climb_stairs(n);

        assert_eq!(expected, actual);
    }

    #[test]
    fn climb_stairs_case_2() {
        let n = 3;
        let expected = 3;
        let actual = Solution::climb_stairs(n);

        assert_eq!(expected, actual);
    }

    #[test]
    fn climb_stairs_case_3() {
        let n = 2;
        let expected = 2;
        let actual = Solution::climb_stairs_fab(n);

        assert_eq!(expected, actual);
    }

    #[test]
    fn climb_stairs_case_4() {
        let n = 3;
        let expected = 3;
        let actual = Solution::climb_stairs_fab(n);

        assert_eq!(expected, actual);
    }
}
