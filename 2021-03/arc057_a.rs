use whiteread::parse_line;

fn main() {
    let (mut a, k): (usize, usize) = parse_line().unwrap();
    let nicho: usize = 2 * 10usize.pow(12) as usize;
    let mut i: usize = 0;

    if k == 0 {
        println!("{}", nicho - a)
    } else {
        loop {
            i = i + 1;
            a = a + a*k + 1;

            if a >= nicho {
                println!("{}", i);
                break;
            }
        }
    }
}
