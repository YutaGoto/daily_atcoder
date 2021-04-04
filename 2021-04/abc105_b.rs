use whiteread::parse_line;
use std::process;

fn main() {
    let n: usize = parse_line().unwrap();
    if n < 4 {
        println!("No");
        process::exit(0x0100);
    }

    for c in 0..27 {
        for d in 0..16 {
            let cost: usize = 4*c + 7*d;
            if n == cost {
                println!("Yes");
                process::exit(0x0100);
            } else if n < cost {
                break;
            }
        }
    }
    println!("No");
}
