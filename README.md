# AGD: Active learning based generative design for discovery of wide band gap materials
This software package implements our developed framework AGD for materials design based on active learning. This is the official Python repository. 

[Machine Learning and Evolution Laboratory](http://mleg.cse.sc.edu)<br />
Department of Computer Science and Engineering <br />
University of South Carolina <br />

How to cite:<br />


# Table of Contents
* [Introduction](#introduction)
* [Installation](#installation)
* [Dataset](#dataset)
* [Usage](#usage)



<a name="introduction"></a>
# Introduction
The package provides 3 major functions:

- Perform active-learning based sampling in whole design latent space (based on Bayesian Optimization).
- Train and evaluate the performance of a screening model (based on Roost).
- Generate material cadidates' cif files based on element substitution (based on ELMD). 

The following paper describes the details of the our framework:
[Active learning based generative design for discovery of wide band gap materials](https://arxiv.org/pdf/.pdf)



![](front-pic.png)
<a name="installation"></a>
## Installation
Install any of the relevant packages if not already installed:
* Bayesian Optimization (tested on 1.2.0)
* tensorflow (tested on 2.2.0)
* Pytorch (tested on 1.2.0) - preferably version 1.2.0 or later
* Numpy   (tested on 1.18.5)
* Pandas  (tested on 1.1.0) 
* Scikit-learn (tested on 0.21.3) 
* Pytmatgen (tested on 2020.3.13)
* PyTorch-Geometric (tested on 1.1.2)

- Bayesian Optimization, Pytorch, Numpy, Pandas, Scikit-learn, and Pymatgen
```bash
conda install -c conda-forge bayesian-optimization
pip install torch torchvision 
pip install numpy
pip install pandas
pip install scikit-learn
pip install pymatgen
```
- PyTorch Geometric (1.4.3) [documentation](https://pytorch-geometric.readthedocs.io/en/1.4.3/notes/installation.html#installation). *our codes are compatible with version up to 1.4.3*

<a name="dataset"></a>
## Dataset
1. Download the compressed file of our dataset using [this link](https://figshare.com/articles/dataset/bd_AML_whole_init_300_csv/14132270)
2. Unzip its content ( two .csv files' and 5 pre-trained models)
3. Move the csv files in your AML_Roost directory. i.e. such that the datapath now exists.

<a name="usage"></a>
## Usage
#### Generate target property material candidates
Once all the aforementionned requirements are satisfied, one can easily generate target property material candidates by running Experiment.py in the terminal along with the specification of the appropriate flags. At the bare minimum, using --budget to specify the active learning budget and --kappa to control balance between exploration and exploitation.
- Example. start active-learning process given budget and kappa.
```bash
python Experiment.py --budget 50 --kappa 100 --candidate_out_path path/you/prefer
```
The generated materials and their predicted property will be automatically generated under specified folder

#### Training a new screening model
```bash
python roost-example.py --data-path /home/glard/AML/roost/roost/examples/prepared_training_data/bd_AML_whole_train.csv --train --evaluate --test-path /home/glard/AML/roost/roost/examples/prepared_training_data/bd_AML_whole_test.csv --val-size 0.2  --epochs 200 --run-id 9
```

#### Evaluating the performance of a model trained by active-learning-augemented data
 Upon acquire active-learning augumented data, one can train and evaluate a screening model's performance using Roost package and GAN generated dataset.
 The 5 pre-trained models in figshare link are corresponding to Exp1 ~ Exp3 in the paper.
 Under roost/roost
```bash
python roost-example.py --test-path /home/glard/AML/roost/roost/examples/prepared_training_data/bandgap4new_model.csv --regression --evaluate --run-id 511
```
