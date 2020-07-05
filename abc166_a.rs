use whiteread::parse_line;

fn main() {
    let s: String = parse_line().unwrap();
    if s == "ABC" {
        println!("ARC");
    } else {
        println!("ABC");
    }
}
