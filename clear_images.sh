#!/bin/bash

exiftool -all=* ./images/ && rm -rf ./images/*_original
exiftool -all=* ./code/assets/ && rm -rf ./code/assets/*_original
exiftool -all=* ./latex/ && rm -rf ./latex/*_original
