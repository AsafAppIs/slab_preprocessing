from common.consts import SOA_EXPERIMENT, EXPERIMENT_NAME, INPUT_DIR, OUTPUT_DIR, SPECIAL_CONFIGURATION
from runner.runner_class import Runner

configuration_dict = {
    EXPERIMENT_NAME: SOA_EXPERIMENT,
    INPUT_DIR: 'some path',
    OUTPUT_DIR: 'some path',
    SPECIAL_CONFIGURATION: {

    },
}

if __name__ == '__main__':
    runner = Runner(configuration_dict)
    runner.run()
