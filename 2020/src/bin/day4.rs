use aoc2020::util::*;
use std::collections::HashMap;

struct Passport {
    fields: HashMap<String, String>,
}

impl Passport {
    fn parse(string: &str) -> Self {
        let entries: Vec<&str> = string.split_whitespace().collect();

        let mut fields: HashMap<String, String> = HashMap::new();

        for entry in entries {
            let field_to_value: Vec<&str> = entry.split(':').collect();
            fields.insert(field_to_value[0].to_string(), field_to_value[1].to_string());
        }
        Self { fields }
    }

    fn is_valid(&self) -> bool {
        let keys: Vec<&String> = self.fields.keys().collect();

        if keys.len() == 8 {
            return true;
        }

        if keys.len() == 7 && !keys.contains(&&"cid".to_string()) {
            return true;
        }

        return false;
    }

    fn validate_byr(&self) -> bool {
        let byr = self
            .fields
            .get(&"byr".to_string())
            .unwrap()
            .parse::<usize>()
            .unwrap();
        if byr < 1920 || byr > 2002 {
            return false;
        }
        return true;
    }

    fn validate_iyr(&self) -> bool {
        let iyr = self
            .fields
            .get(&"iyr".to_string())
            .unwrap()
            .parse::<usize>()
            .unwrap();
        if iyr < 2010 || iyr > 2020 {
            return false;
        }
        return true;
    }

    fn validate_eyr(&self) -> bool {
        let eyr = self
            .fields
            .get(&"eyr".to_string())
            .unwrap()
            .parse::<usize>()
            .unwrap();
        if eyr < 2020 || eyr > 2030 {
            return false;
        }
        return true;
    }

    fn validate_hgt(&self) -> bool {
        let hgt: &String = self.fields.get(&"hgt".to_string()).unwrap();
        let suffix: &str = &hgt[&hgt.len() - 2..];

        if !(suffix == "in" || suffix == "cm") {
            return false;
        }
        let value: &usize = &hgt[..&hgt.len() - 2].parse::<usize>().unwrap();
        if suffix == "in" {
            if *value < 59 || *value > 76 {
                return false;
            }
        }
        if suffix == "cm" {
            if *value < 150 || *value > 193 {
                return false;
            }
        }
        return true;
    }

    fn validate_hcl(&self) -> bool {
        let hcl: &String = self.fields.get(&"hcl".to_string()).unwrap();
        let vec_char: Vec<char> = hcl.chars().collect();

        if vec_char.len() != 7 {
            return false;
        }

        let valid_chars = String::from("1234567890abcdef");
        let mut first = true;
        for c in vec_char {
            if first && c != '#' {
                return false;
            }
            if !first {
                if !valid_chars.contains(c) {
                    return false;
                }
            }
            first = false;
        }
        return true;
    }

    fn validate_ecl(&self) -> bool {
        let ecl: &String = self.fields.get(&"ecl".to_string()).unwrap();

        let options = vec!["amb", "blu", "brn", "gry", "grn", "hzl", "oth"];
        if !options.contains(&&ecl[..]) {
            return false;
        }
        return true;
    }

    fn validate_pid(&self) -> bool {
        let pid: &String = self.fields.get(&"pid".to_string()).unwrap();
        let vec_char: Vec<char> = pid.chars().collect();

        if vec_char.len() != 9 {
            return false;
        }

        let valid_chars = String::from("1234567890");
        for c in vec_char {
            if !valid_chars.contains(c) {
                return false;
            }
        }
        return true;
    }

    fn is_present(&self) -> bool {
        if !self.is_valid() {
            return false;
        }

        // Validate byr
        if !self.validate_byr() {
            return false;
        }

        // Validate iyr
        if !self.validate_iyr() {
            return false;
        }

        // Validate eyr
        if !self.validate_eyr() {
            return false;
        }

        // Validate hgt
        if !self.validate_hgt() {
            return false;
        }

        // Validate hcl
        if !self.validate_hcl() {
            return false;
        }

        // Validate ecl
        if !self.validate_ecl() {
            return false;
        }

        // Validate pid
        if !self.validate_pid() {
            return false;
        }

        return true;
    }
}

fn part1(filetype: FileType) -> usize {
    let input: String = read_file(String::from("day4"), filetype);
    let passports: Vec<&str> = input.split("\n\n").collect();

    let mut result: usize = 0;
    for passport in passports {
        let pw = Passport::parse(passport);
        if pw.is_valid() {
            result += 1;
        }
    }

    return result;
}

