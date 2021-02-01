use whiteread::parse_line;

fn main() {
    let (a, b): (i32, i32) = parse_line().unwrap();
    let mut i: i32 = 1;
    let mut same: bool = false;
    while i <= 1000 {
        let aa: i32 = ((i as f32) * 0.08) as i32;
        let bb: i32 = ((i as f32) * 0.1) as i32;

        if aa == a && bb == b {
            println!("{:?}", i);
            same = true;
            break;
        }

        if aa > a || bb > b{
            break;
        }

        i = i + 1;
    }

    if !same {
        println!("-1");
    }
}
