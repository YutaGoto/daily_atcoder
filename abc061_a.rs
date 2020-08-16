use whiteread::parse_line;

fn main() {
    let (a, b, c): (i32, i32, i32) = parse_line().unwrap();

    if a <= c && b >= c {
        println!("Yes");
    } else {
        println!("No");
    }
}
