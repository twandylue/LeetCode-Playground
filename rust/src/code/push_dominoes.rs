struct Solution {}

impl Solution {
    pub fn push_dominoes(dominoes: String) -> String {
        use std::collections::VecDeque;

        let mut dominoes: Vec<char> = dominoes.chars().collect();
        let mut que: VecDeque<(usize, char)> = VecDeque::new();
        for i in 0..dominoes.len() {
            if dominoes[i] != '.' {
                que.push_back((i, dominoes[i]));
            }
        }

        while let Some((i, d)) = que.pop_front() {
            if d == 'L' && i > 0 && dominoes[i - 1] == '.' {
                que.push_back((i - 1, 'L'));
                dominoes[i - 1] = 'L';
            }
            if d == 'R' && i < dominoes.len() - 1 && dominoes[i + 1] == '.' {
                if i < dominoes.len() - 2 && dominoes[i + 2] == 'L' {
                    que.pop_front();
                } else {
                    que.push_back((i + 1, 'R'));
                    dominoes[i + 1] = 'R';
                }
            }
        }

        dominoes.into_iter().collect::<String>()
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn push_dominoes_case_1() {
        // arrange
        let dominoes: String = "RR.L".to_string();
        let expected: String = "RR.L".to_string();

        // act
        let actual = Solution::push_dominoes(dominoes);

        // assert
        assert_eq!(expected, actual);
    }

    #[test]
    fn push_dominoes_case_2() {
        // arrange
        let dominoes: String = ".L.R...LR..L..".to_string();
        let expected: String = "LL.RR.LLRRLL..".to_string();

        // act
        let actual = Solution::push_dominoes(dominoes);

        // assert
        assert_eq!(expected, actual);
    }
}
