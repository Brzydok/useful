# Google Website Tester

This Python script utilizes Selenium to automate testing on the Google website.

## Requirements

- Python 3.x
- [Selenium](https://pypi.org/project/selenium/) library
- [ChromeDriver](https://sites.google.com/chromium.org/driver/) (Download appropriate driver for your browser)

## How to Use

1. **Install the required libraries:**

    ```bash
    pip install selenium
    ```

2. **Clone the repository:**

    ```bash
    git clone https://github.com/your_username/your_repository.git
    cd your_repository
    ```

3. **Download and set the path to ChromeDriver:**

    Download ChromeDriver: [here](https://sites.google.com/chromium.org/driver/)

4. **Update the script with the path to ChromeDriver:**

    ```python
    # Set the path to the webdriver executable (you need to download the appropriate driver for your browser)
    # Download ChromeDriver: https://sites.google.com/chromium.org/driver/
    driver_path = 'path/to/chromedriver'
    ```

5. **Run the script:**

    ```bash
    python google_tester.py
    ```

   Replace `google_tester.py` with the actual filename of your Python script.

6. **The script will open Google's homepage, perform a search, and capture the search results.**

7. **Printed search results titles will be displayed in the console.**

8. **Close the browser window.**

**Note:** Ensure that you have the appropriate permissions and adhere to the terms of service when using this script.

## Disclaimer

This script is provided for educational purposes only. Automated testing should comply with website terms of service.
