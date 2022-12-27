from common.consts import EXPERIMENT_NAME, SPECIAL_CONFIGURATION
from runner.utils import create_configuration_dictionary


class Runner:
    def __init__(self, user_cfg):
        experiment_name = user_cfg[EXPERIMENT_NAME]
        special_cfg = user_cfg[SPECIAL_CONFIGURATION]
        self.configurations = create_configuration_dictionary(experiment_name, special_cfg)

    def run(self):
        pass