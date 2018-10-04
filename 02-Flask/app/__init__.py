# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 12:25:22 2018

@author: flemeill
"""
from flask import Flask
from config import config
from .views import app
# import pickle
import pandas as pd 


DEBUG = True

