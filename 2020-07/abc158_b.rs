use whiteread::parse_line;

fn main() {
    let (n, a, b): (i64, i64, i64) = parse_line().unwrap();
    let t: i64 = n / (a+b);
    let mut ac: i64 = t * a;

    let t: i64 = n % (a+b);
    if t != 0 {
        if t <= a {
            ac = ac + t;
        } else {
            ac = ac + a;
        }
    }

    println!("{}", ac);
}
