use whiteread::parse_line;

fn main() {
    let n: i32 = parse_line().unwrap();
    println!("{}", n/2 + n%2);
}
