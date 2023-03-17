# Automated Time Sheet Completer

This Python script automates the process of filling out employee time attendance using Selenium for web automation. It streamlines the process, reducing the time spent on manual data entry while improving the user experience.

## Features

- Automatically enters time slots for multiple days of the week
- Secure password entry and error handling
- Significant time savings by automating repetitive tasks

## Prerequisites

- Python 3.x
- Selenium
- Chrome WebDriver

## Installation

1. Install Python 3.x from the [official website](https://www.python.org/downloads/).
2. Install Selenium using pip:

```bash
pip install selenium
```

3. Download the [Chrome WebDriver](https://sites.google.com/a/chromium.org/chromedriver/downloads) that matches your Chrome version and place it in a known location.

## Usage

1. Update the `executable_path` variable in the script with the path to your Chrome WebDriver:

```python
service = ChromeService(executable_path="C:\\PATH\\TO\\CHROME\\DRIVER\\HERE")
```

2. Run the script:

```bash
python automated_time_sheet_completer.py
```

3. Enter your email and password when prompted.

4. The script will automatically navigate to the time attendance page, enter time slots for each day of the week, and submit the form.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
