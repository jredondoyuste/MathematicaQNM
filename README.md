# MathematicaQNM
Interpolate the QNM frequencies for Kerr BHs from the pre-computed data from Berti et al for a ready-to-use Mathematica implementation, which I found lacking in the BHPT. 

Please, file an Issue or a Pull Request if you find any Bug or want to help with the development.

# Requirements

+ A Mathematica installation
+ Any Python basic set-up (only tested with 3.10). 

# Installation

1.-Clone the repository and place it in any directory within Mathematica's $Path (if you don't know which are those, you can run ``Echo[$Path]``. 
2.-Copy or move the file "KerrQNMs.wl" to the same level as the repository. Example:

----/Users/MyName/Library/Mathematica/Applications/---MathematicaQNM/Example.nb
                                                                     ...
                                                   ---KerrQNMs.wl
                                                   
# Usage

Load the module in any Notebook by calling ``<<KerrQNMs` ``
Then, the main function that the module provides is ``KerrQNM[l, m, n]``. 

+ l = Angular number (Positive Integer or zero)
+ m = Azimuthal number (Integer between -l and l)
+ n = Overtone index (Integer, fundamental mode is n = 1). 

See Example.nb for an example usage. 
