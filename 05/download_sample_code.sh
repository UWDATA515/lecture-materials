#!/bin/bash

# Download and run this script to download the sample code for Lecture 5.

mkdir sample
mkdir sample/run
mkdir sample/utils
curl https://raw.githubusercontent.com/UWDATA515/lecture-materials/main/05/sample/main.py -o sample/main.py
curl https://raw.githubusercontent.com/UWDATA515/lecture-materials/main/05/sample/run/runner.py -o sample/run/runner.py
curl https://raw.githubusercontent.com/UWDATA515/lecture-materials/main/05/sample/utils/histogram.py -o sample/utils/histogram.py
curl https://raw.githubusercontent.com/UWDATA515/lecture-materials/main/05/sample/utils/palindrome.py -o sample/utils/palindrome.py
