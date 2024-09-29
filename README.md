# modules
====

Overview

## Description
image libraries

## Demo

## VS.

## Requirement
require following libraries.
- opencv
- numpy
- matplotlib
- cv2

## Usage

- append module path to your system path.
 use `sys.path.append()` or
 add environment variable of `PYTHONPATH`

- imagehandler

    import os
    from modules.imagehandler import Separator
    ```
    # input file
    i = Separator(input_file='split/m001.JPG')
    # output (3 x 3)separated files.
    i.separate(3, 3,out_file=os.path.join("split", "splitted", "m_file_{:010}.png"))
    ```

## Install & initial setup
- install Anaconda or Miniconda.
`conda update conda`

- change chanels
```
 conda config --append channels conda-forge 
 conda config --remove channels defaults
 conda config --get channels
```
- This python version is `3.12` 
- make install pip libraries using Anaconda from `environment.lock.yml` .

## import an environment.
`conda env create -f=environment.lock.yml`

- or pip tool.
`pip install -r requirements_pip_win.txt`

## conda env export
### conda
- if you update libries to use and export.
`conda env export -n=mod > environment.tmp.yml`

- use convert shell
`./convertforlock.sh <input file> <output file>`
`./convertforlock.sh environment.tmp.yml environment.lock.yml`

### pip ribrary
- if you export as pip
`conda list --export > requirements.tmp.txt`

- use convert shell
`./convertforlock.sh <input file> <output file>`
`./convertforlock.sh requirements.tmp.txt requirements_pip_win.txt`

(DEPRECATED)
- if you update libries to use and export.
`pip freeze > requirements_win.txt`

## remove conda environment
- remove environment
```
conda env remove -n=mod_v2
```
## create new env 
- install library
```
conda create python=3.12 -n mod  -y
conda activate mod
python --verison
conda install conda-forge::opencv -y
conda install conda-forge::matplotlib -y
conda install conda-forge::requests -y
conda install conda-forge::pandas -y
conda install conda-forge::pytorch -y

``` 

## Contribution

## Licence

[MIT]

## Author

[mickeyjap182](https://github.com/mickeyjap182)
