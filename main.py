import ipsuite as ips
from src import ReadNPZ

with ips.Project(automatic_node_names=True) as project:
    train_data = ReadNPZ(directory="data", regex="4comp.cfg_train_1")
    valid_data = ReadNPZ(directory="data", regex="4comp.cfg_valid_1")

    test_data = ReadNPZ(directory="data", regex="4comp.cfg_valid_1", name="TestData")

    model = ips.models.MACE(data=train_data, test_data=valid_data)

    predictions = ips.analysis.Prediction(data=test_data, model=model)
    analysis = ips.analysis.PredictionMetrics(data=predictions)

project.build()