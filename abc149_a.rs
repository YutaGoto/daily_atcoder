use whiteread::parse_line;

fn main() {
    let (s, t): (String, String) = parse_line().unwrap();
    println!("{}{}", t, s);
}
