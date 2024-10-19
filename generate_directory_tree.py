import os
import sys

def get_directory_tree(directory, prefix=""):
    tree = []
    entries = sorted(os.scandir(directory), key=lambda e: e.name)
    entries = [e for e in entries if e.is_dir()]
    
    for i, entry in enumerate(entries):
        is_last = i == len(entries) - 1
        tree.append(f"{prefix}{'└── ' if is_last else '├── '}{entry.name}")
        if entry.is_dir():
            extension = "    " if is_last else "│   "
            tree.extend(get_directory_tree(entry.path, prefix + extension))
    return tree

# Get the directory of the script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Generate the tree
tree_content = "\n".join(get_directory_tree(script_dir))

# Create the Markdown content
markdown_content = f"```\n{tree_content}\n```"

# Write to file
output_file = os.path.join(script_dir, "directory_structure.md")
with open(output_file, "w", encoding="utf-8") as f:
    f.write(markdown_content)

print(f"Markdown file created: {output_file}")