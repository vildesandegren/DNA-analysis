# DNA-analysis
This is a small project inteded for me to learn how to share my projects on GitHub. 

## What the program does
- Reads a DNA sequence from a file (supports FASTA format)
- Counts each base (A, T, C, G)
- Calculates the percentage of each base
- Computes GC content
- Displays results in the terminal and as a bar chart


## How to run the program 
1. Make sure you have Python and matplotlib installed:

```bash
pip matplotlib install
```

2. Add DNA-sequence in a text file. You may use "example_sequence.txt". 

3. Run the script:

```bash 
python3 DNA_analysis.py
```

4. When prompted, input the name of the input file. 


##Example output:
Input file:sequence_fasta.txt
Total bases: 148
A: 15 (10.1%)
T: 7 (4.7%)
C: 0 (0.0%)
G: 7 (4.7%)
G-C content: 4.7%

And a pop-up window will display a bar chart of base frequencies:


# What I learned
- How to use matplotlib for data visualization
- How to organize a project and share it on GitHub

## Future ideas
- Support multiple sequences in one file
- Save the chart as an image file
- Add support for RNA or protein sequences
- Use Biopython for FASTA handling