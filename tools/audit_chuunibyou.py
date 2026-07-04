import os
import re

TARGET_DIR = "/Users/ryo/TISS/tiss-curriculum/source-material"

substitutions = {
    r"\blaksana\b": "seperti",
    r"\bmeronta\b": "muncul",
    r"\bmeratapi\b": "menyadari",
    r"\bsakral\b": "krusial",
    r"\bdiharamkan\b": "tidak diperbolehkan",
    r"\bpemusnah\b": "eksekutor",
    r"\bmemusnahkan\b": "mengeksekusi",
    r"\bjendela rahim\b": "halaman utama",
    r"\baltar pengujian\b": "lingkungan pengujian"
}

def case_preserving_replace(match, repl):
    word = match.group(0)
    # Special multi-word cases
    if "jendela rahim" in word.lower() or "altar pengujian" in word.lower():
        return repl
        
    if word.isupper():
        return repl.upper()
    elif word.istitle():
        return repl.title()
    else:
        return repl.lower()

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content
    for pattern, replacement in substitutions.items():
        content = re.sub(pattern, lambda m, r=replacement: case_preserving_replace(m, r), content, flags=re.IGNORECASE)

    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

modified_count = 0
for root, dirs, files in os.walk(TARGET_DIR):
    for file in files:
        if file.endswith(".md"):
            if process_file(os.path.join(root, file)):
                modified_count += 1

print(f"Successfully processed {modified_count} files.")
