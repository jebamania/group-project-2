# group-project-2

## Data Source

"[Real / Fake Job Posting Prediction](https://www.kaggle.com/datasets/shivamb/real-or-fake-fake-jobposting-prediction)", licensed under [CC0](https://creativecommons.org/publicdomain/zero/1.0/)

## Dataset Summary

### Overview

This is a dataset with around 18 thousand real and fraudulent job descriptions. It includes open text descriptions as well as categorical & numeric data.

### Feature names

* job_id: a unique job ID
* title: the title of the job
* location: the geographical location of the job, typically formatted as "Country, State, City"
* department: a corporate department
* salary_range: indicative salary range, typically formatted like "100-1000" which would mean $100 to $1,000
* company_profile: a brief description of the company
* description: a detailed description of the job
* requirements: a description of requirements for the job
* benefits: a description of offered benefits
* telecommuting: whether the position has telecommuting
* has_company_logo: whether a company logo is present in the job posting
* has_questions: whether screening questions are present
* employment_type: a token for the type of employment, like Full-time, Part-time, Contract, etc.
* required_experience: a token for a level of experience, like Internship, Executive, Associate, etc.
* required_education: a token for a level of education, like High School or equivalent, Doctorate, Vocational, etc.
* industry: a token for an area of industry, like Computer Software, Sporting Goods, Hospitality, etc.
* function: a token for a functional area of work, like Engineering, Sales, Finance, etc.

### Target feature name

* fraudulent: a classification of whether the job posting was fraudulent

## Approach

Our objective is to build a model that can most accurately identify fraudulent job postings. The way that we are approaching this is by assigning different models (Random Forest, Logistical Regression, and XG Boost) to different team members to build with minimal data cleaning or transformation. Then once we have a baseline score to compare to, we are going to apply the cleaned data to our models to determine which model has the highest accuracy score.
