import setuptools


with open("README.md", "r") as fh:

    long_description = fh.read()


REQUIRED_PACKAGES = [
    # 'tensorflow>=1.4.0,<=1.12.0',
    'gensim==3.6.0',
    'networkx==2.1',
    'joblib==0.13.0',
    'scikit-learn',
    'numpy'
    `tensorflow`

]


setuptools.setup(

    name="ge",

    version="0.0.0",

    author="Weichen Shen",

    author_email="wcshen1994@163.com",

    url="https://github.com/shenweichen/GraphEmbedding",

    packages=setuptools.find_packages(exclude=[]),

    python_requires='>=3.4',  # 3.4.6

    install_requires=REQUIRED_PACKAGES,

    extras_require={

        "tf": ['tensorflow>=1.4.0,!=1.7.*,!=1.8.*'],

        "tf_gpu": ['tensorflow-gpu>=1.4.0,!=1.7.*,!=1.8.*'],

    },

    entry_points={

    },
    license="MIT license",


)
