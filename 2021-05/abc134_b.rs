use whiteread::parse_line;

fn main() {
    let (n, d): (usize, usize) = parse_line().unwrap();
    let k: usize = 1 + 2 * d;
    let sa: usize = if n % k != 0 {
        n / k + 1
    } else {
        n / k
    };
    println!("{:?}", sa);
}
