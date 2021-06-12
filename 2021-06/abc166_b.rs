use whiteread::parse_line;

fn main() {
    let (n, k): (usize, usize) = parse_line().unwrap();
    let mut sunuke: Vec<usize> = vec![0; n];

    for i in 0..k {
        let _d: usize = parse_line().unwrap();
        let a: Vec<usize> = parse_line().unwrap();

        for e in a.iter() {
            sunuke[e-1] = sunuke[e-1] + 1;
        }
    }

    let ans: usize = sunuke.iter().filter(|&snk| *snk == 0).count();
    println!("{}", ans);
}
