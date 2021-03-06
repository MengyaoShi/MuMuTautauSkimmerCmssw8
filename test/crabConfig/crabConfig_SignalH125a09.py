from CRABClient.UserUtilities import config, getUsernameFromSiteDB
config = config()

config.General.requestName = 'request_SignalH125a09_Skim_all_EXO1'
config.General.workArea = 'crab_projects'
config.General.transferOutputs = True
config.General.transferLogs = True

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = '../SignalDiMuSelectionSkim.py'

config.Data.inputDataset = '/SUSYGluGluToHToAA_AToMuMu_AToTauTau_M-9_TuneCUETP8M1_13TeV_madgraph_pythia8/RunIISpring16DR80-premix_withHLT_80X_mcRun2_asymptotic_v14-v1/AODSIM'
config.Data.inputDBS = 'global'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 10
config.Data.outLFNDirBase = '/store/group/phys_higgs/HiggsExo/mshi'
config.Data.publication = True
config.Data.outputDatasetTag = 'CRAB3_SignalH125a09_skim'

config.Site.storageSite = 'T2_CH_CERN'
