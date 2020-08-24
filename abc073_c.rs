use whiteread::parse_line;

fn main() {
    let n: usize = parse_line().unwrap();
    let mut i: usize = 0;
    let mut v: Vec<usize> = Vec::new();

    while i < n {
        let a: usize = parse_line().unwrap();
        v.push(a);
        i = i + 1;
    }

    v.sort();
    i = 0;
    let mut res: usize = 0;

    while i < n {
        let cc: usize = v[i];
        let mut f: usize = 0;
        while i < n && v[i] == cc {
            f = f + 1;
            i = i + 1;
        }
        res = res + f % 2;
    }

    println!("{}", res);
}
