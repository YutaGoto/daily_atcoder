use whiteread::parse_line;
use std::process;

fn main() {
    let n: usize = parse_line().unwrap();

    if n <= 2 {
        println!("0");
        process::exit(0x0100);
    } else if n == 3 {
        println!("1");
        process::exit(0x0100);
    }

    let mut k1: usize = 0;
    let mut k2: usize = 0;
    let mut k3: usize = 1;
    let mut tm: usize = 1;

    for _i in 0..(n-3) {
        tm = k3 + k2 + k1;
        k1 = k2;
        k2 = k3;
        k3 = tm % 10007;
    }

    let ans: usize = k3 % 10007;
    println!("{}", ans);
}
