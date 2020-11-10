use whiteread::parse_line;

fn main() {
    let s: String = parse_line().unwrap();
    if s.starts_with("RS") {
        println!("1");
    } else {
        println!("{}", s.matches("R").count());
    }
}
