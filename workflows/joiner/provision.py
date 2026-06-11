import requests
import yaml
import logging

logger = logging.getLogger(__name__)

def provision_new_hire(employee_id: str, config: dict) -> dict:
    """
    Provision access for a new hire based on role and department.
    Triggered by Workday hire event via webhook.
    """
    saviynt_url = config["saviynt"]["base_url"]
    token = get_saviynt_token(config)

    payload = {
        "username": employee_id,
        "usertype": "Employee",
        "provisioningTrigger": "JOINER",
        "attributes": {
            "department": config.get("department"),
            "jobTitle": config.get("job_title"),
            "manager": config.get("manager_id")
        }
    }

    response = requests.post(
        f"{saviynt_url}/ECM/api/v5/user/createUser",
        headers={"Authorization": f"Bearer {token}"},
        json=payload
    )
    response.raise_for_status()
    logger.info(f"Provisioned user {employee_id}: {response.status_code}")
    return response.json()

def get_saviynt_token(config: dict) -> str:
    r = requests.post(
        f"{config['saviynt']['base_url']}/ECM/api/login",
        json={"username": config["saviynt"]["username"],
              "password": config["saviynt"]["password"]}
    )
    return r.json().get("access_token")
