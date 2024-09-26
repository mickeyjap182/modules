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
- ginza 
- ja_ginza

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

## Install
- install Anaconda or Miniconda.
`conda update conda` 
- change chanels
```
 conda config --append channels conda-forge 
 conda config --append channels pytorch
 conda config --remove channels defaults
 conda config --get channels
```
- This python version is `3.12` 
- make install pip libraries using Anaconda from `environment.lock.yml` .
`conda env create -f=environment.lock.yml`

- or use pip with conda.
`conda env create -f=environment_pip_win.yml`

- or other tool.
`pip install -r requirements_win.txt`

- if you update libries to use and export.
`conda env export > environment.lock.yml`
- if you update libries to use and export.
`pip freeze > requirements_win.txt`
 
- remove environment
```
conda env remove -n=mod_v2
```
- install log.(WIP)
```
conda install -c conda-forge opencv -y
conda install conda-forge::matplotlib -y
pip install -U ginza ja_ginza

Preparing transaction: done
Verifying transaction: done
Executing transaction: done
Installing pip dependencies: \ Ran pip subprocess with arguments:
['C:\\Users\\yoshi\\anaconda3\\envs\\mod_v2\\python.exe', '-m', 'pip', 'install', '-U', '-r', 'C:\\workspace\\modules\\]
Pip subprocess output:
Collecting annotated-types==0.7.0 (from -r C:\workspace\modules\requirements.txt (line 1))
  Using cached annotated_types-0.7.0-py3-none-any.whl.metadata (15 kB)
Collecting blis==0.7.11 (from -r C:\workspace\modules\requirements.txt (line 2))
  Using cached blis-0.7.11-cp312-cp312-win_amd64.whl.metadata (7.6 kB)
Collecting catalogue==2.0.10 (from -r C:\workspace\modules\requirements.txt (line 3))
  Using cached catalogue-2.0.10-py3-none-any.whl.metadata (14 kB)

Pip subprocess error:
ERROR: Ignored the following yanked versions: 2022.5.18
ERROR: Could not find a version that satisfies the requirement certifi==1.1.1 (from versions: 0.0.1, 0.0.2, 0.0.3, 0.0.)
ERROR: No matching distribution found for certifi==1.1.1
 
``` 

## Contribution

## Licence

[MIT]

## Author

[mickeyjap182](https://github.com/mickeyjap182)
