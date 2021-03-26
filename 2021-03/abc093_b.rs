use whiteread::parse_line;

fn main() {
    let (a, b, k): (isize, isize, isize) = parse_line().unwrap();

    if a == b {
        println!("{}", a);
    } else if b-k < a+k {
        for i in a..=b {
            println!("{}", i);
        }
    } else {
        for i in a..(a+k) {
            println!("{}", i);
        }

        for i in (b-k+1)..=b {
            println!("{}", i);
        }
    }
}
