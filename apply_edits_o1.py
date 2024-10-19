import re

def generate_table_of_contents(content):
    """
    Generates a Markdown Table of Contents based on the headers in the content.
    """
    toc = []
    headers = re.findall(r'^(#{2,6})\s*(.+)$', content, flags=re.MULTILINE)
    for header in headers:
        hashes, title = header
        level = len(hashes) - 1  # Adjust level (h2 -> level 1)
        # Clean the title to create an anchor
        anchor = title.lower()
        anchor = re.sub(r'[^\w\s-]', '', anchor)
        anchor = anchor.strip().replace(' ', '-')
        anchor = re.sub(r'-+', '-', anchor)
        # Indentation for nested headers
        indent = '    ' * (level - 1)
        toc_line = f'{indent}- [{title}](#{anchor})'
        toc.append(toc_line)
    return '\n'.join(toc)

def replace_table_of_contents(content, new_toc):
    """
    Replaces the existing TOC in the content with the new_toc.
    """
    # Define the TOC markers (case-insensitive)
    toc_start_marker = '<!-- TOC START -->'
    toc_end_marker = '<!-- TOC END -->'

    # Create a pattern to match the existing TOC, including the markers
    toc_pattern = re.compile(
        r'<!--\s*TOC START\s*-->.*?<!--\s*TOC END\s*-->',
        flags=re.DOTALL | re.IGNORECASE
    )

    new_toc_block = f'{toc_start_marker}\n{new_toc}\n{toc_end_marker}'

    if toc_pattern.search(content):
        # Replace the existing TOC
        content = toc_pattern.sub(new_toc_block, content)
    else:
        # Insert the TOC after the main title (first level 1 heading)
        main_title_pattern = re.compile(r'^(# .+)$', flags=re.MULTILINE)
        match = main_title_pattern.search(content)
        if match:
            # Insert the TOC after the main title
            insert_position = match.end()
            content = content[:insert_position] + '\n\n' + new_toc_block + '\n' + content[insert_position:]
        else:
            # No main title found; insert TOC at the beginning
            content = new_toc_block + '\n\n' + content

    return content

def apply_edits(content):
    """
    Applies the proposed edits to the provided Markdown content.
    """
    # Replace smart quotes with straight quotes for consistency
    content = content.replace('“', '"').replace('”', '"').replace('’', "'").replace('‘', "'")

    # Standardize the use of hyphens and dashes
    content = content.replace('–', '-').replace('—', '-')

    # Correct capitalization and formatting of specific terms
    content = re.sub(r"Live2D’s", "Live2D's", content)
    content = re.sub(r"Ren’Py", "Ren'Py", content)
    content = re.sub(r"\blip[\s-]?sync\b", "lip-sync", content, flags=re.IGNORECASE)
    content = re.sub(r"\bnon[- ]?Python\b", "non-Python", content, flags=re.IGNORECASE)
    content = re.sub(r"\bCubism sdk\b", "Cubism SDK", content, flags=re.IGNORECASE)
    content = re.sub(r"\bGit hub\b", "GitHub", content, flags=re.IGNORECASE)
    content = re.sub(r"\bLive2D Cubism sdk\b", "Live2D Cubism SDK", content, flags=re.IGNORECASE)

    # Fix grammatical errors and improve clarity
    content = re.sub(r"developer’s", "developers", content)
    content = re.sub(r"developers's", "developers'", content)
    content = re.sub(r"visual novel’s", "visual novels", content)
    content = re.sub(r"conduct thorough testing", "conduct comprehensive testing", content)
    content = re.sub(r"ensure seamless functionality", "ensure seamless integration and functionality", content)
    content = re.sub(r"Robust testing strategies and error handling mechanisms", "Robust testing strategies and error-handling mechanisms", content)
    content = re.sub(r"\bcross platform\b", "cross-platform", content, flags=re.IGNORECASE)
    content = re.sub(r"Set up development environment", "Set up the development environment", content)
    content = re.sub(r"Implement basic model loading and rendering", "Implement basic model-loading and rendering", content)
    content = re.sub(r'\bvisual novel engine\b', 'visual novel engine', content)

    # Ensure consistent formatting for lists and bullet points
    content = re.sub(r"^\s*-\s+([A-Z])", r"- \1", content, flags=re.MULTILINE)
    content = re.sub(r"^\s*-\s+([a-z])", r"- \1", content, flags=re.MULTILINE)
    content = re.sub(r"^\s*- \*\*([A-Z])", r"- **\1", content, flags=re.MULTILINE)

    # Correct typos and inconsistencies in section titles
    # (Optional: you might want to adjust this depending on your actual section numbering)
    # content = re.sub(r"(?<=\n## )(\d+)\. Introduction", "1. Introduction", content)
    # content = re.sub(r"(?<=\n## )(\d+)\. Repository Analysis", "2. Repository Analysis", content)

    # Adjust bullet points to ensure parallel structure
    content = re.sub(r"^-+\s+([A-Za-z])", r"- \1", content, flags=re.MULTILINE)

    # Replace multiple blank lines with a single blank line
    content = re.sub(r"\n{3,}", "\n\n", content)

    # Correct inconsistent use of apostrophes and quotation marks (again, in case any remain)
    content = content.replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"')

    # Remove duplicate section headings
    content = re.sub(r"(## \d+\. Project Structure Analysis)\n+\1", r"\1", content)

    # Ensure consistent spacing around headings
    content = re.sub(r'\n{2,}(##)', r'\n\n\1', content)

    return content

def main():
    # Read the original document
    with open('original_document.md', 'r', encoding='utf-8') as file:
        original_content = file.read()

    # Apply the proposed edits
    revised_content = apply_edits(original_content)

    # Generate the updated Table of Contents
    new_toc = generate_table_of_contents(revised_content)

    # Replace the existing Table of Contents with the new one
    final_content = replace_table_of_contents(revised_content, new_toc)

    # Write the revised document with the updated TOC
    with open('revised_document.md', 'w', encoding='utf-8') as file:
        file.write(final_content)

    print("Revised document with updated Table of Contents has been generated as 'revised_document.md'.")

if __name__ == "__main__":
    main()