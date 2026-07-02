import os, glob, re

base_dir = "/Users/ryo/TISS/tiss-curriculum/output"
files = glob.glob(f"{base_dir}/**/*.md", recursive=True)

# Words to simply remove (with an optional leading space to prevent double spaces)
remove_words = [
    r" Klien\b", r"Klien\b",
    r" Kargo\b", r"Kargo\b",
    r" mutlak\b", r"mutlak\b",
    r" murni\b", r"murni\b",
    r" rupa\b", r"rupa\b",
    r" pilar\b", r"pilar\b",
    r" lisan\b", r"lisan\b",
    r" pangkalan\b", r"pangkalan\b",
    r" dewa\b", r"dewa\b",
    r" maut\b", r"maut\b",
    r" pamor\b", r"pamor\b",
    r" lumbung\b", r"lumbung\b",
    r" kancah\b", r"kancah\b",
    r" kengerian\b", r"kengerian\b",
    r" kawah\b", r"kawah\b",
    r" raksasa\b", r"raksasa\b"
]

replace_map = {
    r" algojo\b": " sensor",
    r"algojo\b": "sensor",
    r" kiamat\b": " insiden",
    r"kiamat\b": "insiden",
    r" pembantaian\b": " pengujian",
    r"pembantaian\b": "pengujian",
    r" letusan\b": " serangan",
    r"letusan\b": "serangan",
    r" mahakarya\b": " dokumen",
    r"mahakarya\b": "dokumen",
    r" sang prajurit\b": " analis",
    r"sang prajurit\b": "analis",
    r" kutukan\b": " ancaman",
    r"kutukan\b": "ancaman"
}

modified_count = 0

for f in files:
    with open(f, "r", encoding="utf-8") as file:
        content = file.read()
    
    orig_content = content
    
    # Apply replacements
    for pattern, repl in replace_map.items():
        content = re.sub(pattern, repl, content)
        
    # Apply removals
    for pattern in remove_words:
        content = re.sub(pattern, "", content)
        
    # Clean up any double spaces created by removals
    content = re.sub(r" +", " ", content)
    # Clean up space before punctuation
    content = re.sub(r" \.", ".", content)
    content = re.sub(r" ,", ",", content)
    content = re.sub(r" \?", "?", content)
    content = re.sub(r" \!", "!", content)
    
    if content != orig_content:
        with open(f, "w", encoding="utf-8") as file:
            file.write(content)
        modified_count += 1

print(f"Sanitized {modified_count} files.")
