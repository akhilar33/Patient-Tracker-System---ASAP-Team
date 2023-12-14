cd "./test"
coverage run --branch DAO_testing.py
coverage report -m 
coverage html -d decision_html
