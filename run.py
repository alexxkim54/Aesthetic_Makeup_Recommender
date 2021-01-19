#!/usr/bin/env python
import pandas as pd
import sys
import os
import json
import shutil
import pandas as pd
import warnings
import pickle


sys.path.insert(0, 'src')


def main(targets):
    '''
    Runs the main project pipeline logic, given the targets.
    targets must contain: 'data', 'analysis', 'model'. 
    
    `main` runs the targets in order of data=>analysis=>model.
    '''
    
    
    # with open('config/data-params.json') as fh:
    #     data_cfg = json.load(fh)['outdir']
        
    # run all targets    
    if 'all' in targets:
        targets = ['data', 'features', 'model', 'accuracy']
        
    if 'test' in targets:
        targets += ['features', 'model', 'accuracy']
        with open('config/test-params.json') as fh:
            data_cfg = json.load(fh)['testdir']



    
    
    # Scrape data from Sephora.com. 
    if 'data' in targets:
        
        

   
        
    # create and save the features
    # if 'features' in targets:            
        
    
    # load the model using the saved features.
    # if 'model' in targets:

    
    # Get accuracy of the model
    # if 'accuracy' in targets:
        
        
    


    return


if __name__ == '__main__':
    # run via:
    # python main.py data features model
    targets = sys.argv[1:]
    main(targets)