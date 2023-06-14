struct StockSpanner {
    stack: Vec<(i32, i32)>,
}

/**
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl StockSpanner {
    fn new() -> Self {
        let stock_spanner = Self { stack: Vec::new() };

        stock_spanner
    }

    fn next(&mut self, price: i32) -> i32 {
        let mut span: i32 = 1;
        loop {
            match self.stack.iter().last() {
                Some(&(val, _)) => {
                    if val > price {
                        self.stack.push((price, span));
                        break;
                    } else {
                        let (_, s) = self.stack.pop().unwrap();
                        span += s;
                    }
                }
                None => {
                    self.stack.push((price, span));
                    return span;
                }
            }
        }

        return span;
    }
}

/**
 * Your StockSpanner object will be instantiated and called as such:
 * let obj = StockSpanner::new();
 * let ret_1: i32 = obj.next(price);
 */
#[cfg(test)]
mod test {
    use super::*;

    #[test]
    fn online_stock_span_case_1() {
        let mut stock = StockSpanner::new();
        assert_eq!(stock.next(100), 1);
        assert_eq!(stock.next(80), 1);
        assert_eq!(stock.next(60), 1);
        assert_eq!(stock.next(70), 2);
        assert_eq!(stock.next(60), 1);
        assert_eq!(stock.next(75), 4);
        assert_eq!(stock.next(85), 6);
    }

    #[test]
    fn online_stock_span_case_2() {
        let mut stock = StockSpanner::new();
        assert_eq!(stock.next(31), 1);
        assert_eq!(stock.next(41), 2);
        assert_eq!(stock.next(48), 3);
        assert_eq!(stock.next(59), 4);
        assert_eq!(stock.next(79), 5);
    }
}
