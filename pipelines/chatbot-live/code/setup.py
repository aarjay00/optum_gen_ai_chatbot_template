from setuptools import setup, find_packages
setup(
    name = 'chatbot-live',
    version = '1.0',
    packages = find_packages(include = ('chatbotlive*', )) + ['prophecy_config_instances'],
    package_dir = {'prophecy_config_instances' : 'configs/resources/config'},
    package_data = {'prophecy_config_instances' : ['*.json', '*.py', '*.conf']},
    description = 'workflow',
    install_requires = [
'prophecy-spark-ai==0.1.8', 'prophecy-libs==1.6.7'],
    entry_points = {
'console_scripts' : [
'main = chatbotlive.pipeline:main'], },
    data_files = [(".prophecy", [".prophecy/workflow.latest.json"])],
    extras_require = {
'test' : ['pytest', 'pytest-html'], }
)
