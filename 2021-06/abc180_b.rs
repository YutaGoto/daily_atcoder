use whiteread::parse_line;

fn main() {
    let n: usize = parse_line().unwrap();
    let mut x: Vec<isize> = parse_line().unwrap();

    let mut manhattan: usize = 0;
    let mut euclid: f64 = 0.0;

    for i in 0..n {
        manhattan = manhattan + x[i].abs() as usize;
        euclid = euclid + ((x[i] * x[i]) as f64);
        x[i] = x[i].abs();
    }

    euclid = euclid.sqrt();
    let chebyshev = x.iter().max().unwrap();
    println!("{}", manhattan);
    println!("{}", euclid);
    println!("{}", chebyshev);
}
