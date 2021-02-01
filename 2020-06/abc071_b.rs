use whiteread::parse_line;

fn main() {
    let s: String = parse_line().unwrap();
    let ss: Vec<_> = s.chars().collect();
    let t: Vec<_> = "abcdefghijklmnopqrstuvwxyz".chars().collect();
    let mut b: bool = true;

    for e in t {
        if !ss.contains(&e) {
            println!("{}", e);
            b = false;
            break;
        }
    }
    if b {
        println!("None");
    }
}
