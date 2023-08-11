# GH-Toolkit

GH-Toolkit is a suite of tools to interact with the GitHub API, allowing for automated creation of issues, labels, and more. It offers an effortless approach to maintain repositories by automating routine tasks.

## Features

- Create GitHub issues programmatically.
- Manage and ensure GitHub labels exist.
- Load labels and issues configuration from JSON files.

## Installation

1. Clone the repository:

```
git clone https://github.com/chrismannina/gh-toolkit.git
```

2. Navigate to the project directory:

```
cd gh-toolkit
```

3. Install the required dependencies:

```
pip install requests python-dotenv
```

## Usage

1. **Setting Up Configuration**:

   Create a `data.json` in the root directory with the structure similar to the `example_data.json`. Modify the `repo_owner` and `repo_name` fields according to your repository.

2. **Labels**:

   All your label configurations should be stored in the `labels` folder in JSON format. The folder contains some predefined labels. Follow the same structure provided in those examples to create your own.

3. **Running the Script**:

   Simply execute the script:

```
python main.py [path_to_configuration_file]
```

If no configuration file path is provided, it defaults to `data.json` in the root directory.

## Example Configuration

The `example_data.json` file contains some sample issues to demonstrate the format.
