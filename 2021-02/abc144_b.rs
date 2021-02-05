use whiteread::parse_line;
use std::process;

fn main() {
    let n: usize = parse_line().unwrap();
    for i in 1..10 {
        if n % i == 0 && n / i <= 9 {
            println!("Yes");
            process::exit(0x0100);
        }
    }
    println!("No");
}
