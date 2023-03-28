(* ::Package:: *)

BeginPackage["KerrQNM`"];


KerrQNM::usage = "Reads data from Berti et al repositories, and constructs interpolating functions. Inputs: l (orbital number), m (azimuthal number), n (overtone index: fundamental mode is n = 1). "


Begin["`Private`"];


packageDirectory = DirectoryName[FindFile["KerrQNM`"]];
SetDirectory[packageDirectory];
Run["./UnzipQNMs.py"];


FileName[l_Integer, m_Integer, n_Integer] := 
"QNMData/l"<>ToString[l]<>"/n"<>ToString[n]<>"l"<>ToString[l]<>"m"<>ToString[m]<>".dat";


KerrQNM[l_, m_, n_]:=Module[{temp, \[Omega], i\[Omega]},
temp = Import[FileName[l,m,n]];
\[Omega] = Table[{temp[[i,1]],temp[[i,2]]+ I temp[[i,3]]},{i,1,Length[temp]}];
i\[Omega]=Interpolation[\[Omega]];
i\[Omega]
];


End[];


EndPackage[];
