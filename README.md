### Overview

This is the repository for a Python seminar that was taught to students of a few different programs at the *Fordham Graduate School of Business* in October of 2016. 

The bulk of our time was spent working through a variety of technciques for data maniuplation in *Pandas*. Our coursework was broken up over four sessions in roughly the following way:

	1) Python fundamentals
	2) Python practice & intro to Pandas
	3) Deeper into Pandas
	4) Heavier data engineering in Pandas, with some light modeling at the end
    
This code was written using Python 3.5, with Pandas as a heavy dependency. 
Much of this code will run in 2.7, but there will be some issues.

This is a work in progress that I will continue to update (more detail on that below).
    
### Repository contents

**stock_csvs/** contains 500 csv files, each with daily stock price data for one of the 500 stocks in the S&P 500, for the time period ranging Jan 1998 - August 2013. Presumably, this data corresponds to the 500 stocks in the S&P 500 as of August 9th, 2013, where this data set ends. This was a free data set obtained from https://quantquote.com/historical-stock-data.

**ppts/** contains the powerpoint presentations delivered in class. Though these presentations generally did a pretty mediocre job of predicting what would take place in subsequent classes, they did stay pretty close to whatever was covered in their respective sessions. I plan on eventually moving all of the powerpoint notes into Jupyter notebooks. 

**text_example/** contains a Jupyter notebook that walks through a practice example: searching for names in a text file using built-in Python data structures. This notebook contains detailed notes around what is being done and why - a great place to start for someone interested in learning or refreshing some Python fundamentals. 

**output/** contains output from some of the programs run. 

**code/** is where the bulk of the code lives:
	
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*stock_data.py*: functions used for aggregating the 500 csv's into a workable format
	
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*pandas_basics.ipynb*: provides a first look at DataFrames and columnar access
	
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*pandas_more.ipynb*: takes things a little further, introducing heirarchical columns
	
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*correlation_fun.ipynb*: we look at stocks whose returns were most correlated to other S&P 500 members' returns
	
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*build_table.ipynb*: we compile a daily table with derived columns

Additionally, in **code/**:
	
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*basic_examples.ipynb*: provides some very intro-to-Python style activities
	
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**additional_exercises/**: on-the-fly exercises from class, with & without solutions
	
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;*python_demo.py*: a less polished & heavily commented *stock_data*; a first look at what Python can do


### What this repository does not contain

#### Data analysis & predictive modeling 
While much of the work we were doing might full under the umbrella of *data analysis* (and to be fair I would consider the correlation exercise a useful piece of analysis), we did not get into *real* exploratory data analysis, which would include things like:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- handling missing data

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- understanding how stock price returns are distributed

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- understanding how daily stock price returns correlate to volume and intraday movement

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- understanding how daily stock price returns relate to monthly returns

I might sum up these missing analysis pieces by saying that we did a whole lot of *doing* and not a whole lot of *understanding*, which is fine given the fact that this was **a)** at heart a Python seminar and not a data analysis seminar and **b)** a very time-constrained seminar. And with that in mind, I thought it best to hold off on posting any modeling work that is not accompanied by a real exploratory analysis the data. I am working through producing these materials but at this point in time they are not quite finished. 

Additionally, while a textual overview of the relational data concepts of *joins* and *group by's* is covered in the ppts directory, I think it would be useful to have a dedicated notebook covering these topics in here. 

#### Advanced, non-Pandas Python
Our focus was the Pandas library, as it is highly relevant to the QF and GF coursework. We touched on basic Python too, as that's necessary for being able to properly use Pandas. That said, there is *a lot* of other Python functionality that we didn't cover (or at least didn't thoroughly cover), including:

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- generators

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- the *collections* library

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- the *NumPy* library

I would like to at some point in the near future provide you with at least some kind of reference for using these. 

#### Computer science
We did not really get into any computer science, so to speak - this was a look at how to get started using this language. But understanding computer science - e.g. object-oriented programming, data structures & algorithms - is phenomenally interesting, and it will make you much more proficient as a programmer, even if you are just hacking quick solutions together. If you enjoyed what we worked on I would highly recommend you take the time to investigate Python through a more computer- science-tinted lens. interactivepython.org would be a great place to start. 

Thank you again for your participation in the seminar! 





