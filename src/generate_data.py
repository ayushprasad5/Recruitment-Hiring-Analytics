
import pandas as pd
import numpy as np
from pathlib import Path

# -----------------------------
# SETTINGS
# -----------------------------

np.random.seed(42)

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
DATA_DIR.mkdir(exist_ok=True)

# Number of records
NUM_CANDIDATES = 2000
NUM_JOBS = 30
NUM_APPLICATIONS = 10000

# -----------------------------
# MASTER DATA
# -----------------------------

first_names = [
    "Aarav", "Vivaan", "Aditya", "Arjun", "Rohan",
    "Rahul", "Karan", "Ankit", "Akash", "Varun",
    "Neha", "Priya", "Ananya", "Isha", "Sneha",
    "Pooja", "Kavya", "Riya", "Simran", "Meera"
]

last_names = [
    "Sharma", "Verma", "Gupta", "Patel", "Singh",
    "Kumar", "Agarwal", "Mehta", "Shah", "Joshi",
    "Malhotra", "Kapoor", "Mishra", "Reddy", "Nair"
]

locations = [
    "Bangalore", "Mumbai", "Delhi", "Hyderabad",
    "Pune", "Chennai", "Ahmedabad", "Noida",
    "Gurgaon", "Kolkata"
]

education_levels = [
    "B.Tech", "B.E.", "B.Sc", "M.Tech",
    "MBA", "MCA", "M.Com"
]

skills_list = [
    "Python, SQL, Pandas",
    "SQL, Power BI, Excel",
    "Python, Machine Learning, SQL",
    "Java, Spring Boot, SQL",
    "React, JavaScript, HTML, CSS",
    "AWS, Python, SQL",
    "Excel, Power BI, SQL",
    "Python, Django, PostgreSQL",
    "Tableau, SQL, Excel",
    "Machine Learning, Python, NLP"
]

job_titles = [
    "Data Analyst",
    "Product Analyst",
    "Business Analyst",
    "Software Engineer",
    "Backend Developer",
    "Frontend Developer",
    "Data Scientist",
    "ML Engineer",
    "Product Manager",
    "Business Intelligence Analyst"
]

departments = {
    "Data Analyst": "Data",
    "Product Analyst": "Product",
    "Business Analyst": "Business",
    "Software Engineer": "Engineering",
    "Backend Developer": "Engineering",
    "Frontend Developer": "Engineering",
    "Data Scientist": "Data",
    "ML Engineer": "Data",
    "Product Manager": "Product",
    "Business Intelligence Analyst": "Data"
}

employment_types = [
    "Full-time",
    "Full-time",
    "Full-time",
    "Contract"
]

sources_list = [
    "LinkedIn",
    "Naukri",
    "Indeed",
    "Company Website",
    "Referral",
    "Internshala",
    "Glassdoor",
    "Campus Hiring",
    "Job Fair",
    "Employee Referral",
    "Consultancy",
    "AngelList",
    "CutShort",
    "Hirect",
    "Other"
]

recruiter_names = [
    "Aditi Sharma", "Rahul Verma", "Priya Singh", "Ankit Gupta",
    "Sneha Patel", "Rohit Mehta", "Neha Kapoor", "Karan Shah",
    "Pooja Agarwal", "Vivek Kumar", "Riya Joshi", "Arjun Nair",
    "Simran Reddy", "Kavya Mishra", "Varun Malhotra",
    "Isha Mehta", "Akash Patel", "Meera Shah", "Nikhil Gupta",
    "Sakshi Verma"
]

# -----------------------------
# 1. SOURCES
# -----------------------------

sources = pd.DataFrame({
    "source_id": range(1, len(sources_list) + 1),
    "source_name": sources_list
})

sources.to_csv(DATA_DIR / "sources.csv", index=False)

# -----------------------------
# 2. RECRUITERS
# -----------------------------

recruiters = pd.DataFrame({
    "recruiter_id": range(1, len(recruiter_names) + 1),
    "recruiter_name": recruiter_names,
    "recruiter_team": np.random.choice(
        ["Tech Hiring", "Data Hiring", "Product Hiring", "General Hiring"],
        len(recruiter_names)
    )
})

recruiters.to_csv(DATA_DIR / "recruiters.csv", index=False)

# -----------------------------
# 3. JOBS
# -----------------------------

job_rows = []

for job_id in range(1, NUM_JOBS + 1):
    title = np.random.choice(job_titles)

    opening_date = pd.Timestamp("2025-01-01") + pd.Timedelta(
        days=int(np.random.randint(0, 330))
    )

    closing_date = opening_date + pd.Timedelta(
        days=int(np.random.randint(30, 90))
    )

    job_rows.append({
        "job_id": job_id,
        "job_title": title,
        "department": departments[title],
        "location": np.random.choice(locations),
        "employment_type": np.random.choice(employment_types),
        "opening_date": opening_date.date(),
        "closing_date": closing_date.date()
    })

jobs = pd.DataFrame(job_rows)

jobs.to_csv(DATA_DIR / "jobs.csv", index=False)

# -----------------------------
# 4. CANDIDATES
# -----------------------------

candidate_rows = []

