use whiteread::parse_line;
use std::process;

fn main() {
    let n: usize = parse_line().unwrap();
    if n < 4 {
        println!("No");
        process::exit(0x0100);
    }

    for c in 0..26 {
        for d in 0..15 {
            if n == c*d {
                println!("Yes");
                process::exit(0x0100);
            } else if n < c*d {
                break;
            }
        }
    }
    println!("No");
}
