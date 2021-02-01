use whiteread::parse_line;

fn main() {
    let (n, d): (usize, f64) = parse_line().unwrap();

    let mut c: usize = 0;

    for _i in 0..n {
        let (x, y): (i64, i64) = parse_line().unwrap();
        let distance: f64 = ((x.pow(2) + y.pow(2)) as f64).sqrt();

        if d >= distance {
            c = c + 1;
        }
    }

    println!("{}", c);
}
