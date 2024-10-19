import re

def add_executive_summary(content):
    summary = """
# Executive Summary

This Software Engineering Architectural Design Document outlines the comprehensive plan for integrating the Live2D Cubism SDK with the Ren'Py visual novel engine. The integration aims to enhance Ren'Py projects with dynamic and expressive character animations using Live2D models.

Key aspects of the integration plan include:

1. Detailed analysis of both Ren'Py and Live2D Cubism SDK codebases
2. Proposed modular architecture for seamless integration
3. Comprehensive implementation strategies for core functionalities
4. Performance optimization techniques and cross-platform compatibility considerations
5. Robust testing strategies and error handling mechanisms
6. Guidelines for documentation, coding standards, and future enhancements

This document serves as a strategic roadmap for developers, providing in-depth technical guidance to ensure a successful integration that leverages the strengths of both Ren'Py and Live2D Cubism SDK.
"""
    return summary + "\n\n" + content

def add_glossary(content):
    glossary = """
# Glossary

- **API**: Application Programming Interface
- **CI/CD**: Continuous Integration/Continuous Deployment
- **GPU**: Graphics Processing Unit
- **IDE**: Integrated Development Environment
- **Live2D**: A software for creating 2D models with realistic movements
- **LOD**: Level of Detail
- **Ren'Py**: A visual novel engine that facilitates the creation of interactive storytelling experiences
- **SDK**: Software Development Kit
- **UI**: User Interface
- **UML**: Unified Modeling Language
- **Viseme**: A visual representation of a phoneme or unit of sound in speech
"""
    return content.split("## 1. Introduction")[0] + glossary + "\n\n## 1. Introduction" + content.split("## 1. Introduction")[1]

def update_table_of_contents(content):
    new_toc = """
# Software Engineering Architectural Design Document

## Table of Contents

1. [Introduction](#1-introduction)
2. [Repository Analysis](#2-repository-analysis)
   2.1 [Ren'Py GitHub Repository](#21-renpy-github-repository)
   2.2 [Live2D Cubism SDK](#22-live2d-cubism-sdk)
3. [Project Structure Analysis](#3-project-structure-analysis)
   3.1 [Ren'Py Project Structure](#31-renpy-project-structure)
   3.2 [Live2D Cubism SDK Project Structure](#32-live2d-cubism-sdk-project-structure)
   3.3 [Optimized Integrated Project Structure](#33-optimized-integrated-project-structure)
   3.4 [UML Diagram of Integrated Architecture](#34-uml-diagram-of-integrated-architecture)
   3.5 [Recommendations for Project Structure Improvements](#35-recommendations-for-project-structure-improvements)
4. [Code Purpose and Functionality Summary](#4-code-purpose-and-functionality-summary)
5. [Bug Identification and Potential Improvements](#5-bug-identification-and-potential-improvements)
6. [Discrepancies and Redundancies Addressed](#6-discrepancies-and-redundancies-addressed)
7. [Integration with Ren'Py and Live2D Cubism Systems](#7-integration-with-renpy-and-live2d-cubism-systems)
8. [Code Modification Suggestions](#8-code-modification-suggestions)
9. [Performance Optimization and Compatibility](#9-performance-optimization-and-compatibility)
10. [Code Translation from Non-Python to Python](#10-code-translation-from-non-python-to-python)
11. [Component Listing and Interactions](#11-component-listing-and-interactions)
12. [Python Code Snippets for Key Functions](#12-python-code-snippets-for-key-functions)
13. [Integration with Existing Ren'Py Systems](#13-integration-with-existing-renpy-systems)
14. [Performance Bottlenecks and Optimizations](#14-performance-bottlenecks-and-optimizations)
15. [Cross-Platform Compatibility](#15-cross-platform-compatibility)
16. [Implementation of Cubism Core API and Live2D Cubism SDK](#16-implementation-of-cubism-core-api-and-live2d-cubism-sdk)
17. [Model Loading, Rendering, and Animation](#17-model-loading-rendering-and-animation)
18. [Automatic Eye Blinking and Mouth Movement](#18-automatic-eye-blinking-and-mouth-movement)
19. [Physics Simulation](#19-physics-simulation)
20. [User Data Handling](#20-user-data-handling)
21. [Shader System Development](#21-shader-system-development)
22. [Particle System Implementation](#22-particle-system-implementation)
23. [Rendering Pipeline Blend Modes Support](#23-rendering-pipeline-blend-modes-support)
24. [Shader Parameter Adjustment Interfaces](#24-shader-parameter-adjustment-interfaces)
25. [Voiceover System with Lip Sync and Visemes](#25-voiceover-system-with-lip-sync-and-visemes)
26. [Phoneme Extraction from Audio Files](#26-phoneme-extraction-from-audio-files)
27. [Cursor Tracking for Interactive Elements](#27-cursor-tracking-for-interactive-elements)
28. [Expression System for Characters](#28-expression-system-for-characters)
29. [Localization and Translation Improvements](#29-localization-and-translation-improvements)
30. [Performance Bottlenecks and Optimization Strategies](#30-performance-bottlenecks-and-optimization-strategies)
31. [Integration Plan with Ren'Py Codebase](#31-integration-plan-with-renpy-codebase)
32. [Testing Strategies](#32-testing-strategies)
33. [Impact on Other Ren'Py Systems and Mitigation](#33-impact-on-other-renpy-systems-and-mitigation)
34. [Error Handling and Debugging Strategies](#34-error-handling-and-debugging-strategies)
35. [API Reference with Code Examples](#35-api-reference-with-code-examples)
36. [Example Ren'Py Scripts Demonstrating Live2D Features](#36-example-renpy-scripts-demonstrating-live2d-features)
37. [Documentation and Commenting Standards](#37-documentation-and-commenting-standards)
38. [Step-by-Step Coding Guidelines](#38-step-by-step-coding-guidelines)
39. [Key Challenges and Solutions](#39-key-challenges-and-solutions)
40. [Remaining Concerns and Issues](#40-remaining-concerns-and-issues)
41. [Process Improvements for Future Features](#41-process-improvements-for-future-features)
42. [Areas for Further Enhancement](#42-areas-for-further-enhancement)
43. [Final Recommendations](#43-final-recommendations)
44. [Review and Refinement](#44-review-and-refinement)
"""
    return re.sub(r'## Table of Contents.*?(?=##)', new_toc, content, flags=re.DOTALL)

