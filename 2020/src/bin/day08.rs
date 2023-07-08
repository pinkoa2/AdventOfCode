use aoc2020::util::{read_file, FileType};
use std::collections::HashSet;

#[derive(Debug)]
enum Op {
    NOP,
    ACC,
    JMP,
}

fn parse_line_to_instruction(line: &str) -> Instruction {
    let splitted: Vec<&str> = line.split(" ").collect();
    let first = splitted[0].trim();
    let second = splitted[1].trim();
    let operation: Op = match first {
        "nop" => Op::NOP,
        "acc" => Op::ACC,
        "jmp" => Op::JMP,
        _ => panic!("Unsupported type"),
    };
    let value = second.parse::<isize>().unwrap();
    Instruction { operation, value }
}

fn change_instruction(instruction: &Instruction) -> Instruction {
    let operation = match instruction.operation {
        Op::NOP => Op::JMP,
        Op::JMP => Op::NOP,
        Op::ACC => Op::ACC,
    };
    Instruction {
        operation,
        value: instruction.value,
    }
}

#[derive(Debug)]
struct Instruction {
    operation: Op,
    value: isize,
}

struct Machine<'a> {
    index: usize,
    instructions: Vec<&'a Instruction>,
    value: isize,
    visited: HashSet<usize>,
}

impl<'a> Machine<'a> {
    fn new() -> Self {
        Self {
            index: 0,
            instructions: Vec::new(),
            value: 0,
            visited: HashSet::new(),
        }
    }

    fn add_instruction(&mut self, instruction: &'a Instruction) {
        self.instructions.push(instruction);
    }

    #[allow(unused_assignments)]
    fn solve(&mut self) -> (isize, bool) {
        let mut exitted_early: bool = false;
        loop {
            if self.index >= self.instructions.len() {
                break;
            }
            let instruction = &self.instructions[self.index];
            self.visited.insert(self.index);
            let op = &instruction.operation;
            let value = &instruction.value;
            match op {
                Op::NOP => self.index += 1,
                Op::ACC => {
                    let new_index = self.index + 1;
                    if self.visited.contains(&new_index) {
                        exitted_early = true;
                        break;
                    }
                    self.value += value;
                    self.index = new_index;
                }
                Op::JMP => {
                    let new_index: isize = self.index as isize + value;
                    if self.visited.contains(&(new_index as usize)) {
                        exitted_early = true;
                        break;
                    }
                    self.index = new_index as usize;
                }
            }
        }
        (self.value, exitted_early)
    }
}

fn part1(filetype: FileType) -> isize {
    let input: String = read_file(String::from("day08"), filetype);
    let lines: Vec<&str> = input.split("\n").collect();

    let instructions: Vec<Instruction> = lines
        .iter()
        .map(|line| parse_line_to_instruction(line))
        .collect();
    let mut machine = Machine::new();

    for instruction in &instructions {
        machine.add_instruction(instruction);
    }
    let (result, _) = machine.solve();
    result
}

fn part2(filetype: FileType) -> isize {
    let input: String = read_file(String::from("day08"), filetype);
    let lines: Vec<&str> = input.split("\n").collect();

    let mut instructions: Vec<Instruction> = lines
        .iter()
        .map(|line| parse_line_to_instruction(line))
        .collect();

    let size = instructions.len();
    for index in 0..size {
        let mut machine = Machine::new();
        let original_instruction = instructions.remove(index);
        let new_instruction = change_instruction(&original_instruction);
        instructions.insert(index, new_instruction);

        instructions
            .iter()
            .for_each(|instruction| machine.add_instruction(instruction));

        let (result, exitted_early) = machine.solve();
        if !exitted_early {
            return result;
        }
        instructions.remove(index);
        instructions.insert(index, original_instruction);
    }
    panic!("Should never reach here");

}

fn main() {
    println!("Solution to part1: {}", part1(FileType::Input));
    println!("Solution to part2: {}", part2(FileType::Input));
}

#[test]
fn test_part_1() {
    let test = part1(FileType::Test);
    assert_eq!(test, 5);
    let real = part1(FileType::Input);
    assert_eq!(real, 1814);
}
#[test]
fn test_part_2() {
    let test = part2(FileType::Test);
    assert_eq!(test, 8);
    let real = part2(FileType::Input);
    assert_eq!(real, 1056);
}
