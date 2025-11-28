import re

file_path = r'c:\Users\vivek\Desktop\ATC\final_report.tex'

with open(file_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_lines = []
i = 0
while i < len(lines):
    line = lines[i]
    if line.strip() == r'\clearpage':
        # Check next lines for \subsection
        j = i + 1
        found_subsection = False
        while j < len(lines):
            next_line = lines[j].strip()
            if next_line == '':
                j += 1
                continue
            if next_line.startswith(r'\subsection'):
                found_subsection = True
            break
        
        if found_subsection:
            # Skip this clearpage
            i += 1
            continue
    
    new_lines.append(line)
    i += 1

with open(file_path, 'w', encoding='utf-8') as f:
    f.writelines(new_lines)

print("Processed file.")
