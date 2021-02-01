use whiteread::parse_line;

fn main() {
    let n: String = parse_line().unwrap();
    println!("ABC{}", n);
}
