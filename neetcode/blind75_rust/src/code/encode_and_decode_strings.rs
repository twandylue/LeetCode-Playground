pub struct Solution {}

impl Solution {
    pub fn encode(input: Vec<&str>) -> String {
        let mut ret = String::new();
        input.iter().for_each(|&x| {
            ret.push_str(&format!("{}#{}", x.len(), x));
        });

        return ret;
    }

    pub fn decode(input: String) -> Vec<String> {
        let mut ret: Vec<String> = Vec::new();
        let mut i: usize = 0;
        let input_chars: Vec<char> = input.chars().collect();

        while i < input.len() {
            let mut j = i;
            while input_chars[j] != '#' {
                j += 1;
            }
            let num = input_chars[i..j]
                .into_iter()
                .collect::<String>()
                .parse::<i32>()
                .unwrap();
            let r = input_chars[j + 1..j + 1 + num as usize]
                .into_iter()
                .collect::<String>();
            ret.push(r);
            i = j + 1 + num as usize;
        }

        return ret;
    }

    pub fn tests() {
        let input = vec!["lint", "code", "love", "you"];
        let expected = vec!["lint", "code", "love", "you"];
        let encode_result = Solution::encode(input);
        let decode_result = Solution::decode(encode_result);

        assert_eq!(decode_result, expected);

        let input2 = vec!["we", "say", ":", "yes"];
        let expected2 = vec!["we", "say", ":", "yes"];
        let encode_result2 = Solution::encode(input2);
        let decode_result2 = Solution::decode(encode_result2);

        assert_eq!(decode_result2, expected2);
    }
}
