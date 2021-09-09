from uvicorn.workers import UvicornWorker


class OpenPantheonUvicornWorker(UvicornWorker):
    """
    Add proxy headers to avoid issues with Uvicorn adding a `location` header
    pointing to the http endpoint
    """
    CONFIG_KWARGS = {"proxy_headers": True, "forwarded_allow_ips": "*"}
