from runner.configuration_dictionaries import DEFAULT_CFG, EXPERIMENTS_DICT


def create_configuration_dictionary(experiment_name, special_cfg):
    configuration_dictionary = DEFAULT_CFG
    experiment_dictionary = EXPERIMENTS_DICT[experiment_name]

    if not (experiment_dictionary.keys() <= configuration_dictionary.keys()):
        raise ValueError("experiment dictionary have keys that doesn't exist in the default dictionary")
    if not (special_cfg.keys() <= configuration_dictionary.keys()):
        raise ValueError("user defined dictionary have keys that doesn't exist in the default dictionary")

    configuration_dictionary.update(experiment_dictionary)
    configuration_dictionary.update(special_cfg)

    return configuration_dictionary



