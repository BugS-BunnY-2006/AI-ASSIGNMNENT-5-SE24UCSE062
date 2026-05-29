

# Bayesian Networks: Modelling, Problem Representation and Inferencing

## Aim

To study Bayesian Networks, explore tools used for modelling and inferencing, and implement a real-world example using Bayesian Networks.

---

# Introduction

Bayesian Networks (BNs), also called Belief Networks, are probabilistic graphical models used to represent uncertain knowledge. They combine probability theory and graph theory to model relationships between variables.

Bayesian Networks are widely used in Artificial Intelligence for reasoning under uncertainty, decision-making, prediction, diagnosis, and risk analysis.

A Bayesian Network consists of nodes representing variables and directed edges representing dependencies between those variables.

One of the biggest advantages of Bayesian Networks is that they can make predictions even when some information is missing.

---

# Components of a Bayesian Network

### 1. Nodes

Nodes represent random variables.

Examples:

```text
Rain
Traffic
Accident
Disease
Fever
```

---

### 2. Directed Edges

Edges represent causal relationships.

Example:

```text
Rain → Traffic
```

This means traffic conditions depend on rain.

---

### 3. Conditional Probability Tables (CPT)

Each node contains probabilities describing how it depends on its parent nodes.

Example:

```text
P(Traffic | Rain)
```

---

# Bayesian Network Representation

Consider a simple weather example:

```text
        Rain
       /    \
      v      v
 Traffic   Accident
```

Meaning:

* Rain influences Traffic.
* Rain influences Accident.

---

# Tools Used for Bayesian Networks

## 1. GeNIe

GeNIe is one of the most popular tools for creating Bayesian Networks.

Features:

* Graphical interface
* Drag-and-drop modelling
* Probability editing
* Inferencing support

Applications:

* Medical diagnosis
* Risk analysis
* Decision support systems

---

## 2. Netica

Netica is a commercial software package for Bayesian Networks.

Features:

* Bayesian modelling
* Visualization
* Learning from data
* Prediction and inferencing

Advantages:

* User-friendly interface
* Good visualization tools

---

## 3. Hugin

Hugin is a professional Bayesian Network tool.

Features:

* Probabilistic reasoning
* Decision analysis
* Knowledge engineering

Applications:

* Healthcare
* Finance
* Industrial systems

---

## 4. pgmpy (Python)

pgmpy is a Python library for Probabilistic Graphical Models.

Features:

* Bayesian Networks
* Markov Networks
* Inferencing
* Learning from data

Advantages:

* Open source
* Easy integration with Python

---

## 5. BayesiaLab

BayesiaLab is an advanced platform for Bayesian modelling.

Features:

* Machine learning integration
* Bayesian inference
* Data visualization

---

# Example Problem

## Medical Diagnosis System

A patient may have a disease which can cause fever.

Network:

```text
Disease -----> Fever
```

Variables:

```text
Disease = Yes / No

Fever = Yes / No
```

---

# Probability Tables

### Prior Probability

```text
P(Disease = Yes) = 0.1

P(Disease = No) = 0.9
```

---

### Conditional Probability

```text
P(Fever = Yes | Disease = Yes) = 0.8

P(Fever = No | Disease = Yes) = 0.2
```

```text
P(Fever = Yes | Disease = No) = 0.1

P(Fever = No | Disease = No) = 0.9
```

---

# Bayesian Network Diagram

```text
Disease
    |
    v
  Fever
```

---

# Python Implementation Using pgmpy

## Installation

```bash
pip install pgmpy
```

---

## Implementation Code

```python
from pgmpy.models import DiscreteBayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

# Create Bayesian Network

model = DiscreteBayesianNetwork([
    ('Disease', 'Fever')
])

# Prior Probability

cpd_disease = TabularCPD(
    variable='Disease',
    variable_card=2,
    values=[[0.9], [0.1]]
)

# Conditional Probability Table

cpd_fever = TabularCPD(
    variable='Fever',
    variable_card=2,
    values=[
        [0.9, 0.2],
        [0.1, 0.8]
    ],
    evidence=['Disease'],
    evidence_card=[2]
)

# Add CPDs

model.add_cpds(
    cpd_disease,
    cpd_fever
)

# Check Model

print(
    "Model Valid:",
    model.check_model()
)

# Inference

inference = VariableElimination(model)

result = inference.query(
    variables=['Disease'],
    evidence={'Fever': 1}
)

print(result)
```

---

# Sample Output

```text
Model Valid: True

+-------------+-------------+
| Disease     | Probability |
+-------------+-------------+
| Disease(0)  | 0.692       |
| Disease(1)  | 0.308       |
+-------------+-------------+
```

---

# Interpretation

Suppose a patient has fever.

The Bayesian Network updates the probability of disease based on the observed evidence.

Before observing fever:

```text
P(Disease) = 0.1
```

After observing fever:

```text
P(Disease | Fever)
```

becomes higher.

This demonstrates Bayesian inferencing.

---

# Advantages of Bayesian Networks

1. Handles uncertainty effectively.
2. Supports probabilistic reasoning.
3. Can work with incomplete information.
4. Easy visualization of dependencies.
5. Useful in prediction and diagnosis systems.

---

# Limitations

1. Requires accurate probability values.
2. Large networks become complex.
3. Model construction may require expert knowledge.

---

# Conclusion

In this experiment, Bayesian Networks were studied as a powerful probabilistic graphical model for representing uncertain knowledge. Various tools such as GeNIe, Netica, Hugin, pgmpy, and BayesiaLab were explored for modelling and inferencing. A medical diagnosis example was implemented using Python and the pgmpy library. The results demonstrated how Bayesian Networks can perform inference and update probabilities when new evidence becomes available, making them highly useful for intelligent decision-making systems.
