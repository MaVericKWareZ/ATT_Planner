from att_planner.commons.utils.collections import deep_update
from att_planner.commons.utils.settings import get_settings_from_environment

deep_update(globals(), get_settings_from_environment(ENV_VAR_SETTINGS_PREFIX))  # type: ignore # noqa: F821
