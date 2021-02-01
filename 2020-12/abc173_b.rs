use whiteread::parse_line;

fn main() {
    let n: usize = parse_line().unwrap();

    let mut ac: usize = 0;
    let mut wa: usize = 0;
    let mut tle: usize = 0;
    let mut re: usize = 0;

    for _i in 0..n {
        let s: String = parse_line().unwrap();
        if s == "AC" {
            ac = ac+1;
        } else if s == "WA" {
            wa = wa+1;
        } else if s == "TLE" {
            tle = tle+1;
        } else if s == "RE" {
            re = re+1;
        }
    }

    println!("AC x {}", ac);
    println!("WA x {}", wa);
    println!("TLE x {}", tle);
    println!("RE x {}", re);
}
