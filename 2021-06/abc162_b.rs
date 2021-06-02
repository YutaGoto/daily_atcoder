use whiteread::parse_line;

fn main() {
    let n: usize = parse_line().unwrap();
    let mut ans: usize = 0;

    for i in 1..=n {
        if i % 3 != 0 && i % 5 != 0 {
            ans = ans + i;
        }
    }
    println!("{}", ans);
}
