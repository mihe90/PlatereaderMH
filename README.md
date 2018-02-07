# PlatereaderMH

A small python script to convert exported .txt file from the SpectraMax M5 platereader to tidy .xlsx files.

## Instructions
### Requirements
* Python 3.x (Tested on macOS)
* numpy, pandas, openpyxl (for xlsx-output)

### Installation
The package is installed using pip. Open terminal and type:
```
pip install PlatereaderMH
```
Required packages should be loaded automatically.
### Usage:
Open terminal and type:
```
platereader.py <path to .txt file>
```
Optionally, a platelayout.xlsx file can be used to declare wells of the 96-well plate in advance (See sample/sample_platelayout.xlsx).  
```
platereader.py <path to .txt file> <path to .xlsx file>
```
