
# cis6930fa24 -- Assignment0

## Author

**Name**: Balasai Srikanth Ganti

**UFID** : 5251-6075

## Assignment Description 
This project fetches and processes data from the FBI Wanted API or from a local JSON file, extracts specific fields (title, subjects, and field offices), and formats the data in a thorn-separated format.


## How to install

To set up the environment, use pipenv to install the dependencies.

```bash
pipenv install .
```

## How to run
Run the program using the following commands:

### Option 1: Fetch data from FBI API:
```bash
pipenv run python main.py --page <page-number>
```

### Option 2: Load data from a local JSON file:
```bash
pipenv run python main.py --file <file-location>
```

Replace `<page-number>` with the page number from the FBI API, or replace `<file-location>` with the path to your local JSON file.


## Expected output

When fetching data from the FBI API or loading from a local file, the program should output thorn-separated values for each record, including title, subjects, and field_offices

```bash
John DoeþArmed and Dangerous,AssaultþNew York
Jane SmithþFraudþLos Angeles,Chicago
MARY JOHNSON (DAVIS)þþseattle

```

## Functions

#### main.py
- **fetch_data(page)**: Fetches data from the FBI Wanted API for the specified page.
- **load_local_data(file_location)**: Loads data from the specified local JSON file.
- **extract_data(data)**: Extracts titles, subjects, and field offices from the API or local data.
- **format_data(records)**: Formats the extracted data using thorn-separated formatting.

#### Libraries used
- **argparse**: Used for parsing command-line arguments provided to the script.
- **sys**: Used for exiting the program with error codes and printing errors to stderr.
- **urllib.request**: Used for making HTTP requests to the FBI API to fetch the data.
- **json**: Used for loading and processing JSON data from both the API and local files.


## Testcases

In this project, two test files are used: `test_randompage.py` tests API functionality by fetching data from random pages and verifying fields such as **title**, **subjects**, and **field_offices**, while `test_download.py` tests similar functionality using data loaded from a local file (`loadfile.json`)

#### `test_randompage.py`
- **test_fetch_data**: Ensures that data is successfully fetched and contains non-empty items.

#### `test_download.py`
- **test_load_data**: Ensures that data is successfully loaded from the local JSON file and contains non-empty items.

#### `Common test cases in both `

- **test_extract_title**: Verifies that the title field exists and is a valid string.

- **test_extract_subjects**: Confirms that the subjects field exists and is a valid list.

- **test_extract_field_offices**: Checks if the field_offices field exists and is a list, or is None if not present.

- **test_print_thorn_separated**: Verifies that title, subjects, and field_offices fields are formatted and printed with thorn separators.


## How to run tests:
Make sure the following are installed in your environment:

1. **pipenv**: Used to manage the virtual environment.
2. **pytest**: Python testing framework.

To install all dependencies, run:

```bash
pipenv install

```

To run the testcases you go with the following command:

```bash
pipenv run python -m pytest -v
```


## Bugs and Assumptions:

1.  **Bugs**: 

- If the local file does not exist or is not formatted correctly, the program prints an error message and returns None.

- When fetching data from the FBI API, exceeding the rate limits may result in an HTTP 429 (Too Many Requests) error, causing test failures.

2.  **Assumptions**: 
* The local file should be a valid JSON file that follows the same structure as the FBI API response. The user must provide either a valid page number for the API or a valid file path for the local data.

- It is assumed that each testcases are to be executed on both functions one where data is fetched from the FBI wanted API for a random page, and data loaded from a specified local JSON file in the repository.

- 'docs' is mentioned in the project repo structure and no template or required format for that file in assignment description, consulted TA and advised to skip it for now.

-


