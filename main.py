import sys

from llm import ask_llm
from prompts import (
    SUMMARY_PROMPT,
    EXTRACTION_PROMPT,
    EXCLUSION_PROMPT,
    VALIDATION_PROMPT
)

def read_document(path):
    
    with open(path, "r", encoding="utf-8") as file:
        return file.read()

file_path = sys.argv[1]

policy = read_document(file_path)

summary = ask_llm(
    SUMMARY_PROMPT.format(policy=policy)
)

coverages = ask_llm(
    EXTRACTION_PROMPT.format(policy=policy)
)

exclusions = ask_llm(
    EXCLUSION_PROMPT.format(policy=policy)
)

validation = ask_llm(
    VALIDATION_PROMPT.format(
        policy=policy,
        summary=summary,
        coverage_json=coverages,
        exclusions=exclusions
    )
)

print("\nSUMMARY:")
print(summary)

print("\nCOVERAGES:")
print(coverages)

print("\nEXCLUSIONS:")
print(exclusions)

print("\nSELF-CHECK REPORT:")
print(validation)