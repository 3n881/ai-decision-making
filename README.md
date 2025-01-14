
# AI Decision-Making Model

The AI Decision-Making Model is a machine learning-based solution designed to classify text input (such as questions or queries) into one of three categories: Yes, No, or Maybe. Built using Python, Scikit-learn, and Flask, this model leverages the Multinomial Naive Bayes algorithm to process natural language data. It is packaged as a simple REST API for easy integration into other applications.

Whether you're building an automated assistant, recommendation system, or decision-support tool, this model can be customized and extended to meet your needs. It is lightweight, easy to use, and deployable to platforms like Heroku.


## Authors

- [@3n881](https://www.github.com/3n881)


## Installation

To install this project run

Step 1: Clone the Repository

```bash
git clone https://github.com/your-username/ai-decision-making.git
cd ai-decision-making
```
Step 2: Create a Virtual Environment

On Windows:

```bash
python -m venv venv
venv\Scripts\activate
```
On macOS/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```
Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```
## Usage

Step 1: Train the Model

```bash
python train_model.py
```
Step 2: Run the Flask Application

```bash
python app.py
```
App will run at http://127.0.0.1:5000/
## API Usage

Test the API
Example Request (cURL):

```bash
curl -X POST http://127.0.0.1:5000/predict -H "Content-Type: application/json" -d '{"input": "Should I buy a new phone?"}'
```
Example Response:

```bash
{
  "decision": "Maybe"
}
```
## Deployment

Deploy on Heroku
Login to Heroku:

```bash
heroku login
```

Create a New App:

```bash
heroku create your-app-name
```
Deploy the App:

```bash
git push heroku master
```
Open the App:

```bash
heroku open
```

