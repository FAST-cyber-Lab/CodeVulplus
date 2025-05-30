# CodeVul+

CodeVul+ is a deep learning framework for code vulnerability detection at function-level granularity that leverages GCN reasoning and transformer-based models. The architecture combines GraphCodeBERT embeddings with a dynamic graph convolutional network to capture both syntactic and semantic relationships in code.

# Technical presentation of our approach. <br>


- 📂 [Presentation](https://drive.google.com/drive/folders/1LC9L8bfwItw_pFA6e_8eWtn-UYvH8pq4?usp=sharing)



# Dataset Format.<br>
CodeVul+ expects datasets in CSV format with a column named **`functionSource`** containing the code snippets to analyze. The sample dataset included in the repository **`data\sample_dataset.csv`** demonstrates the expected format. <br>
NOTE: Replace **`\root\`** in the command below with the absolute path to your working environment or project directory as appropriate for your setup.

## Installation

Clone the repository.<br>
<pre lang="markdown">git clone https://github.com/FAST-cyber-Lab/CodeVulplus.git<br> </pre>

### Create a virtual environment (recommended)
<pre lang="markdown">!python -m venv codevul_env </pre>
source codevul_env/bin/activate  <br>
On Windows: codevul_env\Scripts\activate


# Install dependencies.<br>
<pre lang="markdown">pip install -r ./CodeVulplus/requirements.txt</pre>



### Quick Start with Sample Dataset.<br>
Run both training and inference with the sample dataset.<br>
<pre lang="markdown">!python sample_run.py </pre>

### Run For Fine-tuning.<br>
<pre lang="markdown">!python sample_run.py --train </pre>

### Run only inference 
<pre lang="markdown"> python sample_run.py --infer </pre>



# Fine-tuning for Downstream Task.<br>
<pre lang="markdown">!python root/CodeVulplus/train.py --dataset root/CodeVulplus/data/sample_dataset.csv --save_path root/new_finetuned.pt --batch_size 4 --epochs 2
  </pre>

# Inference.<br>
<pre lang="markdown"> !python root/CodeVulplus/infer.py --dataset root/sample_dataset.csv --model_path root/CodeVulplus/pretrained/pretrained.pt --output infered_embeddings.csv </pre>


# Make prediction with your vectorized dataset.<br>
<pre lang="markdown"> !python root/CodeVulplus/predict.py --embeddings root/vectorized_dataset.csv --download</pre>


