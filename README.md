# group-project-2

## Data Source

"[Real / Fake Job Posting Prediction](https://www.kaggle.com/datasets/shivamb/real-or-fake-fake-jobposting-prediction)", licensed under [CC0](https://creativecommons.org/publicdomain/zero/1.0/)

## Dataset Summary
### Overview
This is a dataset with around 18K real and fradulent job descriptions. It includes of open text descriptions as well as some categorical, and numeric data.

### Feature names
* job id 
* title 
* location 
* department 
* salary_range
* company_profile 
* description 
* requirements 
* benefits 
* telecommuting
* has_company_logo 
* has_questions 
* employment_type 
* required_experience 
* required_education 
* Industry 
* Function

### Target name
* Fraudulent

## Approach
* Our objective is to build a model that can most accurately identify fraudulent job postings. The way that we are approaching this is by assigning different models (Random Forest, Logistical Regression, and XG Boost) to different team members to build with minimal data cleaning or transformation. Then once we have a baseline score to compare to, we are going to apply the cleaned data to our models to determine which model has the highest accuracy score.

