import json
import os
import sys
import matplotlib.pyplot as plt
import re

results_path = os.environ.get("RESULTS_PATH")

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
    acc_sum = 0
    val_loss_sum = 0
    train_loss_sum = 0

    for i, filename in enumerate(sorted(os.scandir(path_to_directory), key=lambda x: int(re.findall(r'\d+', x.name)[0]) if 'metrics_epoch_' in  x.name else -1)):

        if filename.is_file() and filename.name[-5:] == '.json' and filename.name not in ['config.json', 'metrics.json', 'meta.json']:
            with open(filename, 'r') as f:
                # print(filename)
                json_data = json.load(f)
                ######################
                # If you want new data, add it here to the list you create above

                ######################

                # if (i+1) % 1 == 0:
                #     training_loss.append(train_loss_sum)
                #     train_loss_sum = 0
                # else:
                #     train_loss_sum += json_data['training_loss']

                # if (i+1) % 1 == 0:
                #     val_loss.append(val_loss_sum)
                #     val_loss_sum = 0
                # else:
                #     val_loss_sum += json_data['validation_loss']

                training_loss.append(json_data['training_loss'])
                val_loss.append(json_data['validation_loss'])

                if (i+1) % 15 == 0:
                    val_seq_acc.append(acc_sum/15)
                    acc_sum = 0
                else:
                    acc_sum += json_data['validation_seq_acc']*100

                val_parse_valid.append(json_data['validation_parse_validity'])
                val_bleu.append(json_data['validation_BLEU']*100)

    data['training_loss'] = training_loss
    data['validation_loss'] = val_loss
    data['validation_seq_acc'] = val_seq_acc
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

    data = {}
    model_names = ['bert_base', 'bert_large', 'elmo', 'glove', 'gpt2_base','gpt2_large','seq2seq']

    for model_name in model_names:
        path_to_dir = f"{results_path}/{model_name}"
        data[model_name] = get_data_from_json(path_to_dir)

    #Plot training loss
    figs, axs = plt.subplots(1, 1)

    SMALL_SIZE = 12
    MEDIUM_SIZE = 16
    BIGGER_SIZE = 18

    plt.rc('font', size=SMALL_SIZE)           # controls default text sizes

    plt.rc('axes', titlesize=MEDIUM_SIZE)     # fontsize of the axes title
    plt.rc('axes', labelsize=BIGGER_SIZE)     # fontsize of the x and y labels
    
    plt.rc('xtick', labelsize=MEDIUM_SIZE)    # fontsize of the tick labels
    plt.rc('ytick', labelsize=MEDIUM_SIZE)    # fontsize of the tick labels
    plt.rc('legend', fontsize=SMALL_SIZE)     # legend fontsize
    plt.rc('figure', titlesize=BIGGER_SIZE)   # fontsize of the figure title

    axs.set_title('Gen. Para. Trained - Validation Loss')
    axs.set_xlabel('epochs')
    
    for model_name in model_names:
        axs.plot(data[model_name]['validation_loss'][:], label = model_name)

    # axs.set_title('Training Loss')
    # axs.set_xlabel('epochs')
    
    # for model_name in model_names:
    #     axs.plot(data[model_name]['training_loss'][:], label = model_name)

    # axs.set_title('Validation Loss')
    # axs.set_xlabel('epochs')
    
    # for model_name in model_names:
    #     axs.plot(data[model_name]['validation_loss'][:], label = model_name)

    # axs.set_title('Validation Accuracy')
    # axs.set_xlabel('every tick is 15 epochs')
    
    # for model_name in model_names:
    #     axs.plot(data[model_name]['validation_seq_acc'][:], label = model_name)
        
    plt.legend()
    plt.show()
    