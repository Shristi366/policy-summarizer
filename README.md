# P&C Policy Summariser CLI Tool

Phase Gate 1 Project — A Python CLI tool that processes Property & Casualty (P&C) insurance policy documents and generates customer-friendly summaries using LLM-based analysis.

## Overview

Insurance policies contain complex legal and technical language that can be difficult for customers to understand.

This project builds a command-line tool that takes a P&C insurance policy document as input and uses an LLM to generate:

* A plain-English summary in 5 bullet points
* Key coverage limits in structured JSON format
* A list of policy exclusions
* A self-check validation step where the LLM compares its generated output against the original policy document and identifies possible inconsistencies

---

# What it does

The tool:

1. Reads a policy document from the `policies` folder
2. Sends the document content to an LLM with custom prompts
3. Generates:

   * Policy summary
   * Coverage details
   * Exclusions
   * Validation report
4. Displays the results through a CLI interface

---

# Project Structure

```
policy_summarizer/

│
├── policies/
│   ├── auto_insurance.txt
│   ├── travel_insurance.txt
│   └── home_insurance.txt
│
├── .env                   # API keys (not uploaded)
│
├── llm.py                 # LLM helper and model interaction
│
├── main.py                # CLI application entry point
│
├── prompts.py             # Prompt templates for LLM tasks
│
├── requirements.txt       # Python dependencies
│
└── README.md              # Project documentation
```

---

# Setup

## 1. Clone the repository

```bash
git clone <repository-url>
```

Move into the project folder:

```bash
cd policy_summarizer
```

---

## 2. Create virtual environment

Create a Python virtual environment:

```bash
python -m venv venv
```

Activate it:

### Windows

```bash
venv\Scripts\activate
```

### Mac/Linux

```bash
source venv/bin/activate
```

---

## 3. Install dependencies

Install required Python packages:

```bash
pip install -r requirements.txt
```

---

## 4. Configure API keys

Create a `.env` file in the project root:

```
GEMINI_API_KEY=your_gemini_api_key
GROQ_API_KEY=your_groq_api_key
```

The `.env` file is ignored by Git and should not be uploaded to GitHub.

---

# Running the Application

Run the CLI tool:

```bash
python main.py ./policies/auto_insurance.txt
```

The tool will generate:

1. Policy summary
2. Coverage limits JSON
3. Exclusions list
4. Self-check validation result

---

# Models Used

## Primary Model

Google Gemini

Purpose:

* Policy understanding
* Summary generation
* Information extraction

---

## Fallback Model

Groq Llama model

Purpose:

* Backup LLM provider if the primary model is unavailable

---

# Prompt Engineering Approach

## 1. Chain-of-Thought Prompting for Summary Generation

Chain-of-thought prompting was used for the summarization task.

The goal was to help the model analyze the policy document carefully before generating a short customer-friendly summary.

Benefits:

* Better understanding of complex insurance wording
* Reduced missing information
* Improved summary quality

---

## 2. Few-Shot Prompting for Structured Extraction

Few-shot examples were used for extracting coverage limits into JSON format.

The prompt provides examples of:

* Expected JSON structure
* Important fields
* Formatting requirements

Benefits:

* More consistent outputs
* Easier downstream processing
* Improved extraction accuracy

---

# Policy Documents Tested

The tool was tested with three fictional P&C insurance policy documents:

## 1. Auto Insurance Policy

Contains:

* Vehicle coverage details
* Accident coverage
* Deductibles
* Claim conditions

## 2. Travel Insurance Policy

Contains:

* Trip coverage
* Medical coverage
* Cancellation benefits
* Exclusions

## 3. Home Insurance Policy

Contains:

* Property coverage
* Damage protection
* Coverage limits
* Excluded events

All documents are fictional and contain no proprietary or client information.

---

# Example Output

When the tool processes a policy document, it generates four sections:

## 1. Policy Summary

Example:

```
SUMMARY:

* The policy provides various coverages, including Third Party Bodily Injury Liability, Third Party Property Damage Liability, Own Damage Coverage, Collision Coverage, Comprehensive Coverage, and Personal Accident Cover.

* The limits of the policy include Unlimited Third Party Bodily Injury Liability, ₹7,50,000 for Third Party Property Damage Liability, ₹18,00,000 for Own Damage Coverage, and ₹15,00,000 for Personal Accident Cover.

* The deductibles applicable to the policy are ₹1,000 (compulsory deductible) for Collision Coverage and ₹500 (voluntary deductible) for Comprehensive Coverage, if opted.

* The policy excludes certain events, such as driving under influence, using the vehicle for commercial purposes without endorsement, intentional damage, mechanical breakdown, and damage occurring outside India.

* Important customer-facing points include the major coverage limits, available discounts such as No Claim Bonus and Anti-theft Device Discount, and optional add-ons like Rental Reimbursement and Roadside Assistance.
```

---

## 2. Coverage Limits (JSON)

The tool extracts important coverage details into structured JSON:

```json
{
   "third_party_bodily_injury_liability": "Unlimited",
   "third_party_property_damage_liability": 750000,
   "own_damage_coverage": 1800000,
   "collision_coverage_deductible": 1000,
   "comprehensive_coverage_deductible": 500,
   "personal_accident_cover": 1500000
}
```

---

## 3. Policy Exclusions

Example:

```
EXCLUSIONS:

- Driving under influence of alcohol or drugs
- Using vehicle for commercial purposes without proper endorsement
- Racing, speed testing, or stunt driving
- Intentional damage or fraudulent claims
- Mechanical breakdown or normal wear and tear
- Personal belongings left in vehicle
- Driving without a valid driving licence
- Damage occurring outside India
- Using vehicle for taxi, delivery, or commercial services without approval
- War, nuclear risks, civil disturbance, or government seizure
```

---

## 4. Self-Check Validation

The LLM verifies the generated summary against the original policy document.

Example:

```
SELF-CHECK REPORT:

✓ Correct findings

The generated summary accurately reflects the policy details. 
All extracted coverage limits and exclusions are supported by the source policy document.

No hallucinations, incorrect coverage values, or missing major exclusions were identified.
```

The self-check step helps improve reliability by validating that generated information matches the original policy content.
