use whiteread::parse_line;

fn main() {
    let s: String = parse_line().unwrap();
    let addition: usize = s.matches("o").count();
    println!("{}", 700 + addition * 100);
}
