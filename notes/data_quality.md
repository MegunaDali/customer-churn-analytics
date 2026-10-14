## Churn

**Analytical type:** Binary target

**Encoding:**
- 0 = customer did not churn
- 1 = customer churned

**Distribution:**
- Non-churn: 2,655 observations (84.29%)
- Churn: 495 observations (15.71%)

**Initial interpretation:**

The target is imbalanced, with approximately 5.4 non-churn observations
for every churn observation.

A naive model that predicts every observation as non-churn would achieve
approximately 84.29% accuracy while identifying zero churners.

Therefore, model accuracy alone will not be sufficient for evaluating
future churn models.

Metrics such as precision, recall, the confusion matrix, and potentially
ranking-based measures should also be considered depending on the
business cost and capacity of retention interventions.

**Important limitation:**

The 15.71% churn rate describes this dataset. It should not automatically
be interpreted as evidence that the telecom company's churn rate is
"high" or "bad" without additional business and time-period context.


## Complains

**Analytical type:** Binary categorical variable

**Encoding:**
- 0 = No recorded complaint
- 1 = Recorded complaint

**Distribution:**
- No complaint: 2,909 observations (92.35%)
- Complaint: 241 observations (7.65%)

**Relationship with churn:**

| Complaint status | Retained | Churned | Churn rate |
|---|---:|---:|---:|
| No complaint | 2,614 | 295 | 10.14% |
| Complaint | 41 | 200 | 82.99% |

**Initial interpretation:**

Customers with recorded complaints exhibit a substantially higher churn rate (82.99%) than customers without complaints (10.14%).

The observed churn rate among complaining customers is approximately 8.18 times higher.

However, 295 of the 495 churned customers (59.60%) had no recorded complaint.

This indicates that complaints are strongly associated with churn, but complaint status alone cannot identify all customers who eventually leave.

**Business implications:**

- Complaint status could be a useful indicator for identifying customer segments with elevated churn risk.
- Complaint handling and service quality deserve further investigation as potential areas for retention improvements.
- Since most churned customers had no recorded complaint, additional behavioral and service-related variables should be examined.

**Important limitations:**

- The observed association does not establish causation.
- The dataset does not establish the precise timing of individual complaints.
- Complaint status alone is insufficient to explain customer churn.
- The findings should not be generalized to the entire telecom customer population without additional context.

## Call Failure

**Analytical type:** Discrete numerical variable

**Distribution:**
- Mean: 7.63
- Median: 6
- Standard deviation: 7.26
- Range: 0–36
- Customers with zero failures: 702 (22.29%)

**Relationship with churn:**

- Retained customers: 7.66 average failures
- Churned customers: 7.48 average failures

**Initial interpretation:**

Average call-failure counts are similar for retained and churned customers, suggesting that failure counts alone do not clearly distinguish the two groups.

Exploratory segmentation suggests a possible non-linear relationship between call failures and churn.

However, higher failure counts are also associated with greater calling activity. This indicates that the absolute number of failures may partly reflect differences in service usage rather than differences in connection quality.

**Important limitations:**

- Exploratory group boundaries are arbitrary.
- The number of failed calls does not necessarily represent connection reliability.
- The observed associations do not establish causation.
- Further analysis of calling activity is required to understand these relationships.