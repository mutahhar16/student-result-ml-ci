# Student Result ML CI

## Project Overview

This project demonstrates Machine Learning model training and Continuous Integration (CI) using Python, scikit-learn, automated testing, and GitHub Actions.

The system predicts whether a student passes or fails based on attendance, internal marks, assignment marks, and previous scores.

## Objectives

- Generate a reproducible dataset containing 300 student records.
- Train a Logistic Regression classification model.
- Evaluate model performance using accuracy and a confusion matrix.
- Save the trained model and evaluation metrics.
- Automatically execute seven unit tests through GitHub Actions.
- Demonstrate an intentional test failure and restore the passing state.

## Project Structure

- `train_model.py` — Generates the dataset, trains the model, evaluates it, and saves the outputs.
- `test_ml_pipeline.py` — Contains seven automated tests for the ML pipeline.
- `requirements.txt` — Lists the Python dependencies.
- `README.md` — Documents the project.
- `.github/workflows/ml-ci.yml` — Defines the GitHub Actions workflow.

## Technologies Used

- Python 3.11
- NumPy
- Pandas
- Scikit-learn
- Joblib
- GitHub Actions
- Python unittest

## Machine Learning Workflow

1. Generate a synthetic dataset containing 300 student records.
2. Calculate weighted scores using attendance, internal marks, assignment marks, and previous scores.
3. Split the dataset into 240 training records and 60 testing records.
4. Train a Logistic Regression model with feature scaling.
5. Evaluate the model using accuracy and a confusion matrix.
6. Save the trained model as `student_result_model.pkl`.
7. Save the evaluation metrics as `metrics.json`.
8. Save the generated dataset as `student_results.csv`.

## Automated Testing

The pipeline includes seven tests that verify:

1. The dataset contains 300 records.
2. The required dataset columns exist.
3. The trained model file exists.
4. The metrics file exists.
5. The model predicts PASS for suitable inputs.
6. The model predicts FAIL for unsuitable inputs.
7. The accuracy value is within the valid range of 0 to 1.

## Continuous Integration

The GitHub Actions workflow runs automatically when changes are pushed to the `main` branch or when a pull request targets `main`.

The workflow checks out the repository, configures Python, installs dependencies, trains the ML model, and runs the automated tests.

## Failure Demonstration

An intentional test failure was introduced by changing the expected dataset record count from 300 to 301. The test correctly failed because the actual dataset contained 300 records.

The expected count was restored to 300, and the workflow completed successfully.

## Conclusion

This practical demonstrates how machine learning training and automated unit testing can be integrated into a GitHub Actions CI pipeline. It also shows how an intentional failure can be detected, corrected, and verified with a successful workflow run.
