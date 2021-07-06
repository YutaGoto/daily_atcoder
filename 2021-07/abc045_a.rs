use whiteread::parse_line;

fn main() {
    let a: usize = parse_line().unwrap();
    let b: usize = parse_line().unwrap();
    let h: usize = parse_line().unwrap();
    let area: usize = (a+b)*h/2;
    println!("{}", area);
}
