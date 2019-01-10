//0.04s user 0.00s system 96% cpu 0.041 total
fn main() {
    let n:i32 = 1000000;

    let mut a = [true; 1000000];

    for x in 2..((n as f32).sqrt() as i32 + 1) {
        for y in 2..(n/x+1 as i32) {
            if x*y-1 <= n {
                a[(x*y-1) as usize] = false;
            }
        }
    }

    let mut last = 2;
    for (key, value) in a.iter().enumerate() {
        if *value {
            last = key+1;
        }
    }
    println!("{}", last);
}
