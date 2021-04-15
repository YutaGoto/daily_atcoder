use whiteread::parse_line;

fn main() {
    let d: usize = parse_line().unwrap();
    match d {
        25 => println!("Christmas"),
        24 => println!("Christmas Eve"),
        23 => println!("Christmas Eve Eve"),
        22 => println!("Christmas Eve Eve Eve"),
        _ => println!("Eve"),
    }
}
