# Finding Donors for CharityML Project

## Introduction

This project is part of The [Udacity](https://eu.udacity.com/) Data Scientist Nanodegree Program which is composed by:

* Term 1
    * Supervised Learning
    * Deep Learning
    * Unsupervised Learning
* Term 2
    * Write A Data Science Blog Post
    * Disaster Response Pipelines
    * Recommendation Engines
    
The goal of this project is to apply Supervised learning techniques on data collected for the U.S. census to help CharityML (a fictitious charity organization) to identify people most likely to donate to their cause. From Udacity a template code was provided in the `finding_donors.ipynb` notebook and the `visuals.py` module which is some out-of-the-box code needed for visualizations. 

## Software and libraries

This project uses Python 3.11 and the most important packages are:

- [NumPy](http://www.numpy.org/)
- [Pandas](http://pandas.pydata.org)
- [matplotlib](http://matplotlib.org/)
- [scikit-learn](http://scikit-learn.org/stable/)

## Local configuration

To setup a new local enviroment and install all dependencies you can run `.\my_scripts\Set-Up.ps1`

Alternatively to create the virtual enviroment you can run `python -m venv .venv`.

More informations in `requirements.txt`. I am providing a simplified version of the file and letting pip handle the dependencies to avoid maintenance overhead.

To create a complete requirements file you can run `pip freeze > requirements.txt` and to install all python packages in it you can run `pip install -r requirements.txt`.

## Data

Have a look at the `data` folder and its [DATA.md](data/DATA.md) file.

## Testing

You can run `.\my_scripts\Test.ps1`.

Alternatively from the project folder run `pytest`

To run a single test: `pytest .\tests\utils\test_setup.py::test_create_folders_default`

## Code styling

[PEP8](https://peps.python.org/pep-0008/) is the style guide for Python code, and it's good practice to follow it to ensure your code is readable and consistent.

To check and format my code according to PEP8 I am using:
- [pycodestyle](https://pypi.org/project/pycodestyle/): tool to check the code against PEP 8 conventions.
- [autopep8](https://pypi.org/project/autopep8/): tool to automatically format Python code according to PEP 8 standards.

You can run `.\my_scripts\FormatAndLint.ps1`.

Alternatively to run pycodestyle on all files in the project folder and create a report: `pycodestyle --statistics --count . > code_style\report.txt`

To run autopep8 on all files in the project folder: `autopep8 --recursive --in-place .`

I prefere to check and update one file at the time because the previous recursive commands affect also `.\venv\` files. For example:

`pycodestyle .\utils\config.py > .\code_style\config_report.txt`

`autopep8 --in-place .\utils\config.py`

## Running the code

The code is provided in the [Jupyter Notebook](http://ipython.org/notebook.html) _finding_donors.ipynb_. It will read the data from `DATA_FOLDER` and step by step explore the data, train 3 models and compare their performances.

You can open _finding_donors.ipynb_ and run each cell and check their results.

You can also run the command `ipython -c "%run finding_donors.ipynb"`.

To convert the notebook in HTML format run `jupyter nbconvert finding_donors.ipynb --to html`.

## Results

I have compared the results of three models:

- **Decision Trees**
- **Support Vector Machines**
- **AdaBoost**

![Results](images/results.jpg)

Becasue the dataset is pretty imbalanced to evaluate the resutls I have used **F-1 Score**. As explained wonderfully in this [post](http://www.davidsbatista.net/blog/2018/08/19/NLP_Metrics/) **Accurcay** is not indicated for imbalanced dataset.

**AdaBoost** has the best **F-1 Score** and using **GridSearchCV** I have tuned the model improving furthermore the performances

Finally I have extracted the feature importance:

![Results](images/feature_importance.png)

## List of activities

In the [TODO.md](TODO.md) file you can find the list of tasks and on going activities.

## Licensing and acknowledgements

Have a look at [LICENSE.md](LICENSE.md) and many thanks to [Udacity](https://eu.udacity.com/) for the dataset.

## Outro

I hope this repository was interesting and thank you for taking the time to check it out. On my Medium you can find a more in depth [story](https://medium.com/@simone-rigoni01/finding-donors-for-charityml-project-e0f4a59dcea0) and on my Blogspot you can find the same [post](https://simonerigoni01.blogspot.com/2024/05/ricerca-di-donatori-per-il-progetto.html) in italian. Let me know if you have any question and if you like the content that I create feel free to [buy me a coffee](https://www.buymeacoffee.com/simonerigoni).
