use whiteread::parse_line;

fn main() {
    let (a, op, b): (isize, String, isize) = parse_line().unwrap();
    if op == "+".to_string() {
        println!("{}", a + b);
    } else if op == "-".to_string() {
        println!("{}", a - b);
    }
}
