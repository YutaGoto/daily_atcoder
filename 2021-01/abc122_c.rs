use whiteread::parse_line;

fn main() {
    let (n, q): (usize, usize) = parse_line().unwrap();
    let s: String = parse_line().unwrap();

    let mut v: Vec<usize> = vec![0; n];

    for i in 0..(n-1) {
        let mut m: usize = 0;
        if &s[i..(i+2)] == "AC" {
            m = 1;
        }
        v[i+1] = v[i] + m;
    }

    for _i in 0..q {
        let (l, r): (usize, usize) = parse_line().unwrap();
        println!("{}", v[(r-1)] - v[(l-1)]);
    }
}
