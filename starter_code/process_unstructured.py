import re

def clean_text(text: str) -> str:
    if not text:
        return ""
    text = text.strip()
    text = re.sub(r'\s+', ' ', text)
    return text

def process_pdf_data(raw_json: dict) -> dict:
    raw_text = raw_json.get("extractedText", "")
    cleaned_content = re.sub(r'HEADER_PAGE_\d+', '', raw_text)
    cleaned_content = re.sub(r'FOOTER_PAGE_\d+', '', cleaned_content)
    cleaned_content = clean_text(cleaned_content)
    
    return {
        "document_id": str(raw_json.get("docId", "")),
        "source_type": "PDF",
        "author": str(raw_json.get("authorName", "Unknown")).strip(),
        "category": str(raw_json.get("docCategory", "Unknown")).strip(),
        "content": cleaned_content,
        "timestamp": str(raw_json.get("createdAt", "Unknown")).strip()
    }

def process_video_data(raw_json: dict) -> dict:
    raw_text = raw_json.get("transcript", "")
    cleaned_content = re.sub(r'\[.*?\]', '', raw_text)
    cleaned_content = clean_text(cleaned_content)
    
    return {
        "document_id": str(raw_json.get("video_id", "")),
        "source_type": "Video",
        "author": str(raw_json.get("creator_name", "Unknown")).strip(),
        "category": str(raw_json.get("category", "Unknown")).strip(),
        "content": cleaned_content,
        "timestamp": str(raw_json.get("published_timestamp", "Unknown")).strip()
    }
