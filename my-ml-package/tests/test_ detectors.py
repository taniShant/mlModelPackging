# Similarly to the previous case, we create a script for holding our tests in tests/test_ detectors.py. Since we are testing more complex functionality, we will have to import more pieces of the package into the script:
import pytest
from outliers.detectors.detection_models import DetectionModels
from outliers.detectors.pipelines import OutlierDetector
from outliers.definitions import MODEL_CONFIG_PATH
import outliers.utils.data
import numpy as np
# 7.We will have the same fixture for dummy data created as in Step 2, but now we also have a fixture for creating some example models to use in tests:

models = DetectionModels(MODEL_CONFIG_PATH)
return models

# 8. Our final fixture creates an example detector instance for us to use, based on the previous model’s fixture:
9. And now we are ready to test some of the model creation functionality. First, we can test that the models we created are not empty objects:

@pytest.fixture()
def example_detector(example_models):
    model = example_models.get_models()[0]
    detector = OutlierDetector(model=model)
    return detector

# 9. And now we are ready to test some of the model creation functionality. First, we can test that the models we created are not empty objects:
# 
def test_model_creation(example_models):
    assert example_models is not None

# 10. We can then test that we can successfully retrieve models using the instance of DetectionModels created in Step 6:
def test_model_get_models(example_models):
    example_models.get_models() is not None

# 11. Finally, we can test that the results found by applying the model pass some simple tests. This shows that the main pieces of our package are working for an end-to-end application:
def test_model_evaluation(dummy_data, example_detector):
    result = example_detector.detect(dummy_data)
    assert len(result[result == -1]) == 39 #number of anomalies to detect
    assert len(result) == len(dummy_data) #same numbers of results assert np.unique(result)[0] == -1
    assert np.unique(result)[1] == 1 

#12. As in Step 4, we can run the full test suite from the command line. We add a verbosity flag to return more information and show the individual tests that pass. This helps confirm that both our data utility and our model tests are being triggered:
# pytest –-verbose    