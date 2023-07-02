use aoc2020::util::*;
use std::ops::RangeInclusive;

/*

1-3 a: abcde
1-3 b: cdefg
2-9 c: ccccccccc

*/

struct Password {
    range: RangeInclusive<i32>,
    key: char,
    value: String,
    positions: (i32, i32),
}

impl Password {
    fn parse_line(line: &str) -> Self {
        let parsed_line: Vec<&str> = line.split(" ").collect();

        // Range x-y
        let range: Vec<&str> = parsed_line[0].split("-").collect();
        let start = range[0].parse::<i32>().unwrap();
        let end = range[1].parse::<i32>().unwrap();
        let range = RangeInclusive::new(start, end);

        // Key x:
        let key: char = parsed_line[1].chars().nth(0).unwrap();

        // Value xxxxxx
        let value: String = parsed_line[2].to_string();

        Self {
            range,
            key,
            value,
            positions: (start, end),
        }
    }

    fn is_valid_part_1(&self) -> bool {
        let mut counter: i32 = 0;
        for c in self.value.chars() {
            if c == self.key {
                counter += 1;
            }
        }
        return self.range.contains(&counter);
    }

    fn is_valid_part_2(&self) -> bool {
        let mut counter: i32 = 0;

        let pos1: usize = self.positions.0 as usize - 1;
        let pos2: usize = self.positions.1 as usize - 1;
        let positions = vec![pos1, pos2];

        for pos in positions {
            if self.value.chars().nth(pos).unwrap() == self.key {
                counter += 1;
            }
        }

        return counter == 1;
    }
}

fn part1(filetype: FileType) -> i32 {
    let input: String = read_file(String::from("day2"), filetype);
    let split_string: Vec<&str> = input.split("\n").collect();

    let mut result = 0;
    for line in split_string {
        let pw = Password::parse_line(line);
        if pw.is_valid_part_1() {
            result += 1;
        }
    }

    return result;
}

fn part2(filetype: FileType) -> i32 {
    let input: String = read_file(String::from("day2"), filetype);
    let split_string: Vec<&str> = input.split("\n").collect();

    let mut result = 0;
    for line in split_string {
        let pw = Password::parse_line(line);
        if pw.is_valid_part_2() {
            result += 1;
        }
    }

    return result;
}

pub fn main() {
    println!("Solution to part1: {}", part1(FileType::Input));
    println!("Solution to part2: {}", part2(FileType::Input));
}

#[test]
fn test_part_1() {
    let result = part1(FileType::Test);
    assert_eq!(result, 2);
}

#[test]
fn test_part_2() {
    let result = part2(FileType::Test);
    assert_eq!(result, 1);
}