for candidate_id in range(1, NUM_CANDIDATES + 1):

    name = (
        np.random.choice(first_names)
        + " "
        + np.random.choice(last_names)
    )

    candidate_rows.append({
        "candidate_id": candidate_id,
        "candidate_name": name,
        "gender": np.random.choice(
            ["Male", "Female", "Other"],
            p=[0.48, 0.48, 0.04]
        ),
        "age": int(np.random.randint(21, 40)),
        "experience_years": round(
            np.random.uniform(0, 12), 1
        ),
        "highest_education": np.random.choice(
            education_levels
        ),
        "current_location": np.random.choice(
            locations
        ),
        "skills": np.random.choice(
            skills_list
        )
    })

candidates = pd.DataFrame(candidate_rows)

candidates.to_csv(DATA_DIR / "candidates.csv", index=False)

# -----------------------------
# 5. APPLICATIONS
# -----------------------------

application_rows = []

candidate_ids = np.random.randint(
    1, NUM_CANDIDATES + 1, NUM_APPLICATIONS
)

job_ids = np.random.randint(
    1, NUM_JOBS + 1, NUM_APPLICATIONS
)

for application_id in range(1, NUM_APPLICATIONS + 1):

    application_date = pd.Timestamp("2025-01-01") + pd.Timedelta(
        days=int(np.random.randint(0, 365))
    )

    # Different sources have different effectiveness
    source_id = np.random.choice(
        sources["source_id"],
        p=[
            0.15, 0.18, 0.08, 0.10, 0.10,
            0.05, 0.05, 0.06, 0.03, 0.06,
            0.04, 0.02, 0.03, 0.03, 0.02
        ]
    )

    status = np.random.choice(
        [
            "Applied",
            "Screening",
            "Rejected",
            "Interview",
            "Offer",
            "Hired"
        ],
        p=[0.20, 0.20, 0.30, 0.15, 0.10, 0.05]
    )

    application_rows.append({
        "application_id": application_id,
        "candidate_id": candidate_ids[application_id - 1],
        "job_id": job_ids[application_id - 1],
        "source_id": int(source_id),
        "recruiter_id": int(
            np.random.randint(1, len(recruiter_names) + 1)
        ),
        "application_date": application_date.date(),
        "application_status": status
    })

applications = pd.DataFrame(application_rows)

applications.to_csv(DATA_DIR / "applications.csv", index=False)

# -----------------------------
# 6. INTERVIEWS
# -----------------------------

interview_rows = []

interview_id = 1

# Applications that reach interview stage
interview_applications = applications[
    applications["application_status"].isin(
        ["Interview", "Offer", "Hired"]
    )
]

for _, app in interview_applications.iterrows():

    interview_date = pd.Timestamp(
        app["application_date"]
    ) + pd.Timedelta(
        days=int(np.random.randint(3, 30))
    )

    interview_rows.append({
        "interview_id": interview_id,
        "application_id": int(app["application_id"]),
        "interview_date": interview_date.date(),
        "interview_type": np.random.choice(
            ["Technical", "HR", "Managerial", "Case Study"]
        ),
        "interview_round": int(
            np.random.randint(1, 4)
        ),
        "interview_status": np.random.choice(
            ["Passed", "Failed"],
            p=[0.65, 0.35]
        ),
        "interview_score": round(
            np.random.uniform(40, 100), 2
        )
    })

    interview_id += 1

interviews = pd.DataFrame(interview_rows)

interviews.to_csv(DATA_DIR / "interviews.csv", index=False)

# -----------------------------
# 7. OFFERS
# -----------------------------

offer_rows = []

offer_id = 1

offer_applications = applications[
    applications["application_status"].isin(
        ["Offer", "Hired"]
    )
]

for _, app in offer_applications.iterrows():

    offer_date = pd.Timestamp(
        app["application_date"]
    ) + pd.Timedelta(
        days=int(np.random.randint(15, 45))
    )

    offer_rows.append({
        "offer_id": offer_id,
        "application_id": int(app["application_id"]),
        "offer_date": offer_date.date(),
        "offered_salary": round(
            np.random.uniform(400000, 1800000), 2
        ),
        "offer_status": np.random.choice(
            ["Accepted", "Rejected", "Pending"],
            p=[0.70, 0.20, 0.10]
        )
    })

    offer_id += 1

offers = pd.DataFrame(offer_rows)

offers.to_csv(DATA_DIR / "offers.csv", index=False)

# -----------------------------
# 8. HIRES
# -----------------------------

hire_rows = []

hire_id = 1

hire_applications = applications[
    applications["application_status"] == "Hired"
]

for _, app in hire_applications.iterrows():

    hire_date = pd.Timestamp(
        app["application_date"]
    ) + pd.Timedelta(
        days=int(np.random.randint(20, 60))
    )

    joining_date = hire_date + pd.Timedelta(
        days=int(np.random.randint(7, 30))
    )

    hire_rows.append({
        "hire_id": hire_id,
        "application_id": int(app["application_id"]),
        "hire_date": hire_date.date(),
        "joining_date": joining_date.date(),
        "final_salary": round(
            np.random.uniform(450000, 1800000), 2
        )
    })

    hire_id += 1

hires = pd.DataFrame(hire_rows)

hires.to_csv(DATA_DIR / "hires.csv", index=False)

# -----------------------------
# SUMMARY
# -----------------------------

print("\nDATA GENERATION COMPLETE")
print("-------------------------")

print(f"Candidates   : {len(candidates)}")
print(f"Jobs         : {len(jobs)}")
print(f"Applications : {len(applications)}")
print(f"Interviews   : {len(interviews)}")
print(f"Offers       : {len(offers)}")
print(f"Hires        : {len(hires)}")

print("\nCSV files saved to:")
print(DATA_DIR)