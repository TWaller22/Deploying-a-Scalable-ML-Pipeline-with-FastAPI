# Model Card

For additional information see the Model Card paper: https://arxiv.org/pdf/1810.03993.pdf

## Model Details

This Random Forest Classifier predicts whether an individual earns more than $50k annually using data from the 1994 U.S. Census. It leverages demographic features such as age, education, work status, and marital status to make predictions. 

## Intended Use

This model is primarily designed for academic purposes, demostrating the application of machine learning techniques on census data. It should not be used for cirtical decision-making in real-world scenarios.

## Training Data

The model was trained using the 1994 U.S. Census dataset, which includes demographic attributes such as age, education level, occupation, and race. The data was split into 80% training data and 20% test data to train and evaluate the model's performance.

## Evaluation Data

This model was evaluated using a test dataset representing 20% of the total data.

## Metrics
Precision: 0.7419 | Recall: 0.6384 | F1: 0.6863

## Ethical Considerations


The model could be subject to bias due to the underreprsentation of certain groups in the dataset, potentially affecting predicition accuracy. Furthermore, the data contains personal demographic information, raising privacy concerns. 
## Caveats and Recommendations

The data used to train the model is over 30 years old, making it unsuitable for contemporary predicitions. The nodel is best suited for educational use to explore machine learning techniques. For real-world applications, the model should be retrained with more recent, representative data. Bias in the data could impact predictions, especially for underrepresented groups. 