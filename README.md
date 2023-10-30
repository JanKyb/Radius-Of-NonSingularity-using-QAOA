# Radius-of-Non-singularity-using-QAOA

In this repository, the binary optimization problem of the Radius of Non-Singularity is solved using a quantum algorithm with the QAOA framework.
The Code follows along the according paper "Using quantum computers in control: interval matrix properties" [Jan Schneider, Julian Berberich 2023].
The goal is to emphasize the future use of quantum algorithms for control theory. Thereby, the addressed problems is of minor importance but represents a good itroductory example.

The repository contains two files, the final implementation for the general case of $\Delta=\delta^Te$ being an example for $rank(\Delta)=1$. The limDelta file is an implmentation of $\Delta=ee^T$, which is the focus of the derivation source nad the hardness proof of the radius of non-singularity.

For the implementation, the PennyLane toolbox is used. However, there are some tries in the Folder trying to use Qiskit. At the end, Pennylane worked better and more robust for the implementation.  

The 2dimex file shows the result of the first example simulation given in the paper. 
