use whiteread::parse_line;

fn main() {
    let (n, _m): (usize, usize) = parse_line().unwrap();
    let v: Vec<usize> = parse_line().unwrap();
    let homeworks: usize = v.iter().sum();
    if homeworks > n {
        println!("-1");
    } else {
        println!("{}", n - homeworks);
    }
}
