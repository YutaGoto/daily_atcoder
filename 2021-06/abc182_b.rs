use whiteread::parse_line;

fn main() {
    let n: usize = parse_line().unwrap();
    let a: Vec<usize> = parse_line().unwrap();
    let mut p: Vec<usize> = vec![0; 1001];

    for i in 2..=1000 {
        for e in a.iter() {
            if e % i == 0 {
                p[i] = p[i] + 1;
            }
        }
    }

    let maxValue: &usize = p.iter().max().unwrap();
    let innum = p.iter().position(|&r| r == *maxValue).unwrap();
    println!("{}", innum);
}
