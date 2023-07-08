use aoc2020::util::{read_file, FileType};
use std::collections::HashSet;

fn part1(filetype: FileType, preamble: usize) -> u128 {
    let input = read_file(String::from("day09"), filetype);
    let splitted: Vec<&str> = input.split("\n").collect();

    let sequence: Vec<u128> = splitted
        .iter()
        .map(|num| num.parse::<u128>().unwrap())
        .collect();

    for i in preamble..sequence.len() {
        let current = sequence[i];
        let spliced = &sequence[(i - preamble)..i];
        let hashset: HashSet<&u128> = spliced.iter().collect();

        let mut found_partner = false;
        for num in spliced {
            let lookup = match current.checked_sub(num.clone()) {
                Some(val) => val,
                None => 0,
            };
            if hashset.contains(&lookup) {
                found_partner = true;
            }
        }
        if !found_partner {
            return current;
        }
    }
    panic!("Should not reach here");
}

fn part2(filetype: FileType, preamble: usize) -> u128 {
    let copy = match filetype {
        FileType::Test => FileType::Test,
        FileType::Input => FileType::Input,
    };

    let value = part1(copy, preamble);
    let input = read_file(String::from("day09"), filetype);

    let splitted: Vec<&str> = input.split("\n").collect();
    let sequence: Vec<u128> = splitted
        .iter()
        .map(|num| num.parse::<u128>().unwrap())
        .collect();

    let mut starting = 0;
    let mut ending: usize;
    loop {
        ending = starting + 1;
        'inner: loop {
            let sum_over_range: u128 = sequence[starting..=ending].iter().sum();

            if sum_over_range == value {
                let minimum = sequence[starting..=ending].iter().min().unwrap();
                let maxiimum = sequence[starting..=ending].iter().max().unwrap();
                return minimum + maxiimum;
            }

            if sum_over_range > value {
                break 'inner;
            }
            ending += 1;
        }
        starting += 1;
    }
}

fn main() {
    println!("Solution to part1 is {}", part1(FileType::Input, 25));
    println!("Solution to part2 is {}", part2(FileType::Input, 25));
}

#[test]
fn test_part_1() {
    let test = part1(FileType::Test, 5);
    assert_eq!(test, 127);
    let input = part1(FileType::Input, 25);
    assert_eq!(input, 393911906);
}
#[test]
fn test_part_2() {
    let test = part2(FileType::Test, 5);
    assert_eq!(test, 62);
    let input = part2(FileType::Input, 25);
    assert_eq!(input, 59341885);
}
