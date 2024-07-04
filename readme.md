# Quantum Oracles

In this repo, all the stuff related to my first scientific research is stored. In here, you'll find presentations, other documents, code, tests, results images and the paper as well.

The paper itself, is going to be polished and published in some magazine later, probably to [arxiv](https://arxiv.org/). If you want to see how's it going, you can read the pdf version [here](./latex/paper.pdf).

## The idea

This research was a way I found to understand better about quantum computing, more especfically quantum oracles, how a scientific research works and how a paper publishing process works.

In this reasearch, I did 5 mini-projects to test some quantum computing capabilities using quantum oracles. The main goal, was to understand better about the oracles and how them could be used to translate some classical problems to quantum ones, comparing the results with its classical counterparts.

These mini-projects were:

- Quantum File Explorer
- Miles to Km conversion
- Buckshot Roulette
- QRAM
- Hanoi Tower

The code for them you can find at: [/code](./code).


## Running the code

Case you want to test the code by yourself, I may need to have previously installed:

- [conda](https://www.anaconda.com/)
- [python](https://www.python.org/)

then get your Quantum IBM token and do:

```bash
#on linux
echo "IBM_TOKEN=your-ibm-token" >> .env
```

after that, run:

```bash
conda deactivate
conda env create -f environment.yml
conda activate quantum-oracles
```

If you prefer, you can install all the dependencies without conda, but's not the recommended here. However, you can do that using the [requirements.txt file](./requirements.txt), remember to create a virtual environment using other tools before.

```bash
# installing dependecies without conda
pip install -r requirements.txt
```

Finally, you can start your jupyter server and play around with the code by doing:

```bash
jupyter lab
```