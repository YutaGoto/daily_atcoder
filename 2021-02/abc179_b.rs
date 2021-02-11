use whiteread::parse_line;
use std::process;

fn main() {
    let n: usize = parse_line().unwrap();
    let mut c: usize = 0;

    for _i in 0..n {
        let (a, b): (i32, i32) = parse_line().unwrap();
        if a == b {
            c = c + 1;
        } else {
            c = 0;
        }

        if c == 3 {
            println!("Yes");
            process::exit(0x0100);
        }
    }

    println!("No");
}
