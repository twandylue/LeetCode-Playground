struct Solution {}

impl Solution {
    pub fn simplify_path(path: String) -> String {
        let mut path: Vec<char> = path.chars().collect();
        path.push('/');
        let mut stack: Vec<String> = Vec::new();
        let mut curr: Vec<char> = Vec::new();
        for i in 0..path.len() {
            if path[i] == '/' {
                let curr_string: String = curr.iter().collect::<String>();
                if curr_string == "..".to_string() {
                    if stack.len() > 0 {
                        stack.pop().unwrap();
                    }
                } else if curr_string != ".".to_string() && !curr.is_empty() {
                    stack.push(curr_string);
                }
                curr.clear();
            } else {
                curr.push(path[i]);
            }
        }

        "/".to_string() + &stack[..].join("/")
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn daily_simplify_path_case_1() {
        // arrange
        let path: String = "/home/".to_string();
        let expected: String = "/home".to_string();

        // act
        let actual = Solution::simplify_path(path);

        assert_eq!(expected, actual);
    }

    #[test]
    fn daily_simplify_path_case_2() {
        // arrange
        let path: String = "/../".to_string();
        let expected: String = "/".to_string();

        // act
        let actual = Solution::simplify_path(path);

        assert_eq!(expected, actual);
    }

    #[test]
    fn daily_simplify_path_case_3() {
        // arrange
        let path: String = "/home/user/Documents/../Pictures".to_string();
        let expected: String = "/home/user/Pictures".to_string();

        // act
        let actual = Solution::simplify_path(path);

        assert_eq!(expected, actual);
    }
}
