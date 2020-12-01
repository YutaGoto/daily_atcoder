use whiteread::parse_line;

fn main() {
    let (h, a): (usize, usize) = parse_line().unwrap();
    let t: usize = h % a;
    if t != 0 {
        println!("{}", h / a + 1);
    } else {
        println!("{}", h / a);
    }
}
