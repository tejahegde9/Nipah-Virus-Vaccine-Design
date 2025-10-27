# Nipah-Virus-Vaccine-Design
Computational Design of a Multi-Epitope Vaccine Against Nipah Virus using Immunoinformatics Tools
=======
# 🧬 Nipah Virus Multi-Epitope Vaccine Design
**Author:** Teja Hegde (MSc Bioinformatics)  
**Institution:** [Garden City University]  
**Year:** 2025  

---

## 🧾 Abstract
The Nipah virus (NiV) is a zoonotic pathogen with a high fatality rate and no licensed vaccine available.  
This *in silico* project presents the **computational design and validation of a multi-epitope subunit vaccine** against NiV.  
Immunoinformatics, structural bioinformatics, and molecular dynamics tools were used to predict epitopes, design a vaccine construct, optimize it for *E. coli K12* expression, and validate its structural stability.  
The designed vaccine demonstrated strong antigenicity, non-allergenicity, high population coverage, and stable molecular interactions — suggesting its potential for experimental development.  

---

## 📖 Project Overview
This project focuses on the *in silico* design and validation of a **multi-epitope subunit vaccine** against the **Nipah virus (NiV)** using a comprehensive computational pipeline.  

The goal is to identify potent epitopes from viral proteins, construct a chimeric vaccine sequence, optimize it for *E. coli K12* expression, and validate its structural and immunological properties through bioinformatics tools and simulations.  

---

## 🧪 Methodology Workflow

```
Epitope Prediction → Vaccine Construction → Structure Prediction
        ↓                      ↓                      ↓
 MHC I, MHC II, B-cell   Population Coverage   Refinement (Galaxy)
                              Codon Optimization
                                   ↓
                     Docking → Immune Simulation → MD Simulation
```

---

## ⚙️ Tools and Servers Used

| Step | Tool / Server | Purpose |
|------|----------------|---------|
| Epitope Screening | IEDB | MHC I, MHC II, and B-cell epitope prediction |
| Population Coverage | IEDB Population Coverage Tool | Global immune response estimation |
| Vaccine Construction | Linker joining (GPGPG, AAY) + adjuvant (β-defensin) | Multi-epitope vaccine design |
| Antigenicity & Allergenicity | VaxiJen, AllerTOP | Safety and immunogenicity check |
| Secondary Structure | SOPMA | Structural composition |
| 3D Modelling | AlphaFold2 | Tertiary structure prediction |
| Structure Refinement | GalaxyRefine | Improving model quality |
| Validation | PROCHECK (Ramachandran Plot) | Model validation |
| Docking | ClusPro, PatchDock | Receptor–ligand interactions (TLR4, MHC I/II) |
| Immune Simulation | C-IMMSIM | Host immune response analysis |
| Codon Optimization | JCat / Python Script | Expression optimization in *E. coli K12* |
| Molecular Dynamics | GROMACS | Vaccine stability in physiological conditions |
| Plasmid Construction | SnapGene | Insertion into pET-28a(+) vector |

---

## 📁 Folder Structure

```
Nipah-Virus-Vaccine-Design/
│
├── data/
│   ├── epitopes/
│   ├── fasta_sequences/
│   └── population_coverage/
│
├── docs/
│   └── Nipah_Vaccine_Project_Report_Teja.pdf
│
├── results/
│   ├── structure_prediction/
│   │   ├── vaccine_construct.txt
│   │   ├── alpha_fold_result.zip
│   │   ├── galaxy_refine_structure.zip
│   │   ├── ramachandran_plot.png
│   │   └── vaccine_construct_plasmid_map.png
│   │
│   ├── docking/
│   │   ├── mhc1_docking.zip
│   │   ├── mhc2_docking.zip
│   │   └── tlr4_docking.zip
│   │
│   ├── immune_simulation/
│   │   └── c_immsim_results.pdf
│   │
│   └── md_simulation/
│       ├── gromacs_md.zip
│       ├── rmsd_plot.png
│       ├── rmsf_plot.png
│       ├── rg_plot.png
│       └── sasa_plot.png
│
└── scripts/
    ├── codon_optimization.py
    ├── gc_content_inline.py
    └── README.md
```

---

## 📊 Key Results Summary

- **Codon Adaptation Index (CAI):** 0.98 → excellent for *E. coli K12*  
- **GC Content:** ~54% → optimal for bacterial expression  
- **Vaccine length:** 3720 bases (optimized DNA)  
- **Docking:** Strong binding with TLR4, MHC-I, and MHC-II receptors  
- **Immune Simulation:** High IgG and cytokine peaks confirm strong immune response  
- **MD Simulation:** Stable RMSD and Rg indicate excellent structural stability  

---

## 💻 Technologies Used

- **Python 3.12**  
- **Bioinformatics Web Tools:** IEDB, JCat, GalaxyRefine, ClusPro, C-IMMSIM, SnapGene  
- **GROMACS (v2023)**  
- **VS Code & GitHub** for scripting and version control  

---

## 📘 How to Reproduce

1. **Clone this repository**
   ```bash
   git clone https://github.com/<your-username>/Nipah-Virus-Vaccine-Design.git
   cd Nipah-Virus-Vaccine-Design
   ```

2. **Run codon optimization**
   ```bash
   python scripts/codon_optimization.py
   ```

3. **Check GC content**
   ```bash
   python scripts/gc_content_inline.py
   ```

4. **Explore outputs**
   Results and plots are available under the `/results` directory.

---

## 🧠 Conclusion

This *in silico* study successfully designed a stable, immunogenic, and expression-ready **multi-epitope subunit vaccine** against the Nipah virus.  
The construct shows strong potential for **wet-lab validation** and **experimental expression** in *E. coli* systems.

---

## 🧾 Citation

If you use this project or its scripts, please credit:  
> **Teja Hegde, MSc Bioinformatics (2025)**  
> *Nipah Virus Multi-Epitope Vaccine Design — In Silico Analysis and Validation*

---

## ⚖️ License — MIT License

```
MIT License

Copyright (c) 2025 Teja Hegde

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the “Software”), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

