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
[Active learning based generative design for discovery of wide band gap materials](https://arxiv.org/pdf/2003.13379blablabla.pdf)



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
1. Download the compressed file of our dataset using [this link](https://widgets.figshare.com/articles/12522524/embed?show_title=1)
2. Unzip its content ( a directory named 'DATA')
3. Move the DATA directory in your GATGNN directory. i.e. such that the path GATGNN/DATA now exists.

<a name="usage"></a>
## Usage
#### Training a new model
Once all the aforementionned requirements are satisfied, one can easily generate target property material candidates by running Experiment.py in the terminal along with the specification of the appropriate flags. At the bare minimum, using --budget to specify the active learning budget and --kappa to control balance between exploration and exploitation.
- Example. Train a model on the bulk-modulus property using the CGCNN dataset.
```bash
python Experiment.py --budget 50 --kappa 100 --candidate_out_path path/you/prefer
```

The generated materials and their predicted property will be automatically generated under specified folder

#### Evaluating the performance of a trained model
Upon training a GATGNN, one can evaluate its performance using __evaluate.py__ in the terminal exactly the same way as __train.py__. *It is IMPORTANT that one runs __evaluate.py__ with the exact same flags as it was done when prior training the model.*
- Example-1. Evaluate the performance of a model trained on the bulk-modulus property using the CGCNN dataset.
```bash
python evaluate.py --property bulk-modulus --data_src CGCNN
```
- Example-2. Evaluate the performance of a model trained on the shear-modulus property using the MEGNET dataset.
```bash
python evaluate.py --property shear-modulus --data_src MEGNET
```
- Example-3.  Evaluate the performance of a model trained with 5 layers on the bulk-modulus property using the CGCNN dataset and the global attention technique of fixed cluster unpooling (GI M-2).
```bash
python evaluate.py --property bulk-modulus --data_src CGCNN --num_layers 5 --global_attention cluster --cluster_option fixed
```
