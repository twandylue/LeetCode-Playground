use std::cmp::Reverse;
use std::collections::BinaryHeap;

struct KthLargest {
    heap: BinaryHeap<Reverse<i32>>,
    k: i32,
}

/**
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl KthLargest {
    fn new(k: i32, nums: Vec<i32>) -> Self {
        let mut heap = BinaryHeap::new();
        for n in nums {
            heap.push(Reverse(n))
        }

        while heap.len() > k as usize {
            heap.pop().unwrap();
        }

        Self { heap, k }
    }

    fn add(&mut self, val: i32) -> i32 {
        self.heap.push(Reverse(val));
        if self.heap.len() > self.k as usize {
            self.heap.pop().unwrap();
        }

        return self.heap.peek().unwrap().0;
    }
}

/**
 * Your KthLargest object will be instantiated and called as such:
 * let obj = KthLargest::new(k, nums);
 * let ret_1: i32 = obj.add(val);
 */

#[cfg(test)]
mod test {
    use super::KthLargest;

    #[test]
    fn kth_largest_case_1() {
        let mut kth_largest = KthLargest::new(3, vec![4, 5, 8, 2]);
        assert_eq!(4, kth_largest.add(3));
        assert_eq!(5, kth_largest.add(5));
        assert_eq!(5, kth_largest.add(10));
        assert_eq!(8, kth_largest.add(9));
        assert_eq!(8, kth_largest.add(4));
    }

    #[test]
    fn kth_largest_case_2() {
        let mut kth_largest = KthLargest::new(7, vec![-10, 1, 3, 1, 4, 10, 3, 9, 4, 5, 1]);
        assert_eq!(3, kth_largest.add(3));
        assert_eq!(3, kth_largest.add(2));
        assert_eq!(3, kth_largest.add(3));
        assert_eq!(3, kth_largest.add(1));
        assert_eq!(3, kth_largest.add(2));
        assert_eq!(3, kth_largest.add(4));
        assert_eq!(4, kth_largest.add(5));
        assert_eq!(4, kth_largest.add(5));
        assert_eq!(4, kth_largest.add(6));
        assert_eq!(5, kth_largest.add(7));
        assert_eq!(5, kth_largest.add(7));
        assert_eq!(5, kth_largest.add(8));
        assert_eq!(5, kth_largest.add(2));
        assert_eq!(5, kth_largest.add(3));
        assert_eq!(5, kth_largest.add(1));
        assert_eq!(5, kth_largest.add(1));
        assert_eq!(5, kth_largest.add(1));
        assert_eq!(6, kth_largest.add(10));
        assert_eq!(7, kth_largest.add(11));
        assert_eq!(7, kth_largest.add(5));
        assert_eq!(7, kth_largest.add(6));
        assert_eq!(7, kth_largest.add(2));
        assert_eq!(7, kth_largest.add(4));
        assert_eq!(7, kth_largest.add(7));
        assert_eq!(7, kth_largest.add(8));
        assert_eq!(7, kth_largest.add(5));
        assert_eq!(7, kth_largest.add(6));
    }
}
