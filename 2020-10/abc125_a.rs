use whiteread::parse_line;

fn main() {
    let (a, b, t): (i32, i32, i32) = parse_line().unwrap();
    println!("{}", t / a * b);
}
