use aoc2020::util::*;
use std::collections::HashSet;

fn part1(filetype: FileType) -> usize {
    let input: String = read_file(String::from("day06"), filetype);

    let groups = input.split("\n\n");

    let mut result = 0;
    for people in groups {
        let set_of_answers = people
            .chars()
            .filter(|c| c.is_ascii_alphabetic())
            .collect::<Vec<char>>();
        let count: HashSet<char> = HashSet::<char>::from_iter(set_of_answers);
        result += count.len()
    }

    result
}

fn part2(filetype: FileType) -> usize {
    let input: String = read_file(String::from("day06"), filetype);

    let groups = input.split("\n\n").collect::<Vec<&str>>();

    let mut result = 0;
    for group in groups {
        let mut hashset: HashSet<char> = (b'a'..b'{').map(|c| c as char).collect();
        for people in group.split("\n") {
            let inner_hashset: HashSet<char> = HashSet::<char>::from_iter(people.chars());
            hashset = hashset.intersection(&inner_hashset).cloned().collect();
        }
        result += hashset.len();
    }
    result
}

pub fn main() {
    println!("Solution to part1: {}", part1(FileType::Input));
    println!("Solution to part2: {}", part2(FileType::Input));
}

#[test]
fn test_part1() {
    let result = part1(FileType::Test);
    assert_eq!(result, 11)
}

#[test]
fn test_part2() {
    let result = part2(FileType::Test);
    assert_eq!(result, 6)
}
