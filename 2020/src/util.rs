use std::fs;

pub enum FileType {
    Input,
    Test,
}

pub fn read_file(filename: String, filetype: FileType) -> String {
    let file_prefix = match filetype {
        FileType::Input => "input",
        FileType::Test => "test",
    };
    let file_path = format!("./src/{file_prefix}/{filename}.in");
    let file: String = fs::read_to_string(file_path).expect("Failed to read from file {filename}");
    let trimed_file = file.trim();
    return trimed_file.to_string();
}
