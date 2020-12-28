use whiteread::parse_line;

fn main() {
    let n: u64 = parse_line().unwrap();

    for h in 1..7001 {
        for m in 1..7001 {
            if (4.0/n as f64 - 1.0/h as f64 - 1.0/m as f64) != 0.0 {
                let w: f64 = (1.0 / (4.0/n as f64 - 1.0/h as f64 - 1.0/m as f64));
                if w > 0.0 && w < 10000.0 && w.fract() == 0.0 {
                    println!("{} {} {}", h, m, w);
                    std::process::exit(0);
                }
            }
        }
    }
}
