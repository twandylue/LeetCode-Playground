use std::cmp::Reverse;
use std::collections::{BinaryHeap, HashSet};

struct SeatManager {
    min_heap: BinaryHeap<Reverse<i32>>,
    reversed_seats: HashSet<i32>,
}

/**
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl SeatManager {
    fn new(n: i32) -> Self {
        let mut manager = SeatManager {
            min_heap: BinaryHeap::new(),
            reversed_seats: HashSet::new(),
        };
        for i in 1..n + 1 {
            manager.min_heap.push(Reverse(i));
        }
        manager
    }

    fn reserve(&mut self) -> i32 {
        if let Some(Reverse(seat)) = self.min_heap.pop() {
            self.reversed_seats.insert(seat);
            seat
        } else {
            0
        }
    }

    fn unreserve(&mut self, seat_number: i32) {
        if self.reversed_seats.contains(&seat_number) {
            self.min_heap.push(Reverse(seat_number));
            self.reversed_seats.remove(&seat_number);
        }
    }
}

// /**
//  * Your SeatManager object will be instantiated and called as such:
//  * let obj = SeatManager::new(n);
//  * let ret_1: i32 = obj.reserve();
//  * obj.unreserve(seatNumber);
//  */
#[cfg(test)]
mod tests {
    use super::SeatManager;

    #[test]
    fn seatManager_case_1() {
        // arrange
        let mut seat_manager = SeatManager::new(5);

        // act & assert
        assert_eq!(1, seat_manager.reserve()); // All seats are available, so return the lowest numbered seat, which is 1.
        assert_eq!(2, seat_manager.reserve()); // The available seats are [2,3,4,5], so return the lowest of them, which is 2.
        seat_manager.unreserve(2); // Unreserve seat 2, so now the available seats are [2,3,4,5].
        assert_eq!(2, seat_manager.reserve()); // The available seats are [2,3,4,5], so return the lowest of them, which is 2.
        assert_eq!(3, seat_manager.reserve()); // The available seats are [3,4,5], so return the lowest of them, which is 3.
        assert_eq!(4, seat_manager.reserve()); // The available seats are [4,5], so return the lowest of them, which is 4.
        assert_eq!(5, seat_manager.reserve()); // The only available seat is seat 5, so return 5.
        seat_manager.unreserve(5); // Unreserve seat 5, so now the available seats are [5].
    }
}
