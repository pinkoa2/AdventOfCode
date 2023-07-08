use aoc2020::util::*;
use std::fmt;

#[derive(Debug)]
struct Grid {
    grid: Vec<Vec<char>>,
}

impl fmt::Display for Grid {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        let mut string: String = String::new();
        for line in &self.grid {
            for char in line {
                string.push(*char);
            }
            string.push('\n');
        }
        write!(f, "{}", string)
    }
}

impl Grid {
    fn parse(string: String) -> Self {
        let lines: Vec<&str> = string.split("\n").collect();

        let mut grid: Vec<Vec<char>> = Vec::new();
        for line in lines {
            let char_vector: Vec<char> = line.chars().collect();
            grid.push(char_vector);
        }
        Self { grid }
    }

    fn get_value(&self, x: usize, y: usize) -> char {
        self.grid[y][x % self.grid[0].len()]
    }

    fn traverse(&self, right: usize, down: usize) -> i32 {
        let mut result: i32 = 0;

        let mut pos = (0, 0);

        while pos.1 < self.grid.len() {
            let x = pos.0;
            let y = pos.1;
            let char_at_pos: char = self.get_value(x, y);

            if char_at_pos == '#' {
                result += 1;
            }

            pos = (x + right, y + down)
        }

        return result;
    }
}

fn part1(filetype: FileType) -> i32 {
    let input: String = read_file(String::from("day03"), filetype);
    let grid = Grid::parse(input);
    return grid.traverse(3, 1);
}

fn part2(filetype: FileType) -> usize {
    let input: String = read_file(String::from("day03"), filetype);
    let grid = Grid::parse(input);

    let positions = vec![(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)];

    let mut result: usize = 1;
    for pos in positions {
        result *= grid.traverse(pos.0, pos.1) as usize;
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
    assert_eq!(result, 7);
}

#[test]
fn test_part_2() {
    let result = part2(FileType::Test);
    assert_eq!(result, 336);
}
