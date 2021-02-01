use whiteread::parse_line;

fn main() {
  let (mut a, mut b, mut k): (usize, usize, usize) = parse_line().unwrap();
  if k > 0 {
    if a > 0 {
      if a > k {
        a = a - k;
        k = 0;
      } else {
        k = k - a;
        a = 0;
      }
    }
  }

  if k > 0 {
    if b > 0 {
      if b > k {
        b = b - k;
        k = 0;
      } else {
        k = k - b;
        b = 0;
      }
    }
  }

  println!("{} {}", a, b);
}
