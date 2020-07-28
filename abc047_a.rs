use whiteread::parse_line;

fn main() {
    let (a, b, c): (u64, u64, u64) = parse_line().unwrap();
    if a+b == c || b+c == a || c+a == b {
        println!("Yes");
    } else {
        println!("No");
    }
}
