use whiteread::parse_line;

fn main() {
    let (k, x): (usize, usize) = parse_line().unwrap();
    if 500 * k >= x {
        println!("Yes");
    } else {
        println!("No");
    }
}
