use whiteread::parse_line;

fn main() {
    let n: usize = parse_line().unwrap();
    let v: Vec<usize> = parse_line().unwrap();
    let mut vc = v.clone();
    vc.sort();
    let a: usize = vc[n/2 - 1];
    let b: usize = vc[n/2];

    for e in v.iter() {
        if e <= &a {
            println!("{}", b)
        } else {
            println!("{}", a)
        }
    }
}
