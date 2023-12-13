import os
import dataclasses

from dotenv import load_dotenv


load_dotenv()

@dataclasses.dataclass
class Config:
    ARTIFACTORY_URL: str | None
    ARTIFACTORY_TOKEN: str | None
    POSTGRESQL_URI: str | None


def load() -> Config:
    return Config(
        ARTIFACTORY_URL=os.getenv("ARTIFACTORY_URL"),
        ARTIFACTORY_TOKEN=os.getenv("ARTIFACTORY_TOKEN"),
        POSTGRESQL_URI=os.getenv("POSTGRESQL_URI"),
    )
