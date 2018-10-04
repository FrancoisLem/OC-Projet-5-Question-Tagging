# -*- coding: utf-8 -*-
"""
Created on Tue Jun 12 14:33:30 2018

@author: flemeill
"""

from flask import Flask, render_template, url_for, request, redirect
from config import config

app = Flask(__name__)

app.config.from_object(config)


from .models import get_tags, nettoyage 
from app.form import QuestionForm
# import pickle
import numpy as np
import pandas as pd 

@app.route('/')
@app.route('/form/')
def form():
    form = QuestionForm()
    if form.validate_on_submit() is True:
        print('form validée avec submit')
        print
        return redirect(url_for('/result/'))
    else: 
        print("le formulaire n'a pas encore été envoyé")

    return render_template('form.html', form=form)


@app.route('/result/' , methods = ['GET', 'POST'])
def result():
    if request.method=='POST':

        result = request.form
        titre_brut = result['titre']
        question_brut = result['question']
        
        texte = titre_brut + question_brut
        
        question = nettoyage(texte)
        tags = get_tags(question)
        
        
        return render_template('result.html', question = question_brut, tags = tags)
        
    else: 
        return print('Erreur sur Méthode POST')

    

@app.route('/about/' , methods = ['GET', 'POST'])
def about():
    return render_template('about.html')

@app.route('/erreur/' , methods = ['GET', 'POST'])
def erreur():
    return render_template('erreur.html')