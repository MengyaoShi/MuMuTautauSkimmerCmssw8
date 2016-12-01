import FWCore.ParameterSet.Config as cms
from subprocess import *
import FWCore.Utilities.FileUtils as FileUtils
mylist=FileUtils.loadListFromFile('/afs/cern.ch/work/m/mshi/private/CMSSW_8_0_17/src/GGHAA2Mu2TauAnalysis/testDYLowMass_afterskim.txt')
process = cms.Process("testOutput1")


process.load("FWCore.MessageService.MessageLogger_cfi")
process.MessageLogger.cerr.FwkReport.reportEvery = cms.untracked.int32(1000)

process.options = cms.untracked.PSet(wantSummary = cms.untracked.bool(True),
                SkipEvent = cms.untracked.vstring('ProductNotFound'))

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(-1) )
process.source = cms.Source("PoolSource", fileNames = cms.untracked.vstring(*mylist))


#require event to fire IsoMu24_eta2p1
process.MuMuTauTauRecoAnalyzer=cms.EDAnalyzer(
        'MuMuTauTauRecoAnalyzer',
          tauTag=cms.InputTag('muHadTauSelector','','SKIM'),
 jetMuonMapTag=cms.InputTag('CleanJets','muonValMap','SKIM'),
        Mu1Mu2= cms.InputTag('Isolation'),
        genParticleTag=cms.InputTag('genParticles'),
        muHadMassBins=cms.vdouble(1,2,3,4,12),
        FourBInvMassBins=cms.vdouble(0.0, 200.0,400.0,600.0, 800.0, 1000.0),
        outFileName=cms.string("muHadMassPlot.root")
)
process.Mu1Mu2Analyzer=cms.EDAnalyzer(
  'Mu1Mu2Analyzer',
  genParticleTag=cms.InputTag('genParticles'),
  Mu1Mu2=cms.InputTag('Isolation'),
  particleFlow=cms.InputTag('particleFlow'),
  Mu2PtBins=cms.vdouble(0.0,3.0, 6.0, 9.0, 12.0,15.0, 18.0, 21.0, 24.0, 27.0, 30.0, 33.0, 36.0, 39.0, 42.0, 48.0, 54.0, 60.0, 66.0, 72.0, 78.0, 84.0, 90.0, 96.0, 102.0, 108.0,116.0, 124.0, 130.0, 136.0, 142.0, 148.0, 154.0, 160.0, 166.0, 172.0, 180.0, 186.0, 192.0, 200.0 ),
  invMassBins=cms.vdouble(0.0 ,20.0,40.0,60.0, 80.0,100.0,120.0,140,160,180,200,500)

)
process.noSelectionSequence = cms.Sequence(
  process.MuMuTauTauRecoAnalyzer
)

process.TFileService = cms.Service("TFileService",
    fileName =  cms.string('tes.root')
)
process.noSelectedOutput = cms.OutputModule(
    "PoolOutputModule",
    fileName = cms.untracked.string('condensed.root'),
    SelectEvents=cms.untracked.PSet(SelectEvents = cms.vstring('p'))
    )
#no selection path
process.p = cms.Path(process.noSelectionSequence)
process.e = cms.EndPath(process.noSelectedOutput)
