import os
import sys
import os.path as osp
import argparse

sys.path.append(osp.join(os.path.dirname(os.path.abspath(__file__)), '..'))
from pdf_extract_kit.utils.config_loader import load_config, initialize_tasks_and_models
import pdf_extract_kit.tasks

TASK_NAME = 'ocr'


def parse_args():
    parser = argparse.ArgumentParser(description="Run a task with a given configuration file.")
    parser.add_argument('--config', type=str, required=True, help='Path to the configuration file.')
    return parser.parse_args()

def main(config_path):
    print("Entering main function") # Debug print: Entering main
    config = load_config(config_path)
    task_instances = initialize_tasks_and_models(config)

    # get input and output path from config
    input_data = config.get('inputs', None)
    result_path = config.get('outputs', 'outputs/ocr_output') # Modified output path for debugging
    visualize = config.get('visualize', False)

    print(f"Input path: {input_data}") # Debug print input path
    print(f"Output path: {result_path}") # Debug print output path

    # formula_detection_task
    task = task_instances[TASK_NAME]

    print("Before task.process()") # Debug print before process
    detection_results = task.process(input_data, save_dir=result_path, visualize=visualize)
    print("After task.process()") # Debug print after process

    print(f'Task done, results can be found at {result_path}')

if __name__ == "__main__":
    args = parse_args()
    main(args.config)
