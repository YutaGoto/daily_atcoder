use whiteread::parse_line;
use std::process;

fn main() {
    let (_n, _m, x, y): (i32, i32, i32, i32) = parse_line().unwrap();
    let vx: Vec<i32> = parse_line().unwrap();
    let vy: Vec<i32> = parse_line().unwrap();

    for z in (x+1)..=y {
        if vx.iter().all(|&x| x < z) && vy.iter().all(|&y| y >= z) {
            println!("No War");
            process::exit(0x0100);
        }
    }

    println!("War");
}
