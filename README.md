# Insurance-Quote-Provider

The BMI_Predictor jupter notebook file contains code blocks providing answers for problem 1 and problem 2.

The training dataset is created following the rules mentioned in the assignment

3 different types of Regression models are trainied to predict the BMI which are 
  Elastic Net Regression
  AdaBoost Regression
  K-Neighbours Regression

All the regression models are finetuned using GridSearch and the best models are evaluated using R-Squared Score

R^2 Scores:
|Model                 |Training Set    |Testin Set       |
| :--                  | :--            | :--             |
|Elastic Net           |0.942           |0.944            |
|AdaBoost              |0.978           |0.918            |
|K-Neighbours          |1.0             |0.6711           |

From the above reported scores we can identify that Elastic Net Regression model performs best in predicting the BMI. The Elastic Net regressor
with the best set of parameters is saved and is used for building the Insurance quote provider application.

The python file whe run will ask the user to enter their Age, Gender, Height and Weight, after entering those informations the user will be provided with
their Insurance quote and the reason for providing that quote.
  
