use whiteread::parse_line;

fn main() {
    let (n, k): (i64, i64) = parse_line().unwrap();
    let mut pro: f64 = 0.0;
    let mut i: i64 = 1;

    while i <= n {
        let mut j: i64 = i;
        let mut t: i64 = n;
        while j < k {
            j = j * 2;
            t = t * 2;
        }
        pro = pro + (1.0/(t as f64));
        i = i + 1;
    }

    println!("{}", pro);
}
