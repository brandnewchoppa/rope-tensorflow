from setuptools import setup, find_packages

setup(
    name = 'rope-tensorflow',
    packages = find_packages(exclude = []),
    version = '0.0.1',
    license = 'MIT',
    description = 'RoPE - Enhanced Transformer with Rotary Position Embedding - TensorFlow',
    author = 'brandnewchoppa',
    author_email = '',
    long_description_content_type = 'text/markdown',
    url = 'https://github.com/brandnewchoppa/rope-tensorflow',
    keywords = [
        'artificial intelligence',
        'deep learning',
        'transformers',
        'positional encoding',
        'position embeddings'
    ],
    install_requires = [
        'tensorflow>=2.13.0'
    ],
    classifiers = [
        'Intended Audience :: Developers',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'License :: MIT License',
        'Programming Language :: Python :: 3.11'
    ]
)