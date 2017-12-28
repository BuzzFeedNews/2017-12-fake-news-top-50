# Analysis of fake news sites and viral posts, 2016 vs. 2017

This repository contains data and analysis supporting the BuzzFeed News article, "[These Are 50 Of The Biggest Fake News Hits On Facebook In 2017](https://www.buzzfeed.com/craigsilverman/these-are-50-of-the-biggest-fake-news-hits-on-facebook-in)", published Thursday, December 28, 2017. Please read that article, which contains important context and methodological details, before proceeding.

## Data

The data in this repository was compiled by BuzzFeed News using [BuzzSumo](https://buzzsumo.com/), our own data collection, and [this PolitiFact list](http://www.politifact.com/punditfact/article/2017/apr/20/politifacts-guide-fake-news-websites-and-what-they/). For additional details, please see the main BuzzFeed News article referenced above.

- `fact_check.csv`: Titles and URLs of the top 50 fake news articles of 2017 along with associated fact-checking articles and their engagement numbers
- `sites_2016.csv`: All URLs in our 2016 collection of sites that regularly publish completely fabricated articles
- `sites_2017.csv`: All URLs in our 2017 collection of sites that regularly publish completely fabricated articles
- `top_2016.csv`: The top 50 fake news articles of 2016 (by Facebook engagement) published by our 2016 list of fake news sites
- `top_2017.csv`: The top 50 fake news articles of 2017 (by Facebook engagement) published by our 2017 list of fake news sites

## Analysis

The analysis is contained within [this notebook](notebooks/fake-news-analysis.ipynb). The Python code in that notebook  also produces one output file. This file, [`output/top_domains_comparison.csv`](output/top_domains_comparison.csv), compares the count of unique domains from the list of top 50 fake news articles in 2016 with the equivalent list from 2017.

## Reproducibility

To reproduce the calculations and produce the output file, you will need to do the following:

- Ensure that you have installed [Python](https://www.python.org/) and the Python libraries listed in `requirements.txt`.
- Run `jupyter notebook` from either the root or the `notebooks` directory.
- Open `notebooks/fake-news-analysis.ipynb` in Jupyter and run all the notebook’s cells.

Note: The Makefile and cleaning scripts are contained for reference but are not necessary to reproduce this analysis.

## Feedback/Questions?

Contact Scott Pham at [scott.pham@buzzfeed.com](scott.pham@buzzfeed.com).

Looking for more from BuzzFeed News? [Click here for a list of our open-sourced projects, data, and code](https://github.com/BuzzFeedNews/everything).
