# PassCraft

PassCraft is a lightweight Python CLI tool for generating secure passwords and evaluating their strength in real time. It helps you create stronger credentials for accounts, apps, and internal systems without any external dependencies.

## Why use PassCraft?

Strong passwords are essential for protecting sensitive information. PassCraft gives you a fast, terminal-based way to:

- generate custom passwords based on your preferred length and complexity
- include uppercase letters, numbers, and special characters
- review password strength instantly using a simple scoring system
- create multiple passwords in a single run

## Features

- configurable password length
- optional uppercase letters, numbers, and special characters
- instant strength scoring from Very Weak to Very Strong
- no third-party packages required
- simple cross-platform Python CLI usage

## Requirements

- Python 3.8 or newer
- a terminal or command prompt

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/areebahmed17082008-dot/passcraft.git
   cd passcraft
   ```

2. Create and activate a virtual environment (optional but recommended):

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. Run the application:

   ```bash
   python test.py
   ```

## Usage

When you launch the script, it will prompt for:

- how many passwords to generate
- the desired password length
- whether to include uppercase letters
- whether to include numbers
- whether to include special characters

After generation, each password is shown with a strength label and score.

### Example session

```bash
$ python test.py
How many passwords do you want to generate?: 3
Enter password length: 14
Include uppercase letters?  (y/n): y
Include numbers?   (y/n): y
Include special characters?   (y/n): y

Generated Passwords & Strength Analysis:
1. D7!xNq#pL9wA@t  | Strength: Very Strong (Score: 5/5)
2. q9!T@vL%z4R2kN  | Strength: Strong (Score: 4/5)
3. Mx7$gP!n9X2@fL  | Strength: Strong (Score: 4/5)
```

## Strength scoring

PassCraft evaluates each password using a simple 5-point scale:

- 5: Very Strong
- 4: Strong
- 3: Medium
- 2: Weak
- 1: Very Weak

The score increases when the password includes:

- a minimum length
- lowercase letters
- uppercase letters
- numbers
- special characters

## Security notes

Password generation is helpful for creating strong starting points, but best practices still matter:

- use a unique password for each account
- prefer longer passwords or passphrases when possible
- store credentials in a trusted password manager
- avoid reusing sensitive information like names, dates, or common phrases

## Project structure

```text
passcraft/
├── README.md
├── test.py
├── .gitignore
└── .venv/   # optional local virtual environment
```

## Contributing

Contributions are welcome. If you want to improve the tool, consider adding:

- stronger validation checks
- command-line flags for unattended usage
- password history or export options
- a more advanced scoring model

## License

This project is currently distributed without a formal license file. If you plan to share or publish it publicly, you may want to add an open-source license that matches your intended usage.
