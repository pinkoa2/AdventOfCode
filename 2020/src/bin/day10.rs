use aoc2020::util::{read_file, FileType};
use std::collections::HashMap;

fn part1(filetype: FileType) -> usize {
    let input = read_file(String::from("day10"), filetype);

    let mut sequence: Vec<usize> = input
        .split('\n')
        .map(|num| num.parse::<usize>().unwrap())
        .collect();
    sequence.push(0);
    sequence.sort();

    let mut hashmap: HashMap<usize, usize> = HashMap::new();

    for i in 0..sequence.len() - 1 {
        let num1 = sequence[i];
        let num2 = sequence[i + 1];
        let difference = num2 - num1;

        hashmap
            .entry(difference)
            .and_modify(|counter| *counter += 1)
            .or_insert(1);
    }
    return hashmap.get(&1).unwrap() * (hashmap.get(&3).unwrap() + 1);
}

fn part2(filetype: FileType) -> usize {
    let input = read_file(String::from("day10"), filetype);

    let mut sequence: Vec<usize> = input
        .split('\n')
        .map(|num| num.parse::<usize>().unwrap())
        .collect();
    sequence.push(0);
    sequence.sort();
    sequence.push(sequence[sequence.len() - 1] + 3);

    let mut counter: HashMap<isize, usize> = HashMap::new();
    counter.insert(0, 1);

    for i in 1..sequence.len() {
        let value = sequence[i] as isize;

        let num1 = counter.get(&(value - 1)).unwrap_or(&0);
        let num2 = counter.get(&(value - 2)).unwrap_or(&0);
        let num3 = counter.get(&(value - 3)).unwrap_or(&0);

        counter.insert(value, num1 + num2 + num3);
    }

    return counter
        .get(&(sequence[sequence.len() - 1] as isize))
        .unwrap()
        .clone();
}

fn main() {
    println!("Solution to part1: {}", part1(FileType::Input));
    println!("Solution to part2: {}", part2(FileType::Input));
}

#[test]
fn test_part_1() {
    let test = part1(FileType::Test);
    assert_eq!(test, 22 * 10);
    let input = part1(FileType::Input);
    assert_eq!(input, 2470);
}
#[test]
fn test_part_2() {
    let test = part2(FileType::Test);
    assert_eq!(test, 19208);
    let input = part2(FileType::Input);
    assert_eq!(input, 1973822685184);
}
