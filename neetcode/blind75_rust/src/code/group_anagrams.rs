use std::collections::HashMap;

pub struct Solution {}

impl Solution {
    pub fn group_anagrams(strs: Vec<String>) -> Vec<Vec<String>> {
        let mut map: HashMap<String, Vec<String>> = HashMap::new();
        strs.iter().for_each(|str| {
            let mut v: Vec<u8> = str.chars().map(|x| x as u8).collect();
            v.sort_by(|a, b| a.cmp(b));
            let ordered_string = String::from_utf8(v).unwrap();

            if map.contains_key(&ordered_string) {
                if let Some(val) = map.get_mut(&ordered_string) {
                    val.push(str.to_string());
                } else {
                    return;
                }
            } else {
                map.insert(ordered_string, vec![str.to_string()]);
            }
        });

        let res: Vec<Vec<String>> = map.values().map(|x| x.clone()).collect();

        return res;
    }
}

#[cfg(test)]
mod test {
    use super::Solution;
    #[test]
    fn case_1() {
        let input: Vec<String> = vec!["eat", "tea", "tan", "ate", "nat", "bat"]
            .iter()
            .map(|x| x.to_string())
            .collect();

        let mut expected = vec![vec!["bat"], vec!["nat", "tan"], vec!["ate", "eat", "tea"]];
        let mut actual = Solution::group_anagrams(input);

        expected
            .iter_mut()
            .zip(actual.iter_mut())
            .for_each(|(e, a)| {
                e.sort();
                a.sort();
            });
        expected.sort();
        actual.sort();

        assert_eq!(actual, expected);
    }
}
