use whiteread::parse_line;

fn main() {
    let n: usize = parse_line().unwrap();
    let mut i: usize = 0;

    let mut v: Vec<usize> = Vec::new();

    while i < n {
        let t: usize = parse_line().unwrap();
        v.push(t);
        i = i + 1;
    }

    v.sort();
    v[n-1] = v[n-1] / 2;
    println!("{}", v.iter().cloned().fold(0, |sum, i| sum + i));
}
