# GLEAM - Gamified Learning Examiner AI module
# PDF text extraction for syllabus / past papers:

import PyPDF2

class SyllabusParser:
    def extract_text(self, pdf_path):
        try:
            with open(pdf_path, 'rb') as f:
                reader = PyPDF2.PdfReader(f)
                text_pages = []
                for page in reader.pages:
                    text = page.extract_text()
                    if text:
                        text_pages.append(text)
                return " ".join(text_pages)
        except Exception as e:
            raise RuntimeError(f"Error extracting PDF text: {e}")