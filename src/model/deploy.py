# Import libraries

import mlflow
import uuid

from azure.ai.ml.entities import ManagedOnlineEndpoint


# define functions
def main(args):
    # enable autologging
    mlflow.autolog()

    # Create a unique name for the endpoint
    online_endpoint_name = "credit-endpoint-" + str(uuid.uuid4())[:8]

    # define an online endpoint
    endpoint = ManagedOnlineEndpoint(
        name=online_endpoint_name,
        description="this is an online endpoint",
        auth_mode="key",
        tags={
            "training_dataset": "credit_defaults",
        },
    )

    # create the online endpoint
    # expect the endpoint to take approximately 2 minutes.
    endpoint = ml_client.online_endpoints.begin_create_or_update(endpoint).result()

    endpoint = ml_client.online_endpoints.get(name=online_endpoint_name)
    print(
        f'Endpoint "{endpoint.name}" with provisioning state "
        {endpoint.provisioning_state}" is retrieved'
    )


# run script
if __name__ == "__main__":
    # add space in logs
    print("\n\n")
    print("*" * 60)

    # run main function
    main()

    # add space in logs
    print("*" * 60)
    print("\n\n")
