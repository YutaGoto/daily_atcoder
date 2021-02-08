use whiteread::parse_line;
use std::process;

fn isPrime(num: usize) -> bool {
    if num == 1 {
        return  false;
    }

    for i in 2..((num as f32).sqrt() as usize + 1) {
        if num % i == 0 {
            return false;
        }
    }
    return true;
}

fn main() {
    let n: usize = parse_line().unwrap();

    for i in n..100004 {
        if isPrime(i) {
            println!("{}", i);
            process::exit(0x0100);
        }
    }
}
