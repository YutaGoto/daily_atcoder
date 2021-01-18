use whiteread::parse_line;

fn main() {
    let s: String = parse_line().unwrap();
    let d: String = "2018".to_string() + &s[4..];

    println!("{}", d);
}
