use whiteread::parse_line;

fn main() {
    let s: String = parse_line().unwrap();
    let sv: Vec<&str> = s.split("").collect();
    if sv[2] == sv[3] {
        if sv[1] == sv[2] || sv[3] == sv[4] {
            println!("Yes");
        } else {
            println!("No");
        }
    } else {
        println!("No");
    }
}
