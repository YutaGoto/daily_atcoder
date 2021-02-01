use whiteread::parse_line;

fn main() {
    let (a, b, c): (i32, i32, i32) = parse_line().unwrap();
    
    if a == b {
        println!("{}", c)
    } else if b == c {
        println!("{}", a)
    } else {
        println!("{}", b)
    }
}
