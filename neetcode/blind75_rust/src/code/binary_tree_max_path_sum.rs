use std::cell::RefCell;
use std::cmp;
use std::rc::Rc;

use super::model::binary_tree_node::TreeNode;

pub struct Solution {}

enum Action<T, U> {
    Caller(T),
    Handler(U),
}

impl Solution {
    pub fn max_path_sum_nonrecurs(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
        let mut stack = Vec::<Action<Option<Rc<RefCell<TreeNode>>>, i32>>::new();
        let mut ret_stack = Vec::<i32>::new();
        let mut res = i32::MIN;
        stack.push(Action::Caller(root));

        while let Some(action) = stack.pop() {
            match action {
                Action::Caller(node) => {
                    if let Some(n) = node {
                        stack.push(Action::Handler(n.borrow().val));
                        stack.push(Action::Caller(n.borrow().right.clone()));
                        stack.push(Action::Caller(n.borrow().left.clone()));
                    } else {
                        ret_stack.push(-1);
                    }
                }
                Action::Handler(number) => {
                    let right = cmp::max(0, ret_stack.pop().unwrap());
                    let left = cmp::max(0, ret_stack.pop().unwrap());
                    ret_stack.push(number + cmp::max(left, right));
                    res = cmp::max(res, number + left + right);
                }
            }
        }

        res
    }

    pub fn max_path_sum(root: Option<Rc<RefCell<TreeNode>>>) -> i32 {
        let mut answer = i32::MIN;
        Solution::helper(&root, &mut answer);
        return answer;
    }

    fn helper(root: &Option<Rc<RefCell<TreeNode>>>, ans: &mut i32) -> i32 {
        if let Some(r) = root {
            let left = cmp::max(0, Solution::helper(&r.borrow().left, ans));
            let right = cmp::max(0, Solution::helper(&r.borrow().right, ans));
            *ans = cmp::max(*ans, r.borrow().val + left + right);
            return r.borrow().val + cmp::max(left, right);
        } else {
            -1
        }
    }
}

#[cfg(test)]
mod tests {
    use crate::code::utils::deserialize_to_binary_tree::deserialize_to_BT;

    use super::Solution;

    #[test]
    fn case_1() {
        let root = deserialize_to_BT(vec![Some(1), Some(2), Some(3)]);
        let expected = 6;
        let actual = Solution::max_path_sum(root);

        assert_eq!(expected, actual);
    }

    #[test]
    fn case_2() {
        let root = deserialize_to_BT(vec![
            Some(-10),
            Some(9),
            Some(20),
            None,
            None,
            Some(15),
            Some(7),
        ]);
        let expected = 42;
        let actual = Solution::max_path_sum(root);

        assert_eq!(expected, actual);
    }

    #[test]
    fn case_3() {
        let root = deserialize_to_BT(vec![Some(1), Some(2), Some(3)]);
        let expected = 6;
        let actual = Solution::max_path_sum_nonrecurs(root);

        assert_eq!(expected, actual);
    }

    #[test]
    fn case_4() {
        let root = deserialize_to_BT(vec![
            Some(-10),
            Some(9),
            Some(20),
            None,
            None,
            Some(15),
            Some(7),
        ]);
        let expected = 42;
        let actual = Solution::max_path_sum_nonrecurs(root);

        assert_eq!(expected, actual);
    }

    #[test]
    fn case_5() {
        let root = deserialize_to_BT(vec![Some(-3)]);
        let expected = -3;
        let actual = Solution::max_path_sum_nonrecurs(root);

        assert_eq!(expected, actual);
    }

    #[test]
    fn case_6() {
        let root = deserialize_to_BT(vec![
            Some(1),
            Some(2),
            None,
            Some(3),
            None,
            Some(4),
            None,
            Some(5),
            None,
            Some(7),
        ]);
        let expected = 22;
        let actual = Solution::max_path_sum_nonrecurs(root);

        assert_eq!(expected, actual);
    }
}
