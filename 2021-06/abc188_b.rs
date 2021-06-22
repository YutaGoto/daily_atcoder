use whiteread::parse_line;

fn main() {
    let n: usize = parse_line().unwrap();
    let a: Vec<isize> = parse_line().unwrap();
    let b: Vec<isize> = parse_line().unwrap();
    let mut ans: isize = 0;

    for i in 0..n {
        ans = ans + a[i] * b[i];
    }

    if ans == 0 {
        println!("Yes");
    } else {
        println!("No");
    }
}
