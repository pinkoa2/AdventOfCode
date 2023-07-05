use aoc2020::util::*;
use std::cell::RefCell;
use std::collections::HashMap;
use std::collections::HashSet;
use std::rc::Rc;

#[derive(Debug)]
struct Node {
    name: String,
    parent: Vec<Rc<RefCell<Node>>>,
    children: Vec<Rc<RefCell<Node>>>,
}

impl Node {
    fn new(name: String) -> Rc<RefCell<Self>> {
        Rc::new(RefCell::new(Self {
            name,
            parent: vec![],
            children: vec![],
        }))
    }

    fn attach_parent(&mut self, parent: Rc<RefCell<Node>>) {
        self.parent.push(parent);
    }

    fn attach_child(&mut self, child: Rc<RefCell<Node>>) {
        self.children.push(child)
    }
}

#[derive(Debug)]
struct Bag {
    parent: String,
    children: Vec<(usize, String)>,
}

fn parse_line(line: &str) -> Bag {
    let get_parent: Vec<&str> = line.split("contain").collect();
    let parent: &str = &get_parent[0][..&get_parent[0].len() - 5];
    let remainder: &str = &get_parent[1].trim();
    let names: Vec<&str> = remainder.split(" ").collect();
    let mut children: Vec<(usize, String)> = Vec::new();

    if !(names[0] == "no") {
        for i in (0..names.len()).step_by(4) {
            let num = names[i + 0].parse::<usize>().unwrap();
            let name = format!("{} {}", names[i + 1], names[i + 2]);
            children.push((num, name.trim().to_string()));
        }
    }
    Bag {
        parent: parent.trim().to_string(),
        children,
    }
}

fn part1(filetype: FileType) -> i32 {
    let input: String = read_file(String::from("day7"), filetype);
    let all_lines: Vec<&str> = input.split("\n").collect();

    // Create the nodes. Use the parents names for now
    let mut name_to_node: HashMap<String, Rc<RefCell<Node>>> = HashMap::new();

    for line in &all_lines {
        let bag = parse_line(line);
        let parent = bag.parent;
        let node = Node::new(parent.clone());
        name_to_node.insert(parent.clone(), node);
    }

    for line in &all_lines {
        let bag = parse_line(line);
        let parent_name = bag.parent;
        // println!("{parent_name}");
        let parent = name_to_node.get(&parent_name).unwrap().clone();
        for child_bag in bag.children {
            let child_name = child_bag.1;
            // println!("{child_name}");
            let child = name_to_node.get(&child_name).unwrap().clone();
            child.borrow_mut().attach_parent(Rc::clone(&parent));
            parent.borrow_mut().attach_child(child);
        }
    }

    let mut result: HashSet<String> = HashSet::new();

    let mut current_nodes: Vec<Rc<RefCell<Node>>> =
        vec![name_to_node.get("shiny gold").unwrap().clone()];
    let mut next_nodes: Vec<Rc<RefCell<Node>>> = Vec::new();

    loop {
        for node in current_nodes {
            let parents: Vec<Rc<RefCell<Node>>> = node.borrow_mut().parent.clone();
            for p in parents {
                let r: &String = &p.borrow_mut().name.clone();
                result.insert(r.clone());
                next_nodes.push(p);
            }
        }
        current_nodes = next_nodes.clone();
        next_nodes.clear();
        if current_nodes.len() == 0 {
            break;
        }
    }
    result.len() as i32
}

fn main() {
    println!("Solution to part1: {}", part1(FileType::Input));
}

#[test]
fn test_part_1() {
    let result = part1(FileType::Test);
    assert_eq!(result, 4);
}
