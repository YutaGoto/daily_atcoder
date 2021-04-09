use whiteread::parse_line;

fn main() {
    let (x, y, z): (usize, usize, usize) = parse_line().unwrap();
    let ans: usize = (x - z) / (z + y);
    println!("{}", ans);
}
