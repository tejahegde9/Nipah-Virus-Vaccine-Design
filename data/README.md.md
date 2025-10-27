# 📁 Data Folder

This folder contains input data used for the computational vaccine design project.

## Subfolders
- **fasta_sequences/** → Protein sequences retrieved from UniProt for the three Nipah virus proteins:
  - Fusion glycoprotein
  - Glycoprotein G
  - RNA-dependent RNA polymerase (L)
  
- **epitopes/** → Predicted CTL (MHC Class I) and HTL (MHC Class II) epitopes for each protein, exported as CSV files.

Each CSV file contains:
- Epitope sequence  
- Start and end positions  
- Antigenicity, allergenicity, and toxicity scores  
- Binding allele information