fn part2(filetype: FileType) -> usize {
    let input: String = read_file(String::from("day4"), filetype);
    let passports: Vec<&str> = input.split("\n\n").collect();

    let mut result: usize = 0;
    for passport in passports {
        let pw = Passport::parse(passport);
        if pw.is_present() {
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
    assert_eq!(result, 10);
}

// #[test]
// fn test_part_2() {
//     let result = part2(FileType::Test);
//     assert_eq!(result, 1);
// }

#[test]
fn byr_test_1() {
    let mut hash_map = HashMap::new();
    hash_map.insert(String::from("byr"), String::from("2002"));
    let passport = Passport { fields: hash_map };
    assert_eq!(passport.validate_byr(), true)
}
#[test]
fn byr_test_2() {
    let mut hash_map = HashMap::new();
    hash_map.insert(String::from("byr"), String::from("2003"));
    let passport = Passport { fields: hash_map };
    assert_eq!(passport.validate_byr(), false)
}
#[test]
fn iyr_test_1() {
    let mut hash_map = HashMap::new();
    hash_map.insert(String::from("iyr"), String::from("2010"));
    let passport = Passport { fields: hash_map };
    assert_eq!(passport.validate_iyr(), true)
}
#[test]
fn iyr_test_2() {
    let mut hash_map = HashMap::new();
    hash_map.insert(String::from("iyr"), String::from("2021"));
    let passport = Passport { fields: hash_map };
    assert_eq!(passport.validate_iyr(), false)
}

#[test]
fn hgt_test_1() {
    let mut hash_map = HashMap::new();
    hash_map.insert(String::from("hgt"), String::from("60in"));
    let passport = Passport { fields: hash_map };
    assert_eq!(passport.validate_hgt(), true)
}
#[test]
fn hgt_test_2() {
    let mut hash_map = HashMap::new();
    hash_map.insert(String::from("hgt"), String::from("190cm"));
    let passport = Passport { fields: hash_map };
    assert_eq!(passport.validate_hgt(), true)
}
#[test]
fn hgt_test_3() {
    let mut hash_map = HashMap::new();
    hash_map.insert(String::from("hgt"), String::from("190in"));
    let passport = Passport { fields: hash_map };
    assert_eq!(passport.validate_hgt(), false)
}
#[test]
fn hgt_test_4() {
    let mut hash_map = HashMap::new();
    hash_map.insert(String::from("hgt"), String::from("190"));
    let passport = Passport { fields: hash_map };
    assert_eq!(passport.validate_hgt(), false)
}

#[test]
fn hcl_test_1() {
    let mut hash_map = HashMap::new();
    hash_map.insert(String::from("hcl"), String::from("#123abc"));
    let passport = Passport { fields: hash_map };
    assert_eq!(passport.validate_hcl(), true)
}
#[test]
fn hcl_test_2() {
    let mut hash_map = HashMap::new();
    hash_map.insert(String::from("hcl"), String::from("#123abz"));
    let passport = Passport { fields: hash_map };
    assert_eq!(passport.validate_hcl(), false)
}
#[test]
fn hcl_test_3() {
    let mut hash_map = HashMap::new();
    hash_map.insert(String::from("hcl"), String::from("123abc"));
    let passport = Passport { fields: hash_map };
    assert_eq!(passport.validate_hcl(), false)
}

#[test]
fn ecl_test_1() {
    let mut hash_map = HashMap::new();
    hash_map.insert(String::from("ecl"), String::from("brn"));
    let passport = Passport { fields: hash_map };
    assert_eq!(passport.validate_ecl(), true)
}
#[test]
fn ecl_test_2() {
    let mut hash_map = HashMap::new();
    hash_map.insert(String::from("ecl"), String::from("wat"));
    let passport = Passport { fields: hash_map };
    assert_eq!(passport.validate_ecl(), false)
}

#[test]
fn pid_test_1() {
    let mut hash_map = HashMap::new();
    hash_map.insert(String::from("pid"), String::from("000000001"));
    let passport = Passport { fields: hash_map };
    assert_eq!(passport.validate_pid(), true)
}
#[test]
fn pid_test_2() {
    let mut hash_map = HashMap::new();
    hash_map.insert(String::from("pid"), String::from("0123456789"));
    let passport = Passport { fields: hash_map };
    assert_eq!(passport.validate_pid(), false)
}
