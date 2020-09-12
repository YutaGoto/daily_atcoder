use whiteread::parse_line;

fn main() {
    let (a, b): (i32, i32) = parse_line().unwrap();
    let mut t: i32 = 1;
    let mut k: i32 = 0;
    while t < b {
      k = k + 1;
      t = t - 1 + a;
    }
    println!("{}", k);
}
