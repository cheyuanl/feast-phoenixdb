from tests.integration.feature_repos.integration_test_repo_config import (
    IntegrationTestRepoConfig,
)

PHOENIXDB_CONFIG = {"type": "feast_phoenixdb_online_store.phoenixdb_online_store.PhoenixDBOnlineStore"}

FULL_REPO_CONFIGS = [
    IntegrationTestRepoConfig(online_store=PHOENIXDB_CONFIG),
]