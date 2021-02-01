use whiteread::parse_line;

fn main() {
    let (x, y): (i32, i32) = parse_line().unwrap();
    let v1: Vec<i32> = vec![4,6,9,11];
    let v2: Vec<i32> = vec![1,3,5,7,8,10,12];
    if x == 2 || y == 2 {
        println!("No");
    } else if v1.contains(&x) && v1.contains(&y) {
        println!("Yes");
    } else if v2.contains(&x) && v2.contains(&y) {
        println!("Yes");
    } else {
        println!("No");
    }
}
