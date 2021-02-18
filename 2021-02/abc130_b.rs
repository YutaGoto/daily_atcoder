use whiteread::parse_line;

fn main() {
    let (_n, x): (usize, usize) = parse_line().unwrap();
    let l: Vec<usize> = parse_line().unwrap();

    let mut cp: usize = 0;
    let mut b: usize = 1;

    for e in l.iter() {
        cp = cp + e;
        if cp <= x {
            b = b + 1;
        } else {
            break;
        }
    }
    println!("{}", b);
}
