use whiteread::parse_line;

fn main() {
    let (a, b, c): (i32, i32, i32) = parse_line().unwrap();
    if a + b + c <= 21 {
        println!("win");
    } else {
        println!("bust");
    }
}
