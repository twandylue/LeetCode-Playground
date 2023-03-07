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
    // @return: if a person could attend all meetings
    pub fn can_attend_meetings(mut intervals: Vec<Interval>) -> bool {
        let mut end = i32::MIN;
        intervals.sort_by_key(|x| x.end);
        for i in intervals {
            if i.start >= end {
                end = i.end;
            } else {
                return false;
            }
        }

        true
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
        let expected = false;
        let actual = Solution::can_attend_meetings(intervals);

        assert_eq!(expected, actual);
    }

    #[test]
    fn case_2() {
        let intervals = vec![Interval::new(5, 8), Interval::new(9, 5)];
        let expected = true;
        let actual = Solution::can_attend_meetings(intervals);

        assert_eq!(expected, actual);
    }
}
