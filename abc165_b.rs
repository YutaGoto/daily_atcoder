use whiteread::parse_line;

fn main() {
    let x: u64 = parse_line().unwrap();
    let mut b: u64 = 100;
    let mut n: u32 = 0;
    while b < x {
        b = b + b / 100;
        n = n + 1;
    }
    println!("{:?}", n);
}
