# from job_posting_scraper import scrape_job
# import db_manager
import setup_db
import db_loader_generic
from db_manager import get_person_info

db_path = r"resume.db"
setup_db.db_builder(db_path)
db_loader_generic.load_generic(db_path)

full_name, email, phone, linkedin, github = get_person_info(db_path, 1)
print(f"{full_name}, {email}, {phone}, {linkedin}, {github}")


# job_url = "https://www.governmentjobs.com/careers/tacoma/jobs/4779178/customer-service-representative"  # Replace with actual job URL
# job_info = scrape_job(job_url)
#
# for item in job_info:
#     print(f"{item}: {job_info[item]}")
# for table in db_manager.get_schema(db_path):
#     print(table[0])
