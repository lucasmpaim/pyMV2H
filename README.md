# pyMV2H

A pure-python implementation of MV2H metric, the original repo can be found [here](https://github.com/apmcleod/MV2H).

For a more easily use with python frameworks, like PyTorch and Tensorflow we implement this repo.


# Usage

Using by shell:

```shell
pyMV2H
Usage:
  pyMV2H hello
  pyMV2H midi_converter -i <input_dir> -o <output_dir>
  pyMV2H -h | --help
  pyMV2H --version
Options:
  -h --help                         Show this screen.
  --version                         Show version.
  -i --input                        The input file
  -o --output                       The output file
Examples:
  pyMV2H hello
Help:
  For help using this tool, please open an issue on the Github repository:
  https://github.com/lucasmpaim/pyMV2H
```

Using by python code:

```python
from pyMV2H.metrics import f1
f1.f1_score(0, 0, 0)
```

# Citation
Please, cite the original article:


```bibtex
@inproceedings{McLeod:18a,
  title={Evaluating automatic polyphonic music transcription},
  author={McLeod, Andrew and Steedman, Mark},
  booktitle={International Society for Music Information Retrieval Conference (ISMIR)},
  year={2018},
  pages={42--49}
}
```

# Important
For convenience at this point, python version doesn't include support for multi-tempo


## Next Step's

- [ ] Support for multi-tempo

- [ ] Reduce the number of dependencies

- [ ] Write unit tests
