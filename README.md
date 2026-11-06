Recruitment \& Hiring Analytics System



An end-to-end data analytics project designed to analyze recruitment performance, hiring funnels, recruiter efficiency, recruitment sources, salaries, candidate skills, and hiring outcomes.



\## Project Overview



This project simulates a real-world recruitment analytics environment where candidate, application, interview, offer, and hiring data are analyzed to identify actionable hiring insights.



The project combines:



\- SQL for business analysis

\- Python for data cleaning, EDA, and machine learning

\- Power BI for interactive dashboards

\- Candidate skill analysis

\- AWS S3 and IAM for cloud data storage and access control



\## Business Objectives



The analysis focuses on:



\- Understanding the recruitment funnel

\- Measuring application-to-hire conversion

\- Identifying high-performing recruitment sources

\- Comparing recruiter performance

\- Analyzing hiring trends over time

\- Understanding salary patterns across roles

\- Analyzing candidate skills and hiring outcomes

\- Building a baseline model to predict hiring outcomes



\## Technology Stack



| Area | Technology |

|---|---|

| Programming | Python |

| Database | PostgreSQL |

| Querying | SQL |

| Data Analysis | Pandas, NumPy |

| Visualization | Matplotlib, Seaborn |

| Dashboard | Power BI |

| Machine Learning | Scikit-learn |

| Skill Analysis | Python |

| Cloud | AWS S3, AWS IAM |

| Development | VS Code, Jupyter Notebook |



\## Dataset



The project contains 8 related datasets:



\- Candidates

\- Applications

\- Jobs

\- Recruiters

\- Recruitment Sources

\- Interviews

\- Offers

\- Hires



The database contains:



\- 2,000 candidates

\- 30 jobs

\- 10,000 applications

\- 3,049 interviews

\- 1,533 offers

\- 486 hires

\- 20 recruiters

\- 15 recruitment sources



\## Key Findings



\### Recruitment Funnel



| Stage | Count |

|---|---:|

| Applications | 10,000 |

| Interviews | 3,049 |

| Offers | 1,533 |

| Hires | 486 |



Overall application-to-hire conversion: \*\*4.86%\*\*



Average time to hire: \*\*40.22 days\*\*



\### Recruitment Source Analysis



The analysis compares recruitment sources based on:



\- Application volume

\- Interview conversion

\- Offer conversion

\- Hiring conversion



Consultancy, Employee Referral, and Glassdoor were among the strongest sources based on hiring conversion in the simulated dataset.



\### Recruiter Performance



Recruiters were ranked using:



\- Applications handled

\- Interviews

\- Offers

\- Hires

\- Hiring conversion



\### Role \& Salary Analysis



The project analyzes:



\- Hiring conversion by job role

\- Average offered salary

\- Application volume by role

\- Time-to-hire by role



\### Candidate Skill Analysis



Candidate skills were extracted and analyzed to identify:



\- Most common skills

\- Hiring rate associated with skills

\- Skills with sufficient application volume for reliable comparison



\## Machine Learning



A baseline hiring prediction model was developed using:



\- Age

\- Experience

\- Education

\- Job title

\- Department

\- Employment type

\- Recruitment source



Interview, offer, and hiring-stage information was intentionally excluded from model features to avoid data leakage.



Because only \*\*4.86%\*\* of applications resulted in hires, the target variable is highly imbalanced.



Model evaluation focuses on:



\- Precision

\- Recall

\- F1 Score

\- ROC-AUC



rather than accuracy alone.



\## Power BI Dashboard



The Power BI dashboard contains three major sections:



\### 1. Recruitment \& Hiring Analytics Dashboard



\- Recruitment funnel

\- Application volume

\- Hiring conversion

\- Recruitment source performance

\- Job role performance



\### 2. Hiring Performance



\- Hiring conversion by role

\- Recruiter performance

\- Salary analysis

\- Monthly application trends

\- Offer-to-hire conversion



\### 3. Source \& Recruitment Analysis



\- Recruitment source performance

\- Monthly hiring trends

\- Source-level application analysis

\- Average time to hire

\- Interactive source and job-role filters



\## AWS Architecture



```text

Raw Recruitment CSV Files

&#x20;         |

&#x20;         v

&#x20;     Amazon S3

&#x20;         |

&#x20;         v

&#x20;  AWS IAM Access Control

&#x20;         |

&#x20;         v

&#x20;Local PostgreSQL Database

&#x20;         |

&#x20;         v

&#x20;  SQL + Python Analysis

&#x20;         |

&#x20;         v

&#x20;     Power BI

AWS Components

Amazon S3

Stores the raw recruitment CSV datasets

8 datasets uploaded to the project bucket

Provides cloud-based object storage

AWS IAM

Implements least-privilege access

Custom RecruitmentS3ReadOnly policy created

Policy is scoped to the recruitment analytics S3 bucket



RDS was intentionally not provisioned to keep the project within a zero-spend AWS approach.



Project Structure

Recruitment-Hiring-Analytics/

│

├── data/

│   ├── applications.csv

│   ├── candidates.csv

│   ├── hires.csv

│   ├── interviews.csv

│   ├── jobs.csv

│   ├── offers.csv

│   ├── recruiters.csv

│   └── sources.csv

│

├── ml/

│   ├── model\_comparison\_improved.csv

│   ├── threshold\_analysis.csv

│   ├── feature\_importance\_improved.csv

│   ├── skill\_frequency.csv

│   └── skill\_hiring\_analysis.csv

│

├── notebooks/

│   ├── 01\_eda.ipynb

│   ├── 02\_ml\_model.ipynb

│   └── 03\_nlp\_analysis.ipynb

│

├── powerbi/

│

├── sql/

│   └── analysis.sql

│

├── src/

│   ├── generate\_data.py

│   └── load\_data.py

│

└── README.md

How to Run

1\. Clone the repository

git clone <repository-url>

cd Recruitment-Hiring-Analytics

2\. Create a virtual environment

python -m venv venv

3\. Activate the environment



Windows:



venv\\Scripts\\activate

4\. Install dependencies

pip install pandas numpy matplotlib seaborn sqlalchemy psycopg2-binary jupyter scikit-learn

5\. PostgreSQL



Create a PostgreSQL database named:



recruitment\_analysis



Load the datasets using the provided Python scripts.



Skills Demonstrated

Data Cleaning

Exploratory Data Analysis

SQL Analytics

Data Modeling

KPI Development

Business Intelligence

Power BI

Statistical Analysis

Machine Learning

Feature Engineering

Imbalanced Classification

Candidate Skill Analysis

AWS S3

AWS IAM

Business Problem Solving

Author



Ekansh Awasthi



B.Tech — Computer Science \& Engineering

