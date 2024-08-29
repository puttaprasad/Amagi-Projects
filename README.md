<!--Task1: Video Analysis Automation with pytest -->
This project automates the analysis of a provided video to detect and validate the presence of blank screens using Python and pytest. The goal of this test is to ensure that any blank frames in the video are detected accurately.

<!-- Table of Contents -->
Project Overview
Setup Instructions
Running the Tests
Test Structure
Example Usage

<!-- Project Overview -->
The test case focuses on analyzing the frames of a video file to detect any blank screens. Blank screens are defined as frames where the pixel values are all or nearly the same, indicating a lack of content.

The test case is written using the pytest framework and uses OpenCV for video processing. The primary steps involved include:

Reading the video frame by frame.
Analyzing each frame for blank screens.
Reporting the presence of blank screens as pass or fail criteria.

<!-- Install Required Packages -->
Install the necessary dependencies by running:

bash
Copy code
pip install -r requirements.txt
The requirements.txt file includes the following dependencies:

pytest
opencv-python

<!-- Prepare the Video for Analysis -->
Ensure the video you want to analyze is placed in the videos folder within the project directory. The test script will use this folder to locate and process the video file.

Running the Tests
To run the test cases, simply execute the following command in the terminal:

bash
Copy code
pytest --html=report.html --self-contained-html
This will run the test case and generate an HTML report (report.html) with the results.

Custom Options
You can pass a specific video file to the test by modifying the test case script or by using a configuration file.

<!-- Test Workflow: -->
Load the video file using OpenCV.
Iterate through each frame of the video.
Check if the frame is a blank screen (all pixels are the same or within a defined threshold).
Record the results and generate a report.


<!-- Example Usage -->
Here's an example of how to use the test suite:

Place your video file (e.g., test_video.mp4) in the videos folder.

<!-- Run the test using pytest: -->

bash
Copy code
pytest --html=report.html --self-contained-html
Check the generated report.html file for the test results.


<!--Task2: HTML report is generated, email the reports -->

<!-- Table of Contents -->
Project Overview
Setup Instructions
Running the Tests
Emailing the Report
Test Structure

<!-- Project Overview -->
The goal of this project is to develop 10 test cases with the pytest framework. After running the tests, an HTML report is generated using pytest's --html plugin. This report is then automatically emailed to a designated Gmail account using Python's smtplib module.

<!-- Key features: -->

10 test cases: 7 passing tests and 3 failing tests.
HTML report generation using pytest's HTML plugin.
Automated email delivery of the HTML report.

<!-- Create a Virtual Environment (Optional but Recommended) -->

bash
Copy code
python -m venv venv
source venv/bin/activate   # For Linux/macOS
venv\Scripts\activate      # For Windows

<!-- Install Required Packages -->
Install the necessary dependencies by running:


pip install -r requirements.txt
The requirements.txt file includes the following dependencies:

pytest
pytest-html
smtplib (built into Python)

<!-- Configure Email Credentials -->
Update the send_email() function in the script with your Gmail credentials (use an app password if two-factor authentication is enabled). Ensure that the recipient email is correct.

Running the Tests
To run the tests and generate the HTML report, use the following command:

pytest --html=report.html --self-contained-html
This command will run all the test scripts and create an HTML report named report.html.

<!-- Emailing the Report -->
Once the tests are executed and the HTML report is generated, the report is automatically emailed to the specified Gmail account. Ensure that:

The correct email credentials are provided.
Gmail's security settings allow sending emails from your Python script (e.g., using App Passwords if two-factor authentication is enabled).
<!-- How it Works: -->
Run Tests: The tests are executed using pytest.
Generate Report: The pytest-html plugin generates a report after the test run.
Send Email: A Python script is used to send the generated report as an email attachment to the specified recipient.
<!-- Test Structure -->
test_suite.py: Contains 10 test cases. Seven of them are designed to pass, and three are designed to fail.
email_report.py: A script that handles sending the HTML report via email after the tests are run.
<!-- Example Usage -->
Run the tests and generate the report:

pytest --html=report.html --self-contained-html
The email_report.py script will automatically email the report to the designated recipient.