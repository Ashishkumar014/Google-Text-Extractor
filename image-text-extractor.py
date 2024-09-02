import os
import io
import re
import pandas as pd
from google.cloud import vision
from google.cloud import translate_v2 as translate

# Setting up the Google Vision client
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r"C:\path\to\your\google-cloud-service-account-key.json"
client = vision.ImageAnnotatorClient()

# Function to extract text form image


def extract_text_from_image(image_path):
    with io.open(image_path, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)
    response = client.text_detection(image=image)
    texts = response.text_annotations

    if texts:
        # Combine all detected text into one string
        full_text = " ".join([text.description.strip() for text in texts])

        # Remove redundant text by identifying repeated patterns
        # This regex matches repeated patterns and removes them
        pattern = re.compile(r'\b(\w+)(?:[\s\W]+(?:\1\b))+', re.IGNORECASE)
        clean_text = re.sub(pattern, r'\1', full_text)

        # Strip the extra whitespace
        clean_text = re.sub(r'\s+', ' ', clean_text).strip()

        # Translating the cleaned text
        translator = translate.Client()
        res = translator.translate(clean_text, target_language="en")
        # Return the clean, translated text
        return res['translatedText'].strip()

    return ""


def process_images(directory, search_text):
    results = []
    for filename in os.listdir(directory):
        if filename.endswith(('.png', '.jpg', '.jpeg', 'webp')):
            image_path = os.path.join(directory, filename)
            extracted_text = extract_text_from_image(image_path)

            if search_text.lower() in extracted_text.lower():
                results.append((filename, extracted_text))

    return results


def natural_sort_key(s):
    # Extract groups of digits and convert them to integers for natural sorting
    return [int(text) if text.isdigit() else text.lower() for text in re.split(r'(\d+)', s)]


def rank_images(results, search_text):
    if search_text:
        # Rank based on the percentage of matches with the search text
        ranked_results = sorted(results, key=lambda x: x[1].lower().count(
            search_text.lower()), reverse=True)
    else:
        # If no search text is given, rank based on the image name (filename)
        ranked_results = sorted(results, key=lambda x: natural_sort_key(x[0]))

    return ranked_results


def save_to_csv(results, output_csv):
    import pandas as pd
    df = pd.DataFrame(results, columns=["Image Title", "Extracted Text"])
    df.to_csv(output_csv, index=False)


def main():
    image_directory = r"C:\Users\ashis\Documents\001_Programming_related\My_Projects\Google text extractor\Images"
    # Provide search text here.
    search_text = ''
    output_csv = 'Output.csv'

    results = process_images(image_directory, search_text)
    ranked_results = rank_images(results, search_text)
    save_to_csv(ranked_results, output_csv)


if __name__ == "__main__":
    main()
