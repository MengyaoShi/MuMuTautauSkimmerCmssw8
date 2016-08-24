# MuMuTauTauSkimmer
In CMSSW8

This Skimmer do basically job to skim down dataset of Drell-Yan background to what we are interested. test/DiMuSelectorSkim.py is the corresponding

python file.

Mu45Selector is the trigger I have not made it work yet, comment out that line, and you can start from here add tau-related tags.


Reciepe: 

cmsrel CMSSW_8_0_17

cd src

cmsenv

mkdir GGHAA2Mu2TauAnalysis

cd GGHAA2Mu2TauAnalysis

git clone https://github.com/MengyaoShi/MuMuTautauSkimmerCmssw8 

mv MuMuTautauSkimmerCmssw8 MuMuTauTauSkimmer

cd ..

git clone https://github.com/MengyaoShi/Tools

vim DrellYan.txt

i

copy paste this into txt

root://cms-xrd-global.cern.ch///store/mc/RunIISpring16reHLT80/DYJetsToLL_M-50_TuneCUETP8M1_13TeV-amcatnloFXFX-pythia8/AODSIM/PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v1/40000/003A70D5-E55C-E611-9B14-0025905C53A8.root

:wq


scram b

Comment out Mu45Selector in test/DiMuSelectorSkim.py And you are done! You should start from here work on tau tags.

