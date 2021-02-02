#!/usr/bin/env python
import pandas as pd
import sys
import os
import json
import shutil
import warnings
import pickle




sys.path.insert(0, 'src')
from data.etl import scrape_item_data, scrape_review_data


def main(targets):
    '''
    Runs the main project pipeline logic, given the targets.
    targets must contain: 'data', 'features', 'model'.

    `main` runs the targets in order of data=>features=>model.
    '''


    with open('config/data-params.json') as fh:
        data_cfg = json.load(fh)
        outdir = data_cfg['outputdir']
        chrome_path = data_cfg['chromeexecdir']

    # run all targets
    if 'all' in targets:
        targets = ['data', 'features', 'model', 'accuracy']

    if 'test' in targets:
        targets += ['features', 'model', 'accuracy']
        with open('config/test-params.json') as fh:
            data_cfg = json.load(fh)['testdir']





    # Scrape data from Sephora.com.
    if 'item_data' in targets:
        scrape_item_data(outdir, chrome_path, "./data/cosmetic_url.csv")

    if 'review_data' in targets:
        scrape_review_data(outdir, chrome_path, "./data/cosmetic_url.csv")





    # create and save the features
    if 'features' in targets:

        pass


    # load the model using the saved features.
    if 'model' in targets:
        pass

    # Get accuracy of the model
    if 'accuracy' in targets:
        pass





    return


if __name__ == '__main__':
    # run via:
    # python main.py data features model
    targets = sys.argv[1:]
    main(targets)
