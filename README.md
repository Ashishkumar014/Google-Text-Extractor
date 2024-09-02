# Google Text Extractor

### Key Sections Explained:
- **Overview**: Brief description of the project.
- **Features**: List of features provided by the project.
- **Prerequisites**: Requirements for setting up and using the project.
- **Installation**: Instructions for installing and setting up the project.
- **Usage**: How to run the script and check results.
- **Functions**: Brief overview of the key functions in the code.
- **Contributing**: Guidelines for contributing to the project.
- **Contact**: How to get in touch for questions or feedback.

Image file link: "https://drive.google.com/drive/folders/1-8O9FTcpX7v1DqSyz-g0yj4GY32deS4v?usp=sharing"

## Overview

The Google Text Extractor is a Python project that utilizes Google Cloud Vision and Google Translate APIs to extract and translate text from images. The extracted text is then processed to find and rank images based on user-defined search terms. The results are saved to a CSV file for easy analysis.

## Features

- **Text Extraction**: Uses Google Cloud Vision API to extract text from images.
- **Translation**: Translates extracted text to English using Google Translate API.
- **Text Matching**: Finds and ranks images based on matching text with a search term.
- **Ranking and Sorting**: Ranks images based on text matches or filename if no search term is provided.
- **CSV Output**: Saves the results to a CSV file.

## Prerequisites

1. **Google Cloud Account**: Set up a Google Cloud project and enable the Vision and Translate APIs.
2. **Service Account Key**: Obtain a JSON key file for your Google Cloud service account.

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/google-text-extractor.git
   cd google-text-extractor
2. Set Up Virtual Environment (Optional but recommended):
python -m venv venv
source venv/bin/activate   # On Windows use `venv\Scripts\activate`

3. Install Dependencies:
pip install -r requirements.txt

Set Up Google Cloud Credentials:

Download your service account key file from Google Cloud.
Set the environment variable GOOGLE_APPLICATION_CREDENTIALS to point to your key file:
export GOOGLE_APPLICATION_CREDENTIALS="path/to/your/service-account-key.json"

Usage
Prepare Your Images: Place your images in a directory.

Run the Script:

Edit the main() function in image-text-extractor.py to specify the image_directory, search_text, and output_csv.
Execute the script:
bash
Copy code
python image-text-extractor.py
Check Results: The results will be saved in the specified CSV file.

Functions
extract_text_from_image(image_path): Extracts and translates text from an image.
process_images(directory, search_text): Processes images in a directory and matches them with the search text.
rank_images(results, search_text): Ranks images based on the percentage of matches with the search text or by filename.
save_to_csv(results, output_csv): Saves the results to a CSV file.
Requirements
Python 3.x
google-cloud-vision
google-cloud-translate
pandas
re

Contributing
Feel free to open issues or submit pull requests to contribute to this project. For major changes, please open an issue first to discuss what you would like to change.

Contact
For any questions or feedback, please reach out to ashishkumar.nitrr@gmail.com.


