use whiteread::parse_line;

fn main() {
    let s: String = parse_line().unwrap();
    let t: Vec<&str> = s.split(',').collect();
    let u: String = t.join(" ");
    println!("{}", u);
}
