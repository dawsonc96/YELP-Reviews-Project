# Opening a Successful Cafe: Business Analysis For Aspiring Cafe Owners 


<p align="center">
 <img width="480" height="240" src=Images/yelp.png>
 </p>


## OVERVIEW

This project aims to identify the best insights into the Cafe industry using the Yelp API data for existing cafes in the cities of Los Angeles and San Francisco for anyone looking to open a cafe in these two cities.


<p align="center">
 <img width="480" height="360" src=Images/Cafestockpic.jpg>
 </p>


## BUSINESS PROBLEM

A wealthy group of investors, known as Capital Partners LLC., have been dreaming about opening their own restaurant cafe and have finally decided to begin searching for the right destination. As they have offices in both San Francisco and Los Angeles, the team has narrowed it down to these two locations. They have hired your firm, Data Analysts LLC., to help them better understand each market and ultimately pick the best option of the two. Your team is in charge of exploring which environment will be more profitable through data-driven insights.

## REPOSITORY STRUCTURE

This repository contains a code notebook: yelp_setup.ipynb, a functions and a keys file which contains all code needed to analyze our data. An SQL datatabase (yelp.db) stores all data used for our project. The repository also containsa Readme file: README.md and an images folder for all visualizations and other external images.

## ANALYSIS CRITERIA

For this project, we used five criteria to try to detemine the best location for our cafe:

-Ratings

-Income

-Establishments per capita

-Price

-Review Counts

   **MEDIAN INCOME**
Los Angeles and San Francisco may be bustling cities located in the state of California, but they are very unique cities. Median income between SF and LA are vastly different; Los Angeles MI is just under $70,000, while San Francisco's is roughly $110,000. That gives us an idea that the buying power is much higher in SF than it is in LA. San Francisco, even with it's high cost of living, is still the city with the highest disposable income, not just in the state of California and the US, but also the world, according to this 2019 NBC news article (https://www.nbcbayarea.com/news/local/san-francisco-unseats-zurich-as-city-with-highest-salaries-and-most-disposable-income/156672/).
 
   **RATINGS**
Our next criteria was to assess the average rating of cafes in these two cities. As you can see, according to the data given to us by Yelp, there is not much difference in how customers rate the establishments in LA and SF. Even though cafes tend to rate better in San Francisco, the difference is negligible. Both tend to rate just slighly over 4 stars, with SF beating LA by a tiny margin. This is something we would expect across all major cities, as restaurants are usually compared to ones close in proximity to them (i.e. within the same city).
  
  **CAFES PER CAPITA**
In the graph below, we tried to assess how many cafes there are per capita by dividing total number of cafes in each city by the population of people within that given city. We times that number by 1000 to give us a more tangible data point to work with. We did this to determine where there might be a bigger demand for new cafes and whether or not a market is too saturated for a newcomer. According to our data, Los Angeles houses an average of 3.6 cafes for every 10,000 people while San Francisco houses 22.9 cafes for the same amount of people. This may have alot ot do with accessibility. Los Angeles is a spread out city, while San Francisco is a walker friendly city, limiting the ability for its residents to go to places far away and creating more of a demand of similar establishments in a smaller area. That means that even though the San Francisco market is more saturated, that may not be a sufficient reason for a shortage of demand there.

<p align="center">
 <img width="460" height="360" src=Images/Number_of_Cafes_per_Civilians.png>
 </p>
  
 **PRICE**
The biggest motivator for a business is money. We made this graph to help us determine whether a city is resistant to higher priced cafes. What we can gather from here is that there is only one classification of prices where Los Angeles beats San Francisco: low priced cafes. San Francisco is much more welcoming to medium priced, high priced, and exorbitantly priced cafes. Even if we assume that the high number of pricey cafes in SF might be because it has more cafes in general or has a higher median income, the fact that LA has more than double the amount of low priced cafes and 4.5x the population of SF shows that there is a market for high-end cafes within LA. That in itself is a huge reason why a business might get attracted to San Francisco.

<p align="center">
 <img width="700" height="460" src=Images/Distribution_of_cafes_by_price.png>
 </p>
  
  **REVIEW COUNTS**
Review counts can suggest how much attenion is being brought to a certain industry (espeically the restaurant/cafe industry). We have come up with two graphs to help us do some assessments in that area of this business. Our first graph shows the disparity of reviews between LA and SF. The amoount of reviews left as a perceantage of the population in SF is roughly 7x higher than that of LA, showing a huge discrepency between the two cities. The next graph reiterates this point. Even though LA has almost four times the population of SF, the number of reviews left under cafes in LA is almost half that of SF. What that may show is that people are not as enthusiastic about cafes in LA in comparison to SG. This could mean that cafes in LA dont provide that kind of service or environment/products to its customers like San Francisco cafes due on average, giving an aspiring cafe owner a chance to take advantage of the market. However, our next two graphs suggest that if you're trying to enter the high end market, you should really not worry about the review counts.
  
  
  <p align="center">
 <img width="700" height="460" src=Images/Review_count_as_pct_of_pop.png>
 </p>
 
 <p align="center">
 <img width="900" height="380" src=Images/Num_of_reviews_by_price_and_rating.png>
 </p>
  
 ## SUMMARY
  
  - Los Angeles cafes per capita than SF(roughly 3 to 22, respectively) , signifying that there may be room for new businesses to grow and acquire new customers, taking up unused market share.
  - Since there aren't that many high end cafes in LA in comparison to SF, we can use that as an opportunity to enter the high end market and increase our profitability.
  - Any new cafe owner in LA has an opportunity in the LA market to excite its customer base since the review counts suggest LA residents are much less excited about their cafes than those in SF.
  
  **Contributors**
  [Christa Dawson https://github.com/dawsonc96]
  [Saad Raees https://github.com/Saadraees09]
  
  
  
