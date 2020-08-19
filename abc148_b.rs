use whiteread::parse_line;

fn main() {
    let n: usize = parse_line().unwrap();
    let (s, t): (String, String) = parse_line().unwrap();

    let mut u: String = "".to_string();
    let mut i: usize = 0;

    while i < n {
        u = u + &s[i..i+1] + &t[i..i+1];
        i = i + 1;
    }

    println!("{}", u);
}
