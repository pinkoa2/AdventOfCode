use aoc2020::util::*;
use std::cmp;

fn solve_sequence(s: &str) -> usize {
    let chars: Vec<char> = s.chars().collect();
    let mut start = 0;
    let mut end = 127;
    for i in 0..7 {
        let middle = start + (end - start) / 2;

        if chars[i] == 'F' {
            end = middle;
        } else if chars[i] == 'B' {
            start = middle + 1;
        }
    }
    let row = start;

    start = 0;
    end = 7;
    for i in 0..3 {
        let middle = start + (end - start) / 2;

        if chars[i + 7] == 'L' {
            end = middle;
        } else if chars[i + 7] == 'R' {
            start = middle + 1;
        }
    }
    let col = start;

    return row * 8 + col;
}

fn part1(filetype: FileType) -> usize {
    let input: String = read_file(String::from("day5"), filetype);
    let lines: Vec<&str> = input.split('\n').collect();

    let mut result = 0;
    for line in &lines {
        result = cmp::max(result, solve_sequence(line))
    }
    result
}

fn part2(filetype: FileType) -> usize {
    let input: String = read_file(String::from("day5"), filetype);
    let lines: Vec<&str> = input.split('\n').collect();

    let mut result = 0;
    let mut min = lines.len();
    let mut max = 0;
    for line in &lines {
        let id = solve_sequence(line);
        min = cmp::min(min, id);
        max = cmp::max(max, id);
        result += id;
    }

    let n: f32 = (max - min + 1) as f32;
    ((n / 2.0) * (2.0 * min as f32 + (n - 1.0)) - result as f32) as usize
}

pub fn main() {
    println!("Solution to part1: {}", part1(FileType::Input));
    println!("Solution to part1: {}", part2(FileType::Input));
}

#[test]
fn test_part1() {
    let result = part1(FileType::Test);
    assert_eq!(result, 820);
}
