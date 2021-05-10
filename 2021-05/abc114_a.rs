use whiteread::parse_line;

fn main() {
    let x: usize = parse_line().unwrap();
    if x == 3 || x == 5 || x == 7 {
        println!("YES");
    } else {
        println!("NO");
    }
}
