#!/usr/bin/env python 

import ROOT 

input_file = '../data/events.root'

ROOT.gROOT.LoadMacro('EventTree.h')

root_file = ROOT.TFile.Open(input_file)
