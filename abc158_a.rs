use whiteread::parse_line;

fn main() {
    let s: String = parse_line().unwrap();
    if s == "AAA" || s == "BBB" {
        println!("No");
    } else {
        println!("Yes");
    }
}
