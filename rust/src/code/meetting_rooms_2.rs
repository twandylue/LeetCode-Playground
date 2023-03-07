pub struct Solution;

// Definition of Interval:
#[derive(Debug, PartialEq, Eq)]
pub struct Interval {
    pub start: i32,
    pub end: i32,
}

impl Interval {
    #[inline]
    pub fn new(start: i32, end: i32) -> Self {
        Interval {
            start: start,
            end: end,
        }
    }
}

impl Solution {
    // @param intervals: an array of meeting time intervals
    // @return: the minimum number of conference rooms required
    pub fn min_meeting_rooms(mut intervals: Vec<Interval>) -> i32 {
        let mut res = 0;
        let mut count = 0;
        let mut s = 0;
        let mut e = 0;

        intervals.sort_by_key(|x| x.start);
        let start_times: Vec<i32> = intervals.iter().map(|x| x.start).collect::<Vec<i32>>();
        intervals.sort_by_key(|x| x.end);
        let end_times: Vec<i32> = intervals.iter().map(|x| x.end).collect::<Vec<i32>>();

        while s < intervals.len() {
            if start_times[s] < end_times[e] {
                s += 1;
                count += 1;
            } else {
                e += 1;
                count -= 1;
            }
            res = std::cmp::max(res, count);
        }

        return res;
    }
}

#[cfg(test)]
mod tests {
    use super::{Interval, Solution};

    #[test]
    fn case_1() {
        let intervals = vec![
            Interval::new(0, 30),
            Interval::new(5, 10),
            Interval::new(15, 20),
        ];
        let expected = 2;
        let actual = Solution::min_meeting_rooms(intervals);

        assert_eq!(expected, actual);
    }

    #[test]
    fn case_2() {
        let intervals = vec![Interval::new(2, 7)];
        let expected = 1;
        let actual = Solution::min_meeting_rooms(intervals);

        assert_eq!(expected, actual);
    }
}
