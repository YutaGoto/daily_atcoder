use whiteread::parse_line;

fn main() {
    let (n, k, m): (isize, isize, isize) = parse_line().unwrap();
    let v: Vec<isize> = parse_line().unwrap();
    let sum: isize = v.iter().cloned().fold(0, |sum, i| sum + i);
    if k < (m * n) - sum {
        println!("-1");
    } else if 0 >= (m * n) - sum {
        println!("0");
    } else {
        println!("{}", (m * n) - sum);
    }
}
