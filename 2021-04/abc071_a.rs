use whiteread::parse_line;

fn main() {
    let (x, a, b): (i32, i32, i32) = parse_line().unwrap();
    if (x-a).abs() < (x-b).abs() {
        println!("A");
    } else {
        println!("B");
    }
}
