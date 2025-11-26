use std::fs;

fn main() {
    part1();
    part2();
}

fn part1() {
    let contents = fs::read_to_string("./example.txt").unwrap();
    let mut lines_it = contents.lines();

    let first_line = lines_it.next().unwrap();
    let numbers: Vec<i32> = first_line.split(",").map(|s| s.parse().unwrap()).collect();

    let rest: Vec<&str> = lines_it.collect();
    let boards: Vec<Vec<Vec<i32>>> = rest
        .split(|s| s.is_empty()) // split on empty
        .map(|group| group.to_vec()) // &[&str] -> Vec<str>
        .filter(|group| !group.is_empty()) // filter out []
        .map(|group| {
            group
                .iter() // for each group, split on whitespace
                .map(|elt| {
                    elt.split_whitespace()
                        .map(|s| s.parse().unwrap())
                        .collect::<Vec<_>>()
                })
                .collect()
        })
        .collect();

    let mut marked = vec![];
    for board in &boards {
        let mut current = vec![];
        for row in board {
            current.push(vec![false; row.len()]);
        }
        marked.push(current);
    }
    // better would be
    // let marked: Vec<Vec<Vec<bool>>> = boards
    //     .iter()
    //     .map(|b| b.iter().map(|row| vec![false; row.len()]).collect())
    //     .collect();

    for n in &numbers {
        for (x, board) in boards.iter().enumerate() {
            for (i, row) in board.iter().enumerate() {
                for (j, elt) in row.iter().enumerate() {
                    if elt == n {
                        marked[x][i][j] = true;
                    }
                }
            }
            if has_won(&marked[x]) {
                println!("Board {x} has won");
                let remaining_score = board.iter().enumerate().fold(0, |acc, (i, row)| {
                    acc + {
                        row.iter().enumerate().fold(0, |acc_row, (j, elt)| {
                            if !marked[x][i][j] {
                                acc_row + elt
                            } else {
                                acc_row
                            }
                        })
                    }
                });
                let rem: i32 = board
                    .iter()
                    .enumerate()
                    .map(|(i, row)| {
                        row.iter()
                            .enumerate()
                            .filter(|&(j, _)| !marked[x][i][j])
                            .map(|(_, elt)| elt)
                            .sum::<i32>()
                    })
                    .sum();
                let score = rem * n;
                println!("{remaining_score}");
                println!("{rem}");
                println!("{n}");
                println!("{score}");
                return;
            }
        }
    }
}

fn has_won(marked_board: &Vec<Vec<bool>>) -> bool {
    for row in marked_board.iter() {
        let row_won = row.iter().fold(true, |acc, x| acc && *x);
        if row_won {
            return true;
        }
    }
    for j in 0..marked_board[0].len() {
        let mut col_has_won = true;
        for i in 0..marked_board.len() {
            col_has_won = col_has_won && marked_board[i][j];
        }
        if col_has_won {
            return true;
        };
    }

    return false;
}

fn part2() {
    let contents = fs::read_to_string("./input.txt").unwrap();
    let mut lines_it = contents.lines();

    let first_line = lines_it.next().unwrap();
    let numbers: Vec<i32> = first_line.split(",").map(|s| s.parse().unwrap()).collect();

    let rest: Vec<&str> = lines_it.collect();
    let boards: Vec<Vec<Vec<i32>>> = rest
        .split(|s| s.is_empty()) // split on empty
        .map(|group| group.to_vec()) // &[&str] -> Vec<str>
        .filter(|group| !group.is_empty()) // filter out []
        .map(|group| {
            group
                .iter() // for each group, split on whitespace
                .map(|elt| {
                    elt.split_whitespace()
                        .map(|s| s.parse().unwrap())
                        .collect::<Vec<_>>()
                })
                .collect()
        })
        .collect();

    let mut marked = vec![];
    for board in &boards {
        let mut current = vec![];
        for row in board {
            current.push(vec![false; row.len()]);
        }
        marked.push(current);
    }

    let mut already_won: Vec<bool> = vec![false; boards.len()];
    for n in &numbers {
        for (x, board) in boards.iter().enumerate() {
            if already_won[x] {
                continue;
            }
            for (i, row) in board.iter().enumerate() {
                for (j, elt) in row.iter().enumerate() {
                    if elt == n {
                        marked[x][i][j] = true;
                    }
                }
            }
            if has_won(&marked[x]) {
                already_won[x] = true;
                println!("Board {x} has won");
                let remaining_score = board.iter().enumerate().fold(0, |acc, (i, row)| {
                    acc + {
                        row.iter().enumerate().fold(0, |acc_row, (j, elt)| {
                            if !marked[x][i][j] {
                                acc_row + elt
                            } else {
                                acc_row
                            }
                        })
                    }
                });
                let score = remaining_score * n;
                println!("{remaining_score}");
                println!("{n}");
                println!("{score}");
            }
        }
    }
}
