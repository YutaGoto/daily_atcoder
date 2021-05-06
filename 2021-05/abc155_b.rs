use whiteread::parse_line;

fn main() {
    let n: usize = parse_line().unwrap();
    let v: Vec<usize> = parse_line().unwrap();

    let mut ans: String = "APPROVED".to_string();

    for num in v.iter() {
        if num % 2 == 0 {
            if num % 3 != 0 && num % 5 != 0 {
                ans = "DENIED".to_string();
            }
        }
    }

    println!("{}", ans);
}
