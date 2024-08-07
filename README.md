# Kindle Clippings to DataFrame

This script extracts highlights, notes, and bookmarks from the `clippings.txt` file of a Kindle device and transforms them into a DataFrame.

## Features

- Parses highlights from `clippings.txt`
- Updates an existing CSV file with new highlights, removing duplicates
- Saves the updated highlights to a CSV file

## Requirements

- Python 3.x
- pandas

## Installation

1. Clone this repository.
2. Install the required packages:
```bash
 pip install pandas
```

## Usage

1. Ensure you have the `clippings.txt` file from your Kindle device.
2. Place the `clippings.txt` file in the same directory as the script.
3. Run the script:
```bash
python kindle_clippings.py
```

### Example

After running the script, the highlights will be parsed from `clippings.txt` and saved to `highlights.csv`. Any new highlights will be added to the existing highlights, and duplicates will be removed.

## Script Details

- **parse_highlights(file_path)**: Function to extract highlights from the text file and return a DataFrame.
- **update_highlights(new_file_path, existing_df_path)**: Function to read new highlights, update the existing DataFrame, and save the combined DataFrame to a CSV file.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

For more information, please contact:

- Email: robertdsgabriel@gmail.com
  
- GitHub: [r0bert](https://github.com/r0bertds)
