use whiteread::parse_line;

fn main() {
    let (k, s): (i32, i32) = parse_line().unwrap();
    let (mut a, mut b, mut c): (i32, i32, i32) = (0, 0, 0);
    let mut t: i32 = 0;

    while a <= k {
        while b <= k {
            c = s - a - b;
            if c <= k && c >= 0 {
                t = t + 1;
            }
            b = b + 1;
        }
        a = a + 1;
        b = 0;
    }
    println!("{}", t);
}
