# -*- coding:utf-8 -*-
__author__ = 'yangjian'
"""

"""
from hypernets.experiment import CompeteExperiment
from .hyper_gbm import HyperGBM, HyperGBMEstimator, HyperGBMExplainer, HyperEstimator, HyperModel
from .experiment import make_experiment

from ._version import __version__


def _init():
    from hypernets.utils import logging, isnotebook
    if isnotebook():
        logging.set_level('warn')


_init()
