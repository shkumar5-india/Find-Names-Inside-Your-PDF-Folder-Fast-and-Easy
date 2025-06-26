import os
import shutil
import pytesseract
from pdf2image import convert_from_path
from PIL import Image
from concurrent.futures import ProcessPoolExecutor, as_completed
from tqdm import tqdm

# Set tesseract path (if not in PATH)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Paths
pdf_folder = r"D:\Advanced-Individual Certificates"
poppler_path = r"E:\poppler-24.08.0\Library\bin"
matched_folder = "matched_pdfs"
temp_folder = "temp_images"

# Worker function
def process_pdf(filename_and_search):
    filename, search_name = filename_and_search
    pdf_path = os.path.join(pdf_folder, filename)
    try:
        images = convert_from_path(
            pdf_path,
            dpi=150,
            first_page=1,
            last_page=1,
            fmt='png',
            output_folder=temp_folder,
            paths_only=True,
            poppler_path=poppler_path
        )

        for img_path in images:
            text = pytesseract.image_to_string(Image.open(img_path))
            os.remove(img_path)  # clean up
            if search_name in text.lower():
                shutil.copy2(pdf_path, os.path.join(matched_folder, filename))
                return filename  # match found

    except Exception as e:
        return f"ERROR: {filename} - {e}"
    
    return None  # no match

# === Must be protected on Windows ===
if __name__ == '__main__':
    search_name = input("Enter the name to search: ").strip().lower()

    os.makedirs(matched_folder, exist_ok=True)
    os.makedirs(temp_folder, exist_ok=True)

    pdf_files = [f for f in os.listdir(pdf_folder) if f.lower().endswith(".pdf")]

    print(f"\n🔍 Searching for '{search_name}' in {len(pdf_files)} PDFs...\n")

    matches = []

    with ProcessPoolExecutor() as executor:
        tasks = [(f, search_name) for f in pdf_files]
        futures = {executor.submit(process_pdf, arg): arg[0] for arg in tasks}

        for future in tqdm(as_completed(futures), total=len(futures), desc="Processing"):
            result = future.result()
            if result and not result.startswith("ERROR"):
                matches.append(result)
            elif result and result.startswith("ERROR"):
                print(result)

    print("\n=== RESULTS ===")
    if matches:
        for match in matches:
            print(f"✔️ {match}")
        print(f"\n✅ Found '{search_name}' in {len(matches)} file(s). PDFs copied to: {matched_folder}")
    else:
        print(f"❌ No matches found for '{search_name}'.")
