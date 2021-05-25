use whiteread::parse_line;

fn main() {
    let (h, _w): (usize, usize) = parse_line().unwrap();
    for _i in 0..h {
        let c: String = parse_line().unwrap();
        println!("{}", c);
        println!("{}", c);
    }
}
