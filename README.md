
# Phase 1 Project Templates and Examples

This repo contains templates and examples to help you get started with your Phase 1 Project. Each of these is in a separate branch as explained below.

- The **template-mvp** branch is the template you should use to for your Phase 1 Project. MVP stands for Minimum Viable Product, but this isn't meant in a negative way - if your project uses this template, it will be functional and accessible.

- The **example-mvp** branch is an example project using the MVP template.

Once you've completed your project using the MVP template, you can improve it using the Above and Beyond (AAB) template if you have time:

- The **template-aab** branch is the AAB template to use to keep improving your project.

- The **example-aab** branch is an example project using the AAB template.

# Microsoft Studio Movie Analysis

![director_shot.jpeg](./images/director_shot.jpeg)

**Authors**: [Ben Spilsbury](mailto:benjamin.spilsbury@gmail.com), [Michael Wirtz](mailto:mwirtz@tulane.edu)

## Overview

This project analyzes the needs of Microsoft Corporation, who is considering adding a movie studio to their business portfolio. Descriptive analysis of movie genres, composers, directors, release year, runtime, production budget and target audience shows recommendations for the previously stated in an attempt to maximize financial gain: (1) Genre: Animation or Adventure; (2) Composer: Ed Côrtes; (3) Director: John Woo or Matt Bettinelli-Olpin; (4) Release Year: partner with existing studio to produce; (5) Runtime: feature film length; (6) Production Budget: lower budget linked to higher profitability; (7) Target Audience: 'G' rating. Sample data from online movie databases is used to correlate movie characteristics with financial success in order to ultimately perform this analysis. Microsoft Corporation can use this data to plan out relevant details for its first studio production. 

## Business Problem

Similar to other large tech companies, Microsoft has made the decision to create a movie streaming service, complete with their own originally produced content, and they're seeking guidance in order to ensure the service's success, specifically with regard to what types of movies Microsoft should produce. It is the task of the data science team to quantify what success for a movie actually means and then identify film characteristics that drive to such success. Historical data from internet movie databases are used to perform analysis. Through this analysis, four financial indicators (gross revenue, net profit, return on investment, and quality-weighted return on investment) are measured against seven film traits (genre, runtime, production budget, target audience, director, composer, release year). Overall, then, it is the goal of the data science team to answer the questions, "To what degree does each one of these traits influence a film's success? And what exactly is the nature of that influence?" Armed with this knowledge, Microsoft will have an idea of the approximate profiles of films they should make for their streaming service.

## Data

Mentioned in the Business Problem, the team is using historical film data in order to run analyses and find trends. This data comes from the following online movie databases:

    - Box Office Mojo
    - IMDB
    - Rotten Tomatoes
    - The MovieDB.org
    
Data includes all necessary info for both the four financial success indicators (needed bits of data for each movie were worldwide gross, production budget, and popular review rating out of ten) and the seven examined film traits (each specific film trait was found individually in the data; extra web scrubbing of IMDB is performed to fill in discontinuities found in MPAA rating data). A cleaned data set of ~2000 movies is ultimately used for all analysis.

## Methods

Overall, this project analyzes each of the seven possible film traits that drive success in the same way. For every trait, each film's value is plotted against its four financial indicators. For continuous data, non-categorical data, correlations are calculated to determine the degree to which that trait has any impact on success. In cases where the examined trait is instead categorical/discrete in nature, all films with like characteristic values (e.g. a "G" MPAA rating) are grouped together, and median financial indicators are examined (to limit the effect of outliers on data). As a result, the data team produces four graphs for each film characteristic, illustrating how they are individually related to each success indicator.

## Results

General trends were able identified among most all of the seven traits. Specific conclusions for each trait can be seen in the Conclusions section. Overall, though, results pointed to small groupings of candidate genres, target audiences, directors, and composers to choose from or enlist in a new successful movie project. Relatively low correlation is seen between a movie's success and its runtime (successful movies can be made generally at any runtime) or production budget (when a movie's revenue is normalized against its cost, a movie of any production budget size can be both successful or unsuccessful), so recommendation pertaining to those traits is mainly strategic or abstract in nature. Generally for release year, success indicators seem to be increasing with time, save a dip last year in 2019.

As a result of analysis, four graphs were constructed for each film characteristic that measured its performance across the four established success criteria. An example of one such graph (for the characteristic of genre) can be seen below:

![genre_plots.png](./images/genre_plots.png)

All success indicators were considered in the analysis, but ROI was focused on as possibly the most important metric since, at the end of the day, that is likely what Microsoft would most prefer to maximize.

## Conclusions

In general conclusions and recommendations are able to be made about each of the examined film characteristics and their influence on success:
<ul>
<li><b>Genre:</b> Out of all genres, the recommendation would be to make a movie in the Animation or Adventure genres, as they are the most reliably successful.</li>
<li><b>Runtime:</b> The recommendation is to make at least a feature-length film (~80 minutes). Otherwise, this trait seems to have no strong effect on success.</li>
<li><b>Production Budget:</b> Although this trait didn't seem to have too much an influence on success, it is recommended to produce many lower budget movies as opposed to a handful higher budget movies. If the budget doesn't seem to have too great of an impact on an individual movie's success, Microsoft should prioritize creating more content for their service in the form of cheaper films and shows as opposed to a handful of more expensive ones.</li>
<li><b>Target Audience:</b> The recommendation is to create films open to wider audiences (for the whole family) as opposed to just adult ones.</li>
<li><b>Director:</b> The recommendation is hire either John Woo or Jim Jarmusch, with Jim Jarmusch being the best overall hire for profitability</li>
<li><b>Composer:</b> The recommendation is best off of a comparison between the composers linked to the highest grossing movies. With that in mind, any choice would be worthwhile. The absolute best choice, however, would be Ed Côrtes for composer.</li>
<li><b>Year:</b> The objective of this analysis was to find a trend it movie profitability over the past few years. There was a clear upward trend going up through 2018. This trend reversed and profitability steeply declined in 2019. This might be a good opportunity for Microsoft to partner with or acquire a struggling movie studio instead of creating a whole new one on its own.</li>
</ul>

### Next Steps

Further analysis into each of the factors tested above may produce more accurate and/or specific and actionable insights. Moving into the future, we could look at the following: 

 - Model the salary of directors vs median movie ROI for that director
 - Model composers' genre variations to find most versatile composer
 - Model line of best fit for year to find a usable trendline
 - Overall, analyze each of our seven examined characteristics over time as opposed to all at once to identify recent trends in the industry and capitalize on those
 - Microsoft should develop a business strategy, defining what they ultimately want to get out of their new studio and service. With a defined strategic goal in mind, success criteria can be further expanded upon and researched (e.g. if Microsoft decides they want to focus on competing with streaming competitors as opposed to pure profitability, perhaps research can delve further into content creation and expanding market share as opposed to financial indicators like ROI.)

## For More Information

See the full analysis in the [Jupyter Notebook](./code_success_movie.ipynb) or review this [presentation](./slides_successful_movie.pdf).

For additional info, contact Ben Spilsbury or Michael Wirtz at
[benjamin.spilsbury@gmail.com](mailto:benjamin.spilsbury@gmail.com) or [mwirtz@tulane.edu](mailto:mwirtz@tulane.edu), respectively

## Repository Structure

```
├── data
├── images
├── README.md
├── code_successful_movie.ipynb
└── slides_successful_movie.pdf

