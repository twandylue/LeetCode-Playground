use super::super::models::list_node::ListNode;

pub fn convert_vec_to_linked_list(vector: Vec<i32>) -> Option<Box<ListNode>> {
    if vector.len() == 0 {
        return None;
    } else {
        return Some(Box::new(ListNode {
            val: vector[0],
            next: convert_vec_to_linked_list(vector[1..].to_vec()),
        }));
    }
}
