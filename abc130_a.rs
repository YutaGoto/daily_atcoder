use whiteread::parse_line;

fn main() {
    let (x, r): (usize, usize) = parse_line().unwrap();

    if x < r {
        println!("0");
    } else {
        println!("10");
    }
}
