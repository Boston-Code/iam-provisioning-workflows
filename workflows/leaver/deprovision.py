import requests
import logging
from datetime import datetime

logger = logging.getLogger(__name__)

def deprovision_user(employee_id: str, termination_date: str, config: dict) -> dict:
    """
    Revoke all access for a terminated employee.
    Triggered by Workday termination event.
    """
    token = get_saviynt_token(config)
    base_url = config["saviynt"]["base_url"]

    # Disable account immediately
    disable_payload = {
        "username": employee_id,
        "statuskey": "Inactive",
        "comments": f"Leaver workflow triggered — termination date {termination_date}"
    }
    r = requests.post(
        f"{base_url}/ECM/api/v5/user/updateUser",
        headers={"Authorization": f"Bearer {token}"},
        json=disable_payload
    )
    r.raise_for_status()
    logger.info(f"Disabled account for {employee_id}")
    return {"status": "deprovisioned", "timestamp": datetime.utcnow().isoformat()}
