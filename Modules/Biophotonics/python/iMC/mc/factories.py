'''
Created on Oct 15, 2015

@author: wirkert
'''

from mc.tissuemodels import AbstractTissue, GenericTissue
from mc.batches import AbstractBatch, GenericBatch, VisualizationBatch, \
    GaussianBatch, ColonMuscleBatch


class AbstractMcFactory(object):
    '''
    Monte Carlo Factory.
    Will create fitting models and batches, dependent on your task
    '''

    def create_tissue_model(self):
        return AbstractTissue()

    def create_batch_to_simulate(self):
        return AbstractBatch()

    def __init__(self):
        '''
        Constructor
        '''

class GenericMcFactory(AbstractMcFactory):

    def create_tissue_model(self):
        return GenericTissue()

    def create_batch_to_simulate(self):
        return GenericBatch()

    def __init__(self):
        '''
        Constructor
        '''

class GaussianMcFactory(GenericMcFactory):

    def create_batch_to_simulate(self):
        return GaussianBatch()

    def __init__(self):
        '''
        Constructor
        '''


class ColonMuscleMcFactory(GenericMcFactory):

    def create_batch_to_simulate(self):
        return ColonMuscleBatch()

    def __init__(self):
        '''
        Constructor
        '''

class VisualizationMcFactory(AbstractMcFactory):

    def create_tissue_model(self):
        return GenericTissue()

    def create_batch_to_simulate(self):
        return VisualizationBatch()

    def __init__(self):
        '''
        Constructor
        '''
