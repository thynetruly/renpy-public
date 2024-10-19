import re

def add_timeline_section(content):
    timeline_section = """
## Project Timeline and Milestones

This section outlines the proposed timeline and key milestones for the Live2D Cubism SDK integration with Ren'Py.

1. **Phase 1: Initial Analysis and Setup (Weeks 1-2)**
   - Complete repository analysis
   - Set up development environment
   - Finalize project structure

2. **Phase 2: Core Integration (Weeks 3-6)**
   - Implement basic model loading and rendering
   - Develop animation control system
   - Integrate lip sync functionality

3. **Phase 3: Advanced Features (Weeks 7-10)**
   - Implement physics simulations
   - Develop shader system
   - Create particle system

4. **Phase 4: Optimization and Testing (Weeks 11-13)**
   - Perform performance optimizations
   - Conduct thorough testing (unit, integration, cross-platform)
   - Address identified issues and bugs

5. **Phase 5: Documentation and Refinement (Weeks 14-15)**
   - Complete API documentation
   - Refine user guides and examples
   - Conduct final review and adjustments

6. **Phase 6: Release and Support (Week 16)**
   - Prepare for initial release
   - Set up support channels and documentation portals

Note: This timeline is subject to adjustment based on project progress and any unforeseen challenges.

"""
    # Find the position after the Executive Summary
    exec_summary_end = content.find("## Table of Contents")
    if exec_summary_end == -1:
        # If "## Table of Contents" is not found, insert at the beginning
        return timeline_section + content
    else:
        # Insert the timeline section after the Executive Summary
        return content[:exec_summary_end] + timeline_section + content[exec_summary_end:]

# Read the existing document
with open('document_revised.md', 'r', encoding='utf-8') as file:
    content = file.read()

# Add the timeline section
updated_content = add_timeline_section(content)

# Write the updated content back to the file
with open('document_revised_with_timeline.md', 'w', encoding='utf-8') as file:
    file.write(updated_content)

print("Timeline section has been added to the document. The updated document is saved as 'document_revised_with_timeline.md'.")