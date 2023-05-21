pub struct Solution {}

pub trait FsmExtensions {
    fn to_fsm_event(&self) -> usize;
}

impl FsmExtensions for char {
    fn to_fsm_event(&self) -> usize {
        match self {
            '+' | '-' => 2,
            '.' => 3,
            'e' | 'E' => 4,
            other => {
                if other.is_ascii_digit() {
                    return 1;
                }

                return 0;
            }
        }
    }
}

// NOTE: [decimal]e[integer]
pub const FSM: [[usize; 5]; 12] = [
    [0, 0, 0, 0, 0],  // Failed
    [0, 2, 3, 5, 0],  // start (decimal)
    [0, 2, 0, 7, 8],  // digit (decimal)
    [0, 4, 0, 5, 0],  // sign (decimal)
    [0, 4, 0, 7, 8],  // digit after sign (decimal)
    [0, 6, 0, 0, 0],  // dot (decimal)
    [0, 6, 0, 0, 8],  // digit after dot (decimal)
    [0, 6, 0, 0, 8],  // dot after digit (decimal)
    [0, 9, 10, 0, 0], // start (integer)
    [0, 9, 0, 0, 0],  // digit (integer)
    [0, 11, 0, 0, 0], // sign (integer)
    [0, 11, 0, 0, 0], // digit after sign (integer)
];

impl Solution {
    pub fn is_number(s: String) -> bool {
        let mut state = 1;
        for c in s.chars() {
            state = FSM[state][c.to_fsm_event()];
        }

        state == 2 || state == 4 || state == 6 || state == 7 || state == 9 || state == 11
    }
}

#[cfg(test)]
mod test {
    use super::Solution;

    #[test]
    fn case_1() {
        // arrange
        let s = "0".to_string();
        let expected = true;

        // act
        let actual = Solution::is_number(s);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn case_2() {
        // arrange
        let s = "e".to_string();
        let expected = false;

        // act
        let actual = Solution::is_number(s);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn case_3() {
        // arrange
        let s = ".".to_string();
        let expected = false;

        // act
        let actual = Solution::is_number(s);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn case_4() {
        // arrange
        let s = "3.".to_string();
        let expected = true;

        // act
        let actual = Solution::is_number(s);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn case_5() {
        // arrange
        let s = "0e".to_string();
        let expected = false;

        // act
        let actual = Solution::is_number(s);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn case_6() {
        // arrange
        let s = "2e0".to_string();
        let expected = true;

        // act
        let actual = Solution::is_number(s);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn case_7() {
        // arrange
        let s = "test".to_string();
        let expected = false;

        // act
        let actual = Solution::is_number(s);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn case_8() {
        // arrange
        let s = "-1.".to_string();
        let expected = true;

        // act
        let actual = Solution::is_number(s);

        // assert
        assert_eq!(expected, actual);
    }
}
