# ORG Board elections

Open Rights Group board elections use a modified version of the Meek single transferable vote algorithm that protects a "reopen nominations" choice from elimination.

Nominations are collected into a CSV file, converted into a BLT format file and run using OpenSTV.

## Installation

Assumes OpenSTV 1.6 is installed.

The file MeekSTVRon.py should be copied into the OpenSTV modules library. Example:

```shell
sudo cp MeekSTVRon.py /usr/share/openstv/openstv/MethodPlugins/
```

## Usage

Running the count for three available seats, first as Meek STV, then as Meek STV Ron.

```shell
cd board-2012
python ../rankconvert.py -n 3 org-board-2012.csv > org-board-2012.blt
openstv-run-election -r TextReport MeekSTV org-board-2012.blt > org-board-2012-ifstv.txt
openstv-run-election -r TextReport MeekSTVRon org-board-2012.blt > org-board-2012-result.txt
```

