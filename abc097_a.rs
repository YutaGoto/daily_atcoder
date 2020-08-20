use whiteread::parse_line;

fn main() {
    let (a, b, c, d): (i32, i32, i32, i32) = parse_line().unwrap();

    if (a - c).abs() <= d {
        println!("Yes");
    } else if (a - b).abs() <= d && (b - c).abs() <= d {
        println!("Yes");
    } else {
        println!("No");
    }
}
