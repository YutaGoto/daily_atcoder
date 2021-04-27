use std::collections::HashSet;
use whiteread::parse_line;

fn main() {
    let _n: usize = parse_line().unwrap();
    let v: Vec<char> = parse_line().unwrap();
    let c: HashSet<char> = v.into_iter().collect();

    if c.len() == 3 {
        println!("Three");
    } else {
        println!("Four");
    }
}
