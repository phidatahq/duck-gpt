from typing import List, Optional

from pydantic import BaseSettings, validator


class ApiSettings(BaseSettings):
    """Api settings from container environment.

    Reference: https://pydantic-docs.helpmanual.io/usage/settings/
    """

    # Api title and version
    title: str = "Api"
    version: str = "1.0"

    # Api runtime derived from the `runtime` environment variable.
    # Valid values include "dev", "stg", "prd"
    runtime: str = "dev"

    # Api secret key derived from the `secret_key` environment variable.
    secret_key: Optional[str] = None

    # Set to False to disable docs server at /docs and /redoc
    docs_enabled: bool = True

    # Host and port to run the api server on.
    host: str = "0.0.0.0"
    port: int = 9090

    # Cors origin list to allow requests from.
    # This list is set using the set_cors_origin_list validator
    # which uses the runtime environment variable to set the
    # default cors origin list.
    cors_origin_list: Optional[List[str]] = None

    @validator("runtime")
    def validate_runtime(cls, runtime):
        valid_runtimes = ["dev", "stg", "prd"]
        if runtime not in valid_runtimes:
            raise ValueError(f"Invalid runtime: {runtime}")
        return runtime

    @validator("cors_origin_list", always=True)
    def set_cors_origin_list(cls, cors_origin_list, values):
        valid_cors = cors_origin_list or []

        runtime = values.get("runtime")
        if runtime == "dev":
            # 3000 is the default port for create-react-app
            valid_cors.extend(["http://localhost:3000"])

        return valid_cors


# Create ApiSettings object
api_settings = ApiSettings()
