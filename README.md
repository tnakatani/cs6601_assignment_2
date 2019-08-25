# Assignment 1 - Swap Isolation

This assignment will cover some of the concepts discussed in the Adversarial Search lectures. You will be implementing game playing agents for a variant of the game Isolation.

We are also implementing this through Jupyter Notebook, so you all may find it useful to spend some time getting familiar with this software. During the first week of classes, there was an assignment [Assignment 0](https://github.gatech.edu/omscs6601/assignment_0/) that spends some time going through Python and Jupyter. If you are unfamiliar with either Python or Jupyter, please go through that assignment first!

### Table of Contents
- [Get repository](#repo)
- [Setup](#setup)
- [Environment](#env)
- [Packages](#pkg)
- [Jupyter](#jupyter)
- [Summary](#summary)

<a name="repo"/></a>
## Get repository

Pull this repository to your local machine:

```
git clone https://github.gatech.edu/omscs6601/assignment_1.git
```

<a name="setup"/></a>
## Setup

Activate the environment:
```
conda activate ai_env
```

In case you use a different name, to list of all environments you have on your machine you can run `conda env list`.

Install additional package that will be used to for visualising the game board.

```
pip install ipywidgets==7.5.0
```

<a name="jupyter"/></a>
## Jupyter

Further instructions are provided in the `notebook.ipynb`. Run:

```
jupyter notebook
```

Once started you can access [http://localhost:8888](http://localhost:8888/) in your browser.

## Jupyter Tips

Hopefully, [Assignment 0](https://github.gatech.edu/omscs6601/assignment_0/) got you pretty comfortable with Jupyter or at the very least addressed the major things that you may run into during this project. That said, Jupyter can take some getting used to, so here is a compilation of some things to watch out for specifically when it comes to Jupyter in a sort-of FAQs-like style

**1. My Jupyter notebook does not seem to be starting up or my kernel is not starting correctly.**<br />
Ans: This probably has to do with activating virtual environments. If you followed the setup instructions exactly, then you should activate your conda environment using `conda activate <environment_name>` from the Anaconda Prompt and start Jupyter Notebook from there.

**2. I was running cell xxx when I opened up my notebook again and something or the other seems to have broken.**<br />
Ans: This is one thing that is very different between IDEs like PyCharm and Jupyter Notebook. In Jupyter, every time you open a notebook, you should run all the cells that a cell depends on before running that cell. This goes for cells that are out of order too (if cell 5 depends on values set in cell 4 and 6, you need to run 4 and 6 before 5). Using the "Run All" command and its variants (found in the "Cell" dropdown menu above) should help you when you're in a situation like this.

**3. The value of a variable in one of my cells is not what I expected it to be? What could have happened?** <br />
Ans: You may have run a cell that modifies that variable too many times. Look at the "counter" example in assignment 0. First, try running `counter = 0` and then `counter += 1`. This way, when you print counter, you get counter = 1, right? Now try running `counter += 1` again, and now when you try to print the variable, you see a value of 2. This is similar to the issue from Question 2. The order in which you run the cells does affect the entire program, so be careful.

## IDE 

In case you are willing to use IDE (e.g. Pycharm) to implement your assignment in `.py` file. Please run:

```bash
python helpers/notebook2script.py
```

You will get autogenerated `submission.py` file where you can write your code. However, make sure you have went through the instructions in the `notebook.ipynb` at least once.