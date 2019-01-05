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

## Usage
- imagehandler

    import os
    from modules.imagehandler import Separator
    
    # input file
    i = Separator(input_file='split/m001.JPG')
    # output (3 × 3)separated files.
    i.separate(3, 3,out_file=os.path.join("split", "splitted", "m_file_{:010}.png"))

## Install

## Contribution

## Licence

[MIT](https://github.com/tcnksm/tool/blob/master/LICENCE)

## Author

[mickeyjap182](https://github.com/mickeyjap182)
