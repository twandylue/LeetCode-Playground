use crate::code::best_time_to_buy_and_sell_stock::Solution as S121;
use crate::code::container_with_most_water::Solution as S11;
use crate::code::contains_duplicate::Solution as S227;
use crate::code::encode_and_decode_strings::Solution as S659;
use crate::code::find_minimum_in_rotated_sorted_array::Solution as S153;
use crate::code::group_anagrams::Solution as S49;
use crate::code::longest_consecutive_sequence::Solution as S128;
use crate::code::longest_repeating_character_replacement::Solution as S424;
use crate::code::longest_substring_without_repeating_characters::Solution as S3;
use crate::code::merge_two_sorted_lists::Solution as S21;
use crate::code::minimum_window_substring::Solution as S76;
use crate::code::product_of_array_except_self::Solution as S238;
use crate::code::reorder_list::Solution as S143;
use crate::code::reverse_linked_list::Solution as S206;
use crate::code::search_in_rotated_sorted_array::Solution as S33;
use crate::code::three_sum::Solution as S15;
use crate::code::top_k_frequent_elements::Solution as S347;
use crate::code::two_sum::Solution as S1;
use crate::code::valid_anagram::Solution as S242;
use crate::code::valid_palindrome::Solution as S125;
use crate::code::valid_parentheses::Solution as S20;
// use crate::code::valid_sudoku::Solution as S36;

mod code;

fn main() {
    S1::tests();
    S15::tests();
    // S36::tests();
    S49::tests();
    S227::tests();
    S242::tests();
    S347::tests();
    S238::tests();
    S128::tests();
    S125::tests();
    S11::tests();
    S121::tests();
    S3::tests();
    S424::tests();
    S20::tests();
    S76::tests();
    S33::tests();
    S153::tests();
    S206::tests();
    S21::tests();
    S659::tests();
    S143::tests();
}
