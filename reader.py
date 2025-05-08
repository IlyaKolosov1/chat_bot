import docx

def getText(filename: str) -> str:
    
    doc = docx.Document(filename)
    full_text = []
    for paraghap in doc.paragraphs:
        full_text.append(paraghap.text)

    return '\n'.join(full_text)

