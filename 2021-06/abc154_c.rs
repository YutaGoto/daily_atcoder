use whiteread::parse_line;
use std::process;

fn main() {
    let n: usize = parse_line().unwrap();
    let mut v: Vec<usize> = parse_line().unwrap();
    v.sort();

    for i in 0..(n-1) {
        if v[i] == v[i+1] {
            println!("NO");
            process::exit(0x0100);
        }
    }

    println!("YES");
}
