use whiteread::parse_line;

fn main() {
    let (_n, k): (i32, i32) = parse_line().unwrap();
    let v: Vec<i32> = parse_line().unwrap();
    let mut c: i32 = 0;
    
    for i in v {
        if i >= k {
            c = c + 1;
        }
    }

    println!("{:?}", c);
}