def add_cross_references(content):
    cross_refs = {
        "1": ["2", "3"],
        "2": ["1", "3", "4"],
        "3": ["2", "4", "5"],
        "4": ["3", "5", "6"],
        "5": ["4", "6", "14"],
        "6": ["5", "7"],
        "7": ["6", "8", "13"],
        "8": ["7", "9"],
        "9": ["8", "14", "15"],
        "10": ["9", "11"],
        "11": ["10", "12"],
        "12": ["11", "13"],
        "13": ["7", "12", "14"],
        "14": ["5", "9", "13"],
        "15": ["9", "14"],
        "16": ["7", "17"],
        "17": ["16", "18"],
        "18": ["17", "19"],
        "19": ["18", "20"],
        "20": ["19", "21"],
        "21": ["20", "22"],
        "22": ["21", "23"],
        "23": ["22", "24"],
        "24": ["23", "25"],
        "25": ["24", "26"],
        "26": ["25", "27"],
        "27": ["26", "28"],
        "28": ["27", "29"],
        "29": ["28", "30"],
        "30": ["14", "29", "31"],
        "31": ["13", "30", "32"],
        "32": ["31", "33"],
        "33": ["32", "34"],
        "34": ["33", "35"],
        "35": ["34", "36"],
        "36": ["35", "37"],
        "37": ["36", "38"],
        "38": ["37", "39"],
        "39": ["38", "40"],
        "40": ["39", "41"],
        "41": ["40", "42"],
        "42": ["41", "43"],
        "43": ["42", "44"],
        "44": ["43"]
    }

    def get_section_title(section_num):
        match = re.search(rf"^## {section_num}\. (.+)$", content, re.MULTILINE)
        return match.group(1) if match else f"Section {section_num}"

    def create_ref_link(section_num):
        title = get_section_title(section_num)
        return f"[{section_num}. {title}](#{section_num}-{'-'.join(title.lower().split())})"

    for section, refs in cross_refs.items():
        section_pattern = f"^## {section}\\. "
        ref_links = [create_ref_link(ref) for ref in refs]
        ref_text = "\n\n[Related sections: " + ", ".join(ref_links) + "]\n"
        content = re.sub(f"({section_pattern}.+\n)", f"\\1{ref_text}", content, flags=re.MULTILINE)

    return content

def apply_formatting_fixes(content):
    # Ensure consistent indentation in code blocks
    content = re.sub(r'(```[\w]*\n)(?!    )', r'\1    ', content)
    
    # Ensure consistent language specifiers for code blocks
    content = re.sub(r'```python:path', r'```python', content)
    content = re.sub(r'```renpy:path', r'```renpy', content)
    
    return content

def apply_revisions(content):
    content = add_executive_summary(content)
    content = add_glossary(content)
    content = update_table_of_contents(content)
    content = add_cross_references(content)
    content = apply_formatting_fixes(content)
    return content

# Read the original document
with open('document.md', 'r', encoding='utf-8') as file:
    original_content = file.read()

# Apply all revisions
updated_content = apply_revisions(original_content)

# Write the updated document
with open('document_revised.md', 'w', encoding='utf-8') as file:
    file.write(updated_content)

print("All revisions have been applied. The updated document is saved as 'document_revised.md'.")