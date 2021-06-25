use whiteread::parse_line;

fn main() {
    let (m, n): (isize, isize) = parse_line().unwrap();
    let ans = m * (m-1) / 2 + n * (n-1) / 2;
    println!("{}", ans);
}
