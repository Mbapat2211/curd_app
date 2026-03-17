# crud_app

## Tech Stack

**Frontend + Backend:** Python Streamlit  
**Database:** SQLite

With the limited time frame, I chose Python with the Streamlit framework for both the frontend and backend due to my prior experience building applications with it. SQLite was selected for its straightforward SQL integration with Streamlit, allowing me to demonstrate my SQL skills despite not using MySQL directly.

## Steps to Run Locally

Ensure Python and pip are installed on your local machine, then run the following commands:
```bash
pip install -r requirements.txt
```
```bash
streamlit run app.py
```

## Data Generation

I found this [GitHub repository](https://github.com/matt40k/Names?tab=readme-ov-file) containing CSV files of the most common forenames and surnames in the UK. Using these, I wrote a Python script that selects the top 100 forenames and top 100 surnames and generates every possible combination to produce 10,000 entries. Each email was formatted as `forename.surname@dummy.com` and each age was assigned a random number between 18 and 60.

## Reflection

### What parts of the stack were familiar to you?
Having previously worked with Python, Streamlit, and SQL, all major parts of the stack were familiar to me.

### What was new?
Streamlit is primarily designed for simple dashboards, particularly in machine learning tasks. While the platform does support more complex applications, building them requires the use of session state and context switching, which were areas I had not worked with before.

### What did you learn while doing this project?
This project reinforced the importance of choosing the right tool based on constraints, as selecting a familiar tech stack allowed me to focus on delivering core features within the limited time frame. I also gained practical experience thinking about performance and efficiency when handling 10,000+ records, and was reminded that real-world applications require more thought than just the happy path — with input validation, data sanitisation, and state management adding complexity that is not always obvious at the outset. Finally, I came to appreciate how much can be achieved within a short time box when you scope deliberately and prioritise core requirements before considering bonus features.

## Live Demo

The application is hosted and accessible at: https://curdapp-sfkdpf59cbqz3ahpt8woxl.streamlit.app/