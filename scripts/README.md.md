# 🧬 Scripts — Nipah Virus Multi-Epitope Vaccine Design

This folder contains all Python scripts developed and used during the **MSc Bioinformatics Project: Nipah Virus Multi-Epitope Vaccine Design** by **Teja Hegde**.

Each script performs a crucial role in optimizing and validating the designed vaccine construct for *E. coli K12* expression.

---

## 📁 Script Descriptions


### 1️⃣ `codon_optimization.py`
**Purpose:**  
This script performs **offline codon optimization** of the final vaccine construct.  
It reverse-translates the amino acid sequence into a DNA sequence using the **most frequent codons of *E. coli K12***.

**Features:**
- Converts the protein (amino acid) sequence to a codon-optimized DNA sequence.  
- Automatically saves the optimized sequence in **FASTA format** (`codon_optimized_vaccine.fasta`).  
- Wraps the output at 60 bases per line for readability.  

**Usage:**
```bash
python codon_optimization.py

Output Example:
>codon_optimized_vaccine_EcoliK12
GGGATCATCAACACCCTGCAGAAATACTACTGCCGTG...
Saved codon_optimized_vaccine.fasta successfully!


2️⃣ gc_content_inline.py

Purpose:

This script calculates the GC content (%) and total nucleotide length of the codon-optimized DNA sequence.
It uses the FASTA sequence directly embedded inside the script (no file paths required).

Features:

Reads codon-optimized DNA from the code itself.

Calculates total bases and GC% of the sequence.

Confirms whether the GC% is suitable for bacterial expression (ideal 30–70%).

Usage:
bash
python gc_content_inline.py

Output Example:
Sequence length: 3720 bases
GC Content: 54.12 %


🧠 Notes

Both scripts were executed using Python 3.12 in VS Code.

The GC%  and Codon Adaptation Index  confirm the construct’s suitability for expression in E. coli K12.

Together, these scripts form a Sequence Optimization & Validation Pipeline, demonstrating skills in bioinformatics scripting and data handling.


