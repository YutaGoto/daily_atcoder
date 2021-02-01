use whiteread::parse_line;

fn main() {
    let s: String = parse_line().unwrap();
    let t: String = parse_line().unwrap();
    let u = s.len();

    if s == &t[0..u] {
        println!("Yes");
    } else {
        println!("No");
    }
}
