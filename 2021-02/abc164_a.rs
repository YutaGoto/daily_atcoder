use whiteread::parse_line;

fn main() {
    let (s, w): (usize, usize) = parse_line().unwrap();
    if w >= s {
        println!("unsafe");
    } else {
        println!("safe");
    }
}
