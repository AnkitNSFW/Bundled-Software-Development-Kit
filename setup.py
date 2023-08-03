from setuptools import setup

setup(
    name='bsdk',
    version='0.1.0',
    description='The "bsdk" is a comprehensive meta-package that simplifies the setup of machine learning and data visualization environments. It bundles together a curated selection of essential Python libraries, making it easy for users to install all the required tools for their data analysis and machine learning projects with a single command.',
    author='Ankit Maurya',
    author_email='ankit141003@gmail.com',
    url='https://github.com/Ankit160402/Bundled-Software-Development-Kit',
    install_requires=[
        'tensorflow',
        'torch',
        'scikit-learn',
        'pandas',
        'numpy',
        'matplotlib',
        'seaborn',
        'xgboost',
        'lightgbm',
        'catboost',
        'keras',
        'statsmodels',
        'plotly',
        'bokeh',
        'scipy',
        'cv2',
    ],
)
