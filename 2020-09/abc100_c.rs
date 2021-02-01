use whiteread::parse_line;

fn main() {
    let n: usize = parse_line().unwrap();
    let mut v: Vec<i32> = parse_line().unwrap();
    let mut k: usize = 0;
    let mut t: usize = 0;

    while t < n {
        if v[t] % 2 == 0{
            v[t] = v[t] / 2;
            k = k + 1;
        } else {
            t = t + 1;
        }
    }

    println!("{}", k);
}
