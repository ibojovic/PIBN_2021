# Structural analysis of the Hemoglobin complex

## Data
* All the entries for crystal structures of human  hemoglobin were extracted from the PDB file 1GZX  downloaded from Protein Data Bank.
* The coordinates for different  record types were provided by Introduction to Protein Data Bank Format.
* For Relative solvent accessibility data from AAindex database was used (Residue accessible surface are in tripeptide)

##
* Protein-protein interactions were extracted from IntAct database. 
* DSSP program were used for understanding the total amount of surface that are  shared between pairs of monomers by generating dssp file of complex and all possible trimers.
* Python  package NetworkX was used for creation and study of the structure and dynamics of hemoglobin’s networks 

## Procedure
* The procedure is composed in three parts. 
### Part 1: Residue Identification and Distance Calculation
* Identified residues near the heme and oxygen groups, discarding those over 3.5 Å distance.
* Removed irrelevant water atoms from the analysis.
* Created functions to:
   - Calculate minimum distances with a set threshold.
   - Determine positions of oxygen and heme groups.
   - Compute distances between all possible positions, heme, and oxygen groups.
* Identified potential interacting residues between monomers by locating salt bridges and hydrogen bonds.

### Part 2: Surface Interaction Study
* Analyzed the interaction surface between monomers in a tetramer.
* Determined solvent accessibility for each monomer and generated corresponding DSSP files.
* Calculated the interaction surface:
   - Compared the accessible surface area of monomers in tetramers with those in trimers.
   - Normalized accessibility based on the maximum relative solvent accessibility per residue.
* Adjusted accessibility ratios at N and C terminals to a maximum of 1 to prevent overestimation.

### Part 3: Protein-Protein Interaction Analysis
* Focused on direct interactions between α and β hemoglobin subunits.
* Gathered interaction data from the IntAct database using the human taxid 9606.
* Replaced all isoforms with reference proteins, using Uniprot IDs P69905 for subunit α and P68871 for subunit β.
* Network analysis:
  - Utilized NetworkX to identify subnetworks.
  - Checked for major components containing α and β subunits.
  - Calculated the degree, clustering, and betweenness centrality for hemoglobin subunits.
  - Examined the network's structure after removing nodes corresponding to α and β subunits and recalculated betweenness.
