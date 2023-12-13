import os
import json
import datetime

import httpx
from sqlalchemy import create_engine, text
from sqlalchemy.orm import Session

from config import load
from models.model import ArtifactStorage


def get_artifactory_storage_info() -> list[dict[str, str]]:
    artifactory_url = f"{CONFIG.ARTIFACTORY_URL}/artifactory/api/storageinfo"
    headers = {
        "Accept": "application/json",
        "Authorization": f"Bearer {CONFIG.ARTIFACTORY_TOKEN}",
    }

    response = httpx.get(artifactory_url, headers=headers, verify=False, timeout=20.0)
    if response.status_code != 200:
        raise Exception(f"Failed to get Artifactory storage info: {response.status_code} {response.text}")

    storage_info_raw = json.loads(response.content)

    current_timestamp = datetime.datetime.now()
    storage_info = [
    {
        "repo_key": x.get("repoKey"),
        "repo_type": x.get("repoType"),
        "used_space": x.get("usedSpace"),
        "package_type": x.get("packageType"),
        "folders_count": x.get("foldersCount"),
        "files_count": x.get("filesCount"),
        "free_space_percentage": x.get("percentage"),
        "date_added": current_timestamp,
    } for x in storage_info_raw['repositoriesSummaryList']]
    
    print(storage_info)
    return storage_info


def save_to_db(repo_list: list[dict[str, str]]=None) -> None:
    engine = create_engine(f"postgresql://{CONFIG.POSTGRESQL_URI}", connect_args={'connect_timeout': 20})
    # with Session(engine) as session:
    #     print(session.query(ArtifactStorage).all())

    #     artifact = ArtifactStorage(
    #         repo_key="mion-mgw-maven-snapshots",
    #         repo_type="LOCAL",
    #         used_space="76.26 GB",
    #         package_type="Maven",
    #         folders_count=6191,
    #         files_count=70629,
    #         free_space_percentage="28.64%",
    #         date_added=datetime.datetime.now(),
    #     )
    #     session.add_all([artifact])
    #     session.commit()
    
    with engine.begin() as con:
        query = con.execute(text("select * from services_artifact_storage"))
        print(query.keys())
        print([q for q in query])


if __name__ == "__main__":
    CONFIG = load()
    # get_artifactory_storage_info()
    save_to_db()
