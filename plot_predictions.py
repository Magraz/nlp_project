import json
import os
import sys
import matplotlib.pyplot as plt
import re

'''
If you want to plot different stuff, add a new list to get_data_from_json and append the data to it

'''

plot_titles = {"training_loss": "Training Loss", 
               "val_loss": "Validation Loss", 
               "validation_BLEU": "Validation BLEU", 
               "val_seq_acc": "Validation Accuracy",}

def get_data_from_json(filename):
    loss = []
    
    with open(filename, 'r') as f:
        json_data = json.load(f)

        for prediction in json_data:
            loss.append(prediction['loss'])

    return loss

if __name__ == '__main__':
    model_names = ['bert_base_prediction', 'bert_large_prediction', 'elmo_prediction', 'glove_prediction', 'seq2seq', "gpt2"]
    # model_names = ['bert_base_prediction']
    data = {}
    for model_name in model_names:
        file_path = f"/home/magraz/nlp_project/predictions/{model_name}.json"
        data[model_name] = get_data_from_json(file_path)

    #Plot training loss
    figs, axs = plt.subplots(1, 1)

    axs.set_title('Prediction Loss')
    
    for model_name in model_names:
        axs.bar(x=model_name,height=sum(data[model_name]), label = model_name)
        
    plt.legend()
    plt.show()

    