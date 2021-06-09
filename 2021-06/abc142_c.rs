extern crate itertools;

use whiteread::parse_line;
use itertools::Itertools;

fn main() {
    let n: usize = parse_line().unwrap();
    let a: Vec<usize> = parse_line().unwrap();
    let mut ans: Vec<usize> = vec![0; n];

    for i in 0..n {
        ans[a[a[i]-1]-1] = a[i];
    }

    let ans_string: String = ans.iter().join(" ");

    println!("{}", ans_string);
}
