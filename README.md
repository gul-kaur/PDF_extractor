# PDF Extractor Project

This directory contains the `PDF-Extract-Kit` project, a toolkit for extracting content from PDF documents.

## Project Location

The main project code and resources are located in the `PDF-Extract-Kit/` subfolder.

## About PDF-Extract-Kit

`PDF-Extract-Kit` is a powerful open-source toolkit designed to efficiently extract high-quality content from complex and diverse PDF documents. It integrates state-of-the-art models for tasks like:

*   Layout Detection (identifying text, tables, images, formulas)
*   Formula Detection
*   Formula Recognition (converting formula images to LaTeX)
*   OCR (extracting text)
*   Table Recognition (converting table images to structured formats)

For a full overview, see the project's own README: [`PDF-Extract-Kit/README.md`](./PDF-Extract-Kit/README.md).

## Getting Started

### 1. Navigate to the Project Directory

All commands should be run from within the `PDF-Extract-Kit` directory. Open your terminal and change to that directory:

```bash
cd PDF-Extract-Kit
```

### 2. Environment Setup

It's recommended to use a virtual environment (like conda or venv).

```bash
# Using conda
conda create -n pdf-extract-kit-1.0 python=3.10
conda activate pdf-extract-kit-1.0

# Install dependencies (GPU recommended)
pip install -r requirements.txt

# Or, for CPU-only installation
# pip install -r requirements-cpu.txt
```
*Refer to `PDF-Extract-Kit/README.md` for potential specific installation notes (e.g., for DocLayout-YOLO).*

### 3. Download Models

The pre-trained models are required to run the toolkit. Download them from:

*   **Hugging Face:** [Models (🤗Hugging Face)](https://huggingface.co/opendatalab/PDF-Extract-Kit-1.0)
*   **ModelScope:** [Models(<img src="./PDF-Extract-Kit/assets/readme/modelscope_logo.png" width="20px">ModelScope)](https://www.modelscope.cn/models/OpenDataLab/PDF-Extract-Kit-1.0)

Follow the instructions in the [Model Weights Download Tutorial](https://pdf-extract-kit.readthedocs.io/en/latest/get_started/pretrained_model.html) to place the weights correctly within the `PDF-Extract-Kit` structure.

### 4. Running Extraction Tasks

Use the Python scripts located in the `PDF-Extract-Kit/scripts/` directory to perform specific extraction tasks. Each script uses a configuration file from `PDF-Extract-Kit/configs/`.

**Example Commands (run from within the `PDF-Extract-Kit` directory):**

*   **Layout Detection:**
    ```bash
    python scripts/layout_detection.py --config=configs/layout_detection.yaml
    ```
*   **Formula Detection:**
    ```bash
    python scripts/formula_detection.py --config=configs/formula_detection.yaml
    ```
*   **OCR:**
    ```bash
    python scripts/ocr.py --config=configs/ocr.yaml
    ```
*   **Formula Recognition:**
    ```bash
    python scripts/formula_recognition.py --config=configs/formula_recognition.yaml
    ```
*   **Table Recognition:**
    ```bash
    python scripts/table_parsing.py --config configs/table_parsing.yaml
    ```

### 5. Output Location

By default, the results (visualizations, extracted data) for each task are saved within the `PDF-Extract-Kit/outputs/` directory, in subfolders named after the task (e.g., `PDF-Extract-Kit/outputs/layout_detection/`).

## Cloning (For Reference)

If you were obtaining this project for the first time, you would typically clone it using Git:

```bash
git clone https://github.com/opendatalab/PDF-Extract-Kit.git
```
This would create the `PDF-Extract-Kit` folder containing the project.

## Further Information

For more detailed information, including advanced usage, configuration options, and specific model details, please refer to the main project documentation:

*   **Project README:** [`PDF-Extract-Kit/README.md`](./PDF-Extract-Kit/README.md)
*   **Online Documentation:** [PDF-Extract-Kit Tutorial](https://pdf-extract-kit.readthedocs.io/en/latest/get_started/pretrained_model.html)
