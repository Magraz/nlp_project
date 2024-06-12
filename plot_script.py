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

def get_data_from_json(path_to_directory):
    data = {}
    training_loss = []
    val_loss = []
    val_seq_acc = []
    val_parse_valid = []
    val_bleu = []
    ################################
    # Add new list here
    

    ################################
    for filename in sorted(os.scandir(path_to_directory), key=lambda x: int(re.findall(r'\d+', x.name)[0]) if 'metrics_epoch_' in  x.name else -1):

        if filename.is_file() and filename.name[-5:] == '.json' and filename.name not in ['config.json', 'metrics.json', 'meta.json']:
            with open(filename, 'r') as f:
                # print(filename)
                json_data = json.load(f)
                ######################
                # If you want new data, add it here to the list you create above

                ######################
                training_loss.append(json_data['training_loss'])
                val_loss.append(json_data['validation_loss'])
                val_seq_acc.append(json_data['validation_seq_acc'])
                val_parse_valid.append(json_data['validation_parse_validity'])
                val_bleu.append(json_data['validation_BLEU'])

    data['training_loss'] = training_loss
    data['val_loss'] = val_loss
    data['val_seq_acc'] = val_seq_acc
    # data['val_parse_valid'] = val_parse_valid
    data['validation_BLEU'] = val_bleu
    #################################
    # Add you list to the data dictionary
    #################################

    return data

def get_graphs(data):
    num_graphs = len(data)
    rows = num_graphs // 2
    cols = num_graphs - rows
    figs, axs = plt.subplots(rows, cols)

    keys = list(data.keys())
    ctr = 0
    l = 0

    figs.suptitle("BERT Metrics")

    for i in range(rows):

        for j in range(cols):
            axs[i, j].plot(data[keys[ctr + j]])
            axs[i,j].set_title(plot_titles[keys[ctr + j]])
            axs[i,j].set_xlabel('epochs')
            l += 1
            if l > len(data):
                break
        ctr += cols
        l += 1

        if l > len(data):
            break
    plt.show()

if __name__ == '__main__':
    # path_to_dir = sys.argv[1]
    # path_to_dir = '/home/nboehme/Music/json_tests'

    # path_to_dir = '/home/nboehme/Downloads/metrics_epoch'

    model_names = ['bert_base_seq2seq', 'bert_large_seq2seq', 'elmo_seq2seq', 'glove_seq2seq', 'seq2seq']
    data = {}
    for model_name in model_names:
        path_to_dir = f"/home/magraz/nlp_project/results/{model_name}"
        data[model_name] = get_data_from_json(path_to_dir)

    #Plot training loss
    figs, axs = plt.subplots(1, 1)

    axs.set_title('Training Loss')
    axs.set_xlabel('epochs')
    
    for model_name in model_names:
        axs.plot(data[model_name]['training_loss'][:], label = model_name)
        
    plt.legend()
    plt.show()


    # get_graphs(data)
    