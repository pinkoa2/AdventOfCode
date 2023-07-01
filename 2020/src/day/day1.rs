use crate::util;

fn part1(filetype: util::FileType) -> i32 {
    let input: String = util::read_file(String::from("day1"), filetype);
    let split_string: Vec<&str> = input.split("\n").collect();

    for value in &split_string {
        let partner = 2020 - value.parse::<i32>().unwrap();
        if split_string.contains(&(&partner.to_string()[..])) {
            return partner * value.parse::<i32>().unwrap();
        }
    }
    return 0;
}

fn part2(filetype: util::FileType) -> i32 {
    let input: String = util::read_file(String::from("day1"), filetype);
    let split_string: Vec<&str> = input.split("\n").collect();
    for value1 in &split_string {
        for value2 in &split_string {
            for value3 in &split_string {
                let v1 = value1.parse::<i32>().unwrap();
                let v2 = value2.parse::<i32>().unwrap();
                let v3 = value3.parse::<i32>().unwrap();
                if v1 + v2 + v3 == 2020 {
                    return v1 * v2 * v3;
                }
            }
        }
    }
    return 1;
}

pub fn run() {
    println!("Solution part1: {}", part1(util::FileType::Input));
    println!("Solution part2: {}", part2(util::FileType::Input));
}

#[test]
fn test_part_1() {
    let result = part1(util::FileType::Test);
    assert_eq!(result, 514579);
}
#[test]
fn test_part_2() {
    let result = part2(util::FileType::Test);
    assert_eq!(result, 241861950)
}
