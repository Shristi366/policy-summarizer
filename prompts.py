SUMMARY_PROMPT = """
You are an insurance analyst.

Read the policy carefully.

Think through the document step by step:

1. Identify coverages
2. Identify limits
3. Identify deductibles
4. Identify exclusions
5. Determine the most important customer-facing points

After reasoning, provide ONLY:

- bullet 1
- bullet 2
- bullet 3
- bullet 4
- bullet 5

Policy:

{policy}
"""


EXTRACTION_PROMPT = """
Example 1

Policy:
Building Coverage Limit $500,000
Liability Limit $1,000,000

Output:

{{
   "building": 500000,
   "liability": 1000000
}}

Example 2

Policy:
Personal Property Limit $50,000
Medical Payments Limit $10,000

Output:

{{
   "personal_property": 50000,
   "medical_payments": 10000
}}

Now extract coverage limits from:

{policy}

Return ONLY valid JSON.
"""


EXCLUSION_PROMPT = """
Extract all exclusions.

Return:

- item
- item
- item

Policy:

{policy}
"""


VALIDATION_PROMPT = """
You are a QA reviewer.

Source Policy:

{policy}

Generated Summary:

{summary}

Coverage JSON:

{coverage_json}

Exclusions:

{exclusions}

Check:

1. Is every summary statement supported?
2. Any hallucinations?
3. Any incorrect coverage limits?
4. Any missing exclusions?

Return:

✓ Correct findings

⚠ Issues found
"""