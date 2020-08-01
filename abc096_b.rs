// 入力例: 2 3
use whiteread::parse_line;

fn main() {
    let (mut a, mut b, mut c): (i32, i32, i32) = parse_line().unwrap();
    let k: i32 = parse_line().unwrap();
    let mut i: i32 = 0;

    while i < k {
        if a >= b && a >= c {
            a = a * 2;
        } else if b >= c {
            b = b * 2;
        } else {
            c = c * 2;
        }
        i = i + 1;
    }

    println!("{}", a+b+c);
}
