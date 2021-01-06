use whiteread::parse_line;

fn main() {
    let n: usize = parse_line().unwrap();
    let p: Vec<usize> = parse_line().unwrap();

    let mut c: usize = 0;

    for i in 1..(n-1) {
        if p[i-1] < p[i] && p[i] < p[i+1] || p[i-1] > p[i] && p[i] > p[i+1] {
            c = c + 1;
        }
    }

    println!("{}", c);
}
