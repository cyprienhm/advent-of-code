use std::fs;

fn line_to_amount(line: &str) -> i32 {
    let dir = line.chars().next().unwrap();
    let amount = line[1..].parse::<i32>().unwrap();
    match dir {
        'L' => -amount,
        'R' => amount,
        _ => panic!(),
    }
}

fn part1(parsed: Vec<i32>) -> i32 {
    let mut position = 50;
    let mut count = 0;
    for amount in parsed.into_iter() {
        position += amount;
        position = position.rem_euclid(100);
        if position == 0 {
            count += 1;
        }
    }
    count
}

fn count_and_move((position, count): (i32, i32), amount: i32) -> (i32, i32) {
    let mut new_position = position;
    let mut new_count = count;
    for _ in 0..amount.abs() {
        new_position += amount.signum();
        new_position = new_position.rem_euclid(100);

        if new_position == 0 {
            new_count += 1;
        }
    }
    (new_position, new_count)
}
fn part2(parsed: Vec<i32>) -> i32 {
    let (_, answer) = parsed.into_iter().fold((50, 0), count_and_move);
    answer
}

fn main() {
    let contents = fs::read_to_string("./2025/day_01/input.txt").unwrap();

    let parsed: Vec<i32> = contents.lines().map(line_to_amount).collect();

    println!("{}", part1(parsed.clone()));
    println!("{}", part2(parsed));
}
