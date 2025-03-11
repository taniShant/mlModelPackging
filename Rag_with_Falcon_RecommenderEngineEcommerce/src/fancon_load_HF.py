#Use Falcon-7B or Falcon-40B from Hugging Face.
# Deploy it as a SageMaker endpoint.
import sagemaker
from sagemaker.huggingface import HuggingFaceModel

hub = {
    'HF_MODEL_ID': 'tiiuae/falcon-7b-instruct',  # Falcon model
    'HF_TASK': 'text-generation'
}

role = "arn:aws:iam::123456789012:role/SageMakerExecutionRole"

falcon_model = HuggingFaceModel(
    model_data=None,  # We use Hugging Face Model Hub
    role=role,
    transformers_version="4.26",
    pytorch_version="1.13",
    py_version="py39",
    env=hub
)

##xposing as endpt

falcon_predictor = falcon_model.deploy(
    initial_instance_count=1,
    instance_type="ml.g5.2xlarge"  # Adjust based on needs
)
