use whiteread::parse_line;

fn main() {
    let n: usize = parse_line().unwrap();
    let v: Vec<usize> = parse_line().unwrap();

    let mut c: usize = 0;

    for i in 0..(n-1) {
        for j in (i+1)..n {
            c = c + (v[i] * v[j]);
        }
    }

    println!("{}", c);
}
