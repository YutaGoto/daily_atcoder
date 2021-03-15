use whiteread::parse_line;

fn main() {
    // AT GC
    let s: String = parse_line().unwrap();
    if s == "A" {
        println!("T");
    } else if s == "T" {
        println!("A");
    } else if s == "G" {
        println!("C");
    } else if s == "C" {
        println!("G");
    }
}
