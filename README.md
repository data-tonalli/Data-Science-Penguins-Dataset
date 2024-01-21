# Data-Science-Penguins-Dataset
The goal of this this reposotory is to store code for my data science blog using the penguins data set by Allison Horst.

## Installation
- create conda env with Python 3.9.0
```bash
>> conda create -n blog python=3.9.0
```
- activate your env
```bash
>> conda activate blog
```
- install packages
```bash
>>  conda install --file requirements.txt
```
- add your env to the list of kernesl for jupyter
```bash
>> conda install ipykernel
>> python -m ipykernel install --user --name blog --display-name "Python Blog" 
```

- install and lauch jupyter lab
```bash
>> conda install -c conda-forge jupyterlab
>> jupyter lab
```

## Contents

1. [Probabilistc Graphical Models](https://github.com/JCardenasRdz/Data-Science-Penguins-Dataset/tree/main/1-Probabilistc%20Graphical%20Models)


##  Penguins Data SetReferences

**Data originally published in:**

  - Gorman KB, Williams TD, Fraser WR (2014). Ecological sexual
    dimorphism and environmental variability within a community of
    Antarctic penguins (genus *Pygoscelis*). PLoS ONE 9(3):e90081.
    <https://doi.org/10.1371/journal.pone.0090081>

**Original repo:**
- https://github.com/allisonhorst/palmerpenguins

