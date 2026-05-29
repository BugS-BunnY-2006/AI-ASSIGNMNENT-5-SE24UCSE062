from pgmpy.models import DiscreteBayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

# Create Bayesian Network

model = DiscreteBayesianNetwork([
    ('Rain', 'Traffic'),
    ('Rain', 'Accident')
])

# Rain Probability

cpd_rain = TabularCPD(
    variable='Rain',
    variable_card=2,
    values=[[0.7], [0.3]]
)

# Traffic Probability

cpd_traffic = TabularCPD(
    variable='Traffic',
    variable_card=2,
    values=[
        [0.8, 0.2],
        [0.2, 0.8]
    ],
    evidence=['Rain'],
    evidence_card=[2]
)

# Accident Probability

cpd_accident = TabularCPD(
    variable='Accident',
    variable_card=2,
    values=[
        [0.9, 0.4],
        [0.1, 0.6]
    ],
    evidence=['Rain'],
    evidence_card=[2]
)

# Add CPDs

model.add_cpds(
    cpd_rain,
    cpd_traffic,
    cpd_accident
)

# Verify Model

print("Model Valid:",
      model.check_model())

# Inference

inference = VariableElimination(model)

result = inference.query(
    variables=['Rain'],
    evidence={'Traffic': 1}
)

print(result)
