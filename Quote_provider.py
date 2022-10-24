#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 22 18:18:10 2022

@author: premkumar
"""

import joblib
import pandas as pd

def load_model():
    '''
    Load the saved model into the program
    Returns
    -------
    model : Loaded model ready for predictions.
    '''
    model = joblib.load('/Users/premkumar/Desktop/Prudential Finances Assignment/model.pkl')
    return model

def quote_reason(instance, BMI):
    '''
    Function that provide the quote and reason for the instance considered
    Parameters
    ----------
    instance : DataFrame
        features provided to the model.
    BMI : int
        BMI predicted by the model.

    Returns
    -------
    quote : str
        The quote provided based on the rules.
    reason : str
        The reason provided based on the rules.
    '''
    
    age = int(instance['Ins_Age'].values)
    
    gender = instance['Ins_Gender'].values
    
    print(age, gender)
    
    if (age >= 18 and age <= 39) and (BMI < 17.49 or BMI > 38.5):
        if gender == 'Male':
            quote = '750 USD'
        else:
            quote = '675 USD'
        reason = 'Age is between 18 to 39 and BMI is either less than 17.49 or greater than 38.5'
        
        return quote, reason
    
    elif (age >= 40 and age <= 59) and (BMI < 18.49 or BMI > 38.5):
        if gender == 'Male':
            quote = '1000 USD'
        else:
            quote = '900 USD'
        reason = 'Age is between 40 to 59 and BMI is either less than 18.49 or greater then 38.5'
        
        return quote, reason
    
    elif (age >= 60) and (BMI <= 18.49 or BMI >= 45.5):
        if gender == 'Male':
            quote = '2000 USD'
        else:
            quote = '1800 USD'
        reason = 'Age is greater than 60 and BMI is either less than 18.49 or greater than 38.5'
        
        return quote, reason
    
    else:
        if gender == 'Male':
            quote = '500 USD'
        else:
            quote = '450 USD'
        reason = 'BMI is in right range'
        
        return quote, reason
    
    

if __name__ == '__main__':
    
    print('Loading_model.........')
    model = load_model()    
    print('Model ready to provide quote')
    print('Please provide the following instruction')

    while True:
        age = input('Enter Age :')
        try:
            age = int(age)
            break
        except:
            print('Enter numerical value')
            pass
    
    while True:
        gender = input('Enter Gender :')
        gender = gender.lower()
        try:
            assert gender in ['male', 'female']
            if gender == 'male':
                gender = 'Male'
            else:
                gender = 'Female'
            break
        except:
            print('Enter either "Male" or "Female"')
            pass
    
    while True:
        height = input('Enter height in feets: ')
        try:
            height = int(height)
            break
        except:
            print('Enter numerical value')
            pass
    
    while True:
        weight = input('Enter Weight in lb: ')
        try:
            weight = int(weight)
            break
        except:
            print('Enter numerical value')
            pass
    
    instance = {'Ins_Age' : [age],
                'Ins_Gender' : [gender],
                'Ht' : [height],
                'Wt' : [weight]}
    instance = pd.DataFrame.from_dict(instance)
    
    bmi = model.predict(instance)
    
    quote, reason = quote_reason(instance, bmi)
    
    print('Quote : {}'.format(quote))
    print('Reason : {}'.format(reason))
    
    