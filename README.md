**The assignment is not yet released for the Spring 2021 and might be subject to change.**

# Assignment 1 - Forcefield Isolation

This assignment will cover some of the concepts discussed in the Adversarial Search lectures. You will be implementing game playing agents for a variant of the game Isolation.

We are also implementing this through Jupyter Notebook, so you all may find it useful to spend some time getting familiar with this software. During the first week of classes, there was an assignment [Assignment 0](https://github.gatech.edu/omscs6601/assignment_0/) that spends some time going through Python and Jupyter. If you are unfamiliar with either Python or Jupyter, please go through that assignment first!

### Table of Contents
- [Get repository](#repo)
- [Setup](#setup)
- [Jupyter](#jupyter)
- [Jupyter Tips](#jupyter-tips)
- [FAQ](#faq)
- [IDE](#IDE)

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

In case you used a different environment name, to list of all environments you have on your machine you can run `conda env list`.

<a name="jupyter"/></a>
## Jupyter

Further instructions are provided in the `notebook.ipynb`. Run:

```
jupyter notebook
```

Once started you can access [http://localhost:8888](http://localhost:8888/) in your browser.

<a name="jupyter-tips"/></a>
## Jupyter Tips

Hopefully, [Assignment 0](https://github.gatech.edu/omscs6601/assignment_0/) got you pretty comfortable with Jupyter or at the very least addressed the major things that you may run into during this project. That said, Jupyter can take some getting used to, so here is a compilation of some things to watch out for specifically when it comes to Jupyter in a sort-of FAQs-like style

**1. My Jupyter notebook does not seem to be starting up or my kernel is not starting correctly.**<br />
Ans: This probably has to do with activating virtual environments. If you followed the setup instructions exactly, then you should activate your conda environment using `conda activate <environment_name>` from the Anaconda Prompt and start Jupyter Notebook from there.

**2. I was running cell xxx when I opened up my notebook again and something or the other seems to have broken.**<br />
Ans: This is one thing that is very different between IDEs like PyCharm and Jupyter Notebook. In Jupyter, every time you open a notebook, you should run all the cells that a cell depends on before running that cell. This goes for cells that are out of order too (if cell 5 depends on values set in cell 4 and 6, you need to run 4 and 6 before 5). Using the "Run All" command and its variants (found in the "Cell" dropdown menu above) should help you when you're in a situation like this.

**3. The value of a variable in one of my cells is not what I expected it to be? What could have happened?** <br />
Ans: You may have run a cell that modifies that variable too many times. Look at the "counter" example in assignment 0. First, try running `counter = 0` and then `counter += 1`. This way, when you print counter, you get counter = 1, right? Now try running `counter += 1` again, and now when you try to print the variable, you see a value of 2. This is similar to the issue from Question 2. The order in which you run the cells does affect the entire program, so be careful.

<a name="faq"/></a>
## FAQ
**1. I'm not beating 1a with minimax implemented. What's up?**<br />
Ans: To confidently beat 1a, you should have a correct implementation of minimax along with timeout handling to a depth of 3. The timeout limit on every section on Gradescope is 1 second.

**2. What depth does the server call my search algorithms with?**<br />
Ans: The server will not pass a depth value to your CustomPlayer; whatever you set as the default parameter value will be used on Gradescope. Modifying this default value is extremely important in changing the performance of your agent.

**3. How do I handle timeouts?**<br />
Ans: The time_left parameter passed to you in your functions is a method that, when called using time_left(), tells you how many milliseconds you have to make your move. When this function returns a value near zero, you should change the behavior of your algorithm to stop progressing in the search.

**4. How does Gradescope set up and run each game?**<br />
Ans: Gradescope will run 20 games in order to determine the win ratio. Your player (CustomPlayer) will be Q1 for 10 of those games and Q2 for 10 of those games. Each player has 1 second to make each move and the first two moves (i.e. each player's starting location) will be randomized.

**5. I'm not beating the minimax bot in part 1b with my alpha-beta agent. What's up?**<br />
Ans: To confidently beat the minimax bot, you should have a correct implementation of alpha-beta, handle timeouts, and search to a depth of 4 or more. Additionally, your agent  may want to have a 'killer move' functionality and further optimizations as mentioned in the lectures and described in the textbook.

**6. I'm not beating the alphabeta bot in part 1b with my agent. What's up?**<br />
Ans: To confidently beat the alphabeta bot, you should have a correct implementation of iterative deepening along with the agent described in the previous bulletpoint. The timeout handling of iterative deepening should be sure to use the last completed search and not the last incomplete search. That is, if you experience a timeout when searching to depth D, you should recognize this and return the result of your search at depth D - 1.

**7. I've implemented every optimization I can think of and haven't passed 1b. Why is this so hard?**<br />
Ans: Adding any more optimizations than required adds a substantial amount of complexity to your code, and makes it much harder to debug. Implementing node ordering, iterative deepening, and writing your own CustomEvalFn to beat the minimax player creates three more possible points of failure when you should only have one: alphabeta. Stripping down your agent to the required optimizations for your current section will help you focus on what's important. This testing method is important in all sections of this assignment; not just 1b.

**8. Can we use multithreading of multiprocessing?**<br />
Ans: Sorry, we will not allow multithreading or multiprocessing on this Assignment. It isn't necessary to successfully complete the Assignment.

**9. I'm not getting any points on 1c. How do I proceed?**<br />
Ans: With the agent described in the previous bullet point, you should be getting ~50% winrate against the iterative deepening bot. To increas

**10. I have a question about the isolation API or the workings of the framework. Where should I learn more?**<br />
Ans: Firstly, watch the recorded YouTube live stream of assignment 1 where isolation API is covered. If this video and the docstrings inside isolation.py leave you with more questions, feel free to post a question on Piazza and a TA will respond as soon as possible with clarifications.

<a name="IDE"/></a>
## IDE 

In case you are willing to use IDE (e.g. Pycharm) to implement your assignment in `.py` file. Please run:

```bash
python helpers/notebook2script.py submission
```

You will get autogenerated `submission/submission.py` file where you can write your code. However, make sure you have gone through the instructions in the `notebook.ipynb` at least once.
