# RoPE - TensorFlow
RoPE (TensorFlow implementation) from the paper [Transformer Quality in Linear Time](https://arxiv.org/pdf/2202.10447.pdf).

Based on the original work of paper [Enhanced Transformer with Rotary Position Embedding](https://arxiv.org/pdf/2104.09864.pdf).

> [!WARNING]
> This repository is under developemnt, but please feel free to explore and provide any feedback or suggestions you may have. :construction:

## Usage

```python
import tensorflow as tf
from rope_tensorflow import RoPE

rotary_emb = RoPE(dim = 32)

q = tf.random.normal([1, 128, 64])
k = tf.random.normal([1, 128, 64])

q = rotary_emb.rotate(q)
k = rotary_emb.rotate(k)
```

### Length-Extrapolatable
Introduced in [A Length-Extrapolatable Transformer](https://arxiv.org/pdf/2212.10554.pdf) paper.

```python
import tensorflow as tf
from rope_tensorflow import RoPE

rotary_emb = RoPE(dim = 32)

q = tf.random.normal([1, 128, 64])
k = tf.random.normal([1, 128, 64])

q, k = rotary_emb.rotate([q, k])
```

### Interpolating Sequence Positions
Introduced in [Position Interpolation](https://arxiv.org/pdf/2306.15595.pdf) paper.

```python
import tensorflow as tf
from rope_tensorflow import RoPE

rotary_emb = RoPE(dim = 32, interpolate_factor = 2.0)
```

## Citations

```bibtex
@article{Hua2022TransformerQI,
    title   = {Transformer Quality in Linear Time},
    author  = {Weizhe Hua and Zihang Dai and Hanxiao Liu and Quoc V. Le},
    journal = {ArXiv},
    year    = {2022},
    volume  = {abs/2202.10447}
}
```

```bibtex
@misc{Su2021RoFormer,
    title   = {RoFormer: Enhanced Transformer with Rotary Position Embedding}, 
    author  = {Jianlin Su and Yu Lu and Shengfeng Pan and Bo Wen and Yunfeng Liu},
    journal = {ArXiv},
    year    = {2021},
    volume  = {abs/2104.09864}
}
```

```bibtex
@misc{rope-eleutherai,
  title = {Rotary Embeddings: A Relative Revolution},
  author = {Biderman, Stella and Black, Sid and Foster, Charles and Gao, Leo and Hallahan, Eric and He, Horace and Wang, Ben and Wang, Phil},
  howpublished = \url{blog.eleuther.ai/},
  note = {[Online; accessed ]},
  year = {2021}
}
```
