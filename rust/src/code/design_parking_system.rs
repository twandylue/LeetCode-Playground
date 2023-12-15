struct ParkingSystem {
    big_num: i32,
    med_num: i32,
    small_num: i32,
}

/**
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl ParkingSystem {
    fn new(big: i32, medium: i32, small: i32) -> Self {
        ParkingSystem {
            big_num: big,
            med_num: medium,
            small_num: small,
        }
    }

    fn add_car(&mut self, car_type: i32) -> bool {
        match car_type {
            1 => {
                if self.big_num > 0 {
                    self.big_num -= 1;
                    return true;
                }
                return false;
            }
            2 => {
                if self.med_num > 0 {
                    self.med_num -= 1;
                    return true;
                }
                return false;
            }
            3 => {
                if self.small_num > 0 {
                    self.small_num -= 1;
                    return true;
                }
                return false;
            }
            _ => {
                unreachable!("Input is wrong...")
            }
        }
    }
}

/**
 * Your ParkingSystem object will be instantiated and called as such:
 * let obj = ParkingSystem::new(big, medium, small);
 * let ret_1: bool = obj.add_car(carType);
 */

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn parking_system_case_1() {
        // arrange
        let mut park = ParkingSystem::new(1, 1, 0);

        // assert
        assert!(park.add_car(1));
        assert!(park.add_car(2));
        assert!(!park.add_car(3));
        assert!(!park.add_car(1));
    }
}
