use whiteread::parse_line;

fn main() {
    let r: u32 = parse_line().unwrap();
    println!("{:?}", r * r);
}
