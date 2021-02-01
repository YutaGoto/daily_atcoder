use whiteread::parse_line;

fn divisor(n: usize) -> Vec<usize> {
    let mut lower_divisors = Vec::new();
    let mut upper_divisors = Vec::new();
    let mut i: usize = 1;

    while i * i <= n {
        if n % i == 0 {
            lower_divisors.push(i);
            if i != n / i {
                upper_divisors.push(n / i);
            }
        }
        i = i + 1;
    }

    upper_divisors.reverse();
    lower_divisors.extend(upper_divisors);
    return lower_divisors;
}

fn main() {
    let n: usize = parse_line().unwrap();
    let v = divisor(n);

    for e in v.iter() {
        println!("{}", e);
    }
}
