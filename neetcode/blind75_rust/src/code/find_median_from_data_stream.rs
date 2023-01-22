// ref: https://doc.rust-lang.org/stable/std/collections/struct.BinaryHeap.html
use std::{cmp::Reverse, collections::BinaryHeap};

struct MedianFinder {
    small: BinaryHeap<i32>,
    large: BinaryHeap<Reverse<i32>>,
}

/**
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl MedianFinder {
    fn new() -> Self {
        MedianFinder {
            small: BinaryHeap::new(),
            large: BinaryHeap::new(),
        }
    }

    fn add_num(&mut self, num: i32) {
        if self.large.len() > 0 && num > self.large.peek().unwrap().0 {
            self.large.push(Reverse(num))
        } else {
            self.small.push(num)
        }

        if self.small.len() > self.large.len() + 1 {
            let val = self.small.pop().unwrap();
            self.large.push(Reverse(val));
        } else if self.large.len() > self.small.len() + 1 {
            let val = self.large.pop().unwrap().0;
            self.small.push(val);
        }
    }

    fn find_median(&self) -> f64 {
        if self.small.len() > self.large.len() {
            return self.small.peek().unwrap().clone().into();
        } else if self.small.len() < self.large.len() {
            return self.large.peek().unwrap().clone().0.into();
        } else {
            return (self.small.peek().unwrap().clone() as f64
                + self.large.peek().unwrap().clone().0 as f64)
                / 2_f64;
        }
    }
}

/**
 * Your MedianFinder object will be instantiated and called as such:
 * let obj = MedianFinder::new();
 * obj.add_num(num);
 * let ret_2: f64 = obj.find_median();
 */

#[cfg(test)]
mod tests {
    use super::MedianFinder;

    #[test]
    fn case_1() {
        let mut median_finder = MedianFinder::new();
        median_finder.add_num(1); // arr = [1]
        median_finder.add_num(2); // arr = [1, 2]
        assert_eq!(1.5, median_finder.find_median()); // return 1.5 (i.e., (1 + 2) / 2)
        median_finder.add_num(3); // arr[1, 2, 3]
        assert_eq!(2.0, median_finder.find_median()); // return 2.0
    }
}
