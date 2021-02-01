use whiteread::parse_line;

fn main() {
    let n: isize = parse_line().unwrap();
    let a: Vec<isize> = parse_line().unwrap();

    let avg: isize = ((a.iter().cloned().fold(0, |sum, i| sum + i)) as f64 / n as f64).round() as isize;
    let mut cost: isize = 0;

    for e in a.iter() {
        cost = cost + (e - avg) * (e - avg);
    }
    println!("{}", cost);
}
