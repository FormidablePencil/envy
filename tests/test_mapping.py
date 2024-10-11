TEST_MAPPING = {
    # test in `py_cmd/<test_dir>` <test_dir> is either unit or integration test
    # Those files associated to unit and integration tests repectfully and the
    # whole path to the file is stored
    'py_cmd': {
        'main.py': {
            'unit': ['tests/unit/test_py.py'],
            'integration': ['tests/integration/test_py.py']
        }
    },
    # 'central_ai_manager/core.py': {
    #     'unit': 'tests/unit/test_central_ai_manager.py',
    #     'integration': 'tests/integration/test_central_ai_manager.py'
    # },
    # 'ai_components/code_generator.py': {
    #     'unit': 'tests/unit/test_code_generator.py',
    #     'integration': 'tests/integration/test_code_generator.py'
    # }
}