use whiteread::parse_line;
use num_integer::gcd;

fn main() {
    let (a, b, c, d): (usize, usize, usize, usize) = parse_line().unwrap();
    let cd: usize = c*d / gcd(c, d);

    let bc = b/c;
    let ac = (a-1)/c;
    let bd = b/d;
    let ad = (a-1)/d;
    let bcd = b/cd;
    let acd = (a-1)/cd;

    let cc = bc - ac;
    let dc = bd - ad;
    let cdc = bcd - acd;

    println!("{}", b - a + 1 - cc - dc + cdc);
}
