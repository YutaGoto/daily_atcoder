use whiteread::parse_line;

fn main() {
    let (a, b, k): (usize, usize, usize) = parse_line().unwrap();
    let mut c: usize = 0;

    for i in (1..101).rev() {
        if a % i == 0 && b % i == 0 {
            c = c + 1;
            if c == k {
                println!("{}", i);
            }
        }
    }
}
