use whiteread::parse_line;

fn main() {
    let c: char = parse_line().unwrap();
    let vowels: Vec<char> = vec!['a', 'i', 'u', 'e', 'o'];

    if vowels.contains(&c) {
        println!("vowel");
    } else {
        println!("consonant");
    }
}
