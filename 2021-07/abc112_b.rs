use whiteread::parse_line;

fn main() {
    let (n, mt): (usize, usize) = parse_line().unwrap();
    let mut cc: Vec<usize> = vec![];

    for _i in 0..n {
        let (c, t): (usize, usize) = parse_line().unwrap();
        if t <= mt {
            cc.push(c);
        }
    }

    if cc.len() == 0 {
        println!("TLE");
    } else {
        println!("{:?}", cc.iter().min().unwrap());
    }
}
