# Setup guide
#### Installation

1. **Install Python (if you haven't already)**:
    - Link: https://www.python.org/downloads/

2. **Install packages in requirements.txt**:
    ```bash
    pip install -r requirements.txt
    ```

# About the tool
* This is a simple quoting tool that I developed for my partner to use for her goldsmith business.

* It takes in cost price, hours spent, wage, and margin, and then outputs the calculated quote.

* Screenshot:



# How to use the tool
1.  Open the folder in your IDE

2. Run the following command to create the GUI app:
    - This will create the an executable 'tool' in the dist folder.
    ```bash
    pyinstaller --onefile --windowed tool.py
    ```
3. Navigate to the 'dist' folder and double-click the app to open up the GUI.

# Testing
    - The unit test is written using Pytest, to run the test simply run the following command in your terminal:
    ```bash
    pytest
    ```