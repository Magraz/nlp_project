#NLP_PROJECT
export SEED=0
export CUDA_DEVICE=0 #-1 for no CUDA
export EVALUATE_ON_TEST=0
export TRAIN_PATH="/home/magraz/nlp_project/gpsr-commands-dataset-master/gen/train.txt"
export VALIDATION_PATH="/home/magraz/nlp_project/gpsr-commands-dataset-master/gen/val.txt"
export PROJECT_PATH="/home/magraz/nlp_project"

export RESULTS_PATH="results/gen"
export PREDICTION_PATH="predictions/gen"

# export EVALUATE_COMMANDS_PATH="evaluations/gen/gen_eval/commands"
# export EVALUATE_LAMBDA_PATH="evaluations/gen/gen_eval/lambda"

# export TEST_COMMAND_PATH="/home/magraz/nlp_project/gpsr-commands-dataset-master/gen/test.txt"
# export TEST_LAMBDA_PATH="/home/magraz/nlp_project/gpsr-commands-dataset-master/gen_logical/test.txt"

export EVALUATE_COMMANDS_PATH="evaluations/gen/para_eval/commands"
export EVALUATE_LAMBDA_PATH="evaluations/gen/para_eval/lambda"

export TEST_COMMAND_PATH="/home/magraz/nlp_project/gpsr-commands-dataset-master/para/test.txt"
export TEST_LAMBDA_PATH="/home/magraz/nlp_project/gpsr-commands-dataset-master/para_logical/test.txt"


