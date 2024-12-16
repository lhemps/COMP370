Q1: What is the difference between found and designed data?
    - found data is prexisting data made for other purposes originally (ie. my little pony transcripts, ncy 311 dataset, etc. for previous assignments), while designed data is data which needs to be constructed specifically for this project (ie. the montreal gazette trending articles scraped from the website for this assignment specifically)
Q2: What are the two primary challenges that necessitate sampling when collecting data?
    - scale (ie. API call limit, storage, cost, time, etc.)
    - your query is too undefined to be collected directly so having all the data isn't necessarily useful (eg. how do we tell which twitter users are bots? getting every tweet that exists instead of trying to figure out what characterizes bot behaviour would be counterproductive!)
Q3: Why are website owners more likely to be upset about collecting data using scrapers than using APIs?
    - an API backend is a lot more streamlined than loading all the display elements of a full webpage, and scraping can require more page requests to get the right/enough data, so using scrapers taxes the website owners resources a lot more than an API.