use whiteread::parse_line;

fn main() {
    let s: String = parse_line().unwrap();
    let pcount: usize = s.matches("+").count();
    let mcount: usize = s.matches("-").count();
    println!("{}", pcount as isize - mcount as isize);
}
