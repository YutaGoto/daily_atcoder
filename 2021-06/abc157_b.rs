use whiteread::parse_line;

fn main() {
    let (a11, a12, a13): (usize, usize, usize) = parse_line().unwrap();
    let (a21, a22, a23): (usize, usize, usize) = parse_line().unwrap();
    let (a31, a32, a33): (usize, usize, usize) = parse_line().unwrap();
    let n: usize = parse_line().unwrap();
    let mut bingo: Vec<Vec<usize>> = vec![
        vec![0,0,0],
        vec![0,0,0],
        vec![0,0,0],
    ];

    for _i in 0..n {
        let b: usize = parse_line().unwrap();
        if a11 == b {
            bingo[0][0] = 1;
        }
        if a12 == b {
            bingo[0][1] = 1;
        }
        if a13 == b {
            bingo[0][2] = 1;
        }
        if a21 == b {
            bingo[1][0] = 1;
        }
        if a22 == b {
            bingo[1][1] = 1;
        }
        if a23 == b {
            bingo[1][2] = 1;
        }
        if a31 == b {
            bingo[2][0] = 1;
        }
        if a32 == b {
            bingo[2][1] = 1;
        }
        if a33 == b {
            bingo[2][2] = 1;
        }
    }

    let sum0: usize = bingo[0].iter().sum();
    let sum1: usize = bingo[1].iter().sum();
    let sum2: usize = bingo[2].iter().sum();

    if sum0 == 3 || sum1 == 3 || sum2 == 3 {
        println!("Yes");
    } else if bingo[0][0] == bingo[1][0] && bingo[1][0] == bingo[2][0] && bingo[2][0] == 1 {
        println!("Yes");
    } else if bingo[0][1] == bingo[1][1] && bingo[1][1] == bingo[2][1] && bingo[2][1] == 1 {
        println!("Yes");
    } else if bingo[0][2] == bingo[1][2] && bingo[1][2] == bingo[2][2] && bingo[2][2] == 1 {
        println!("Yes");
    } else if bingo[0][0] == bingo[1][1] && bingo[1][1] == bingo[2][2] && bingo[2][2] == 1 {
        println!("Yes");
    } else if bingo[0][2] == bingo[1][1] && bingo[1][1] == bingo[2][0] && bingo[2][0] == 1 {
        println!("Yes");
    } else {
        println!("No");
    }
}
