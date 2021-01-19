use whiteread::parse_line;

fn main() {
    let n: usize = parse_line().unwrap();
    let mut v: Vec<usize> = parse_line().unwrap();

    v.sort();
    v.reverse();

    let mut a: usize = 0;
    let mut b: usize = 0;

    for i in 0..n {
        if i % 2 == 0 {
            a = a + v[i];
        } else {
            b = b + v[i];
        }
    }

    println!("{}", a - b);
}
