use crate::code::contains_duplicate::Solution as S227;
use crate::code::group_anagrams::Solution as S49;
use crate::code::longest_consecutive_sequence::Solution as S128;
use crate::code::product_of_array_except_self::Solution as S238;
use crate::code::top_k_frequent_elements::Solution as S347;
use crate::code::two_sum::Solution as S1;
use crate::code::valid_anagram::Solution as S242;
// use crate::code::valid_sudoku::Solution as S36;
use crate::code::valid_palindrome::Solution as S125;

mod code;

fn main() {
    S1::tests();
    // S36::tests();
    S49::tests();
    S227::tests();
    S242::tests();
    S347::tests();
    S238::tests();
    S128::tests();
    S125::tests();
}
