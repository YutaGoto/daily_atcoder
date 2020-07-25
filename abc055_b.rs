use whiteread::parse_line;

fn main() {
    let n: usize = parse_line().unwrap();
    let mut i: usize = 1;
    let mut p: usize = 1;
    while i <= n {
        p = p*i % 1000000007;
        i = i+1;
    }
    println!("{}", (p % 1000000007));
}
