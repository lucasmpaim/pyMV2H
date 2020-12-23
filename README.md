# pyMV2H

A pure-python implementation of MV2H metric, the original repo can be found [here](https://github.com/apmcleod/MV2H).

For a more easily use with python frameworks, like PyTorch and Tensorflow we implement this repo.


# Usage

Using by shell:

```shell
pyMV2H
Usage:
  pyMV2H midi_converter -i <input_dir> -o <output_dir>
  pyMV2H compare_files -g <reference_file> -t <transcription_file> [-a]
  pyMV2H -h | --help
  pyMV2H --version
Options:
  -h --help                         Show this screen.
  --version                         Show version.
  -o --output                       The output file
  -t                                The transcription file
  -g                                The reference file
  -a                                Align both files
Examples:
  pyMV2H hello
Help:
  For help using this tool, please open an issue on the Github repository:
  https://github.com/lucasmpaim/pyMV2H
```

Using by python code:

```python
from pyMV2H.utils.music import Music
from pyMV2H.metrics.mv2h import mv2h

reference_file = Music.from_file('<reference_file_dir>')
transcription_file = Music.from_file('<transcription_file_dir>')

print(mv2h(reference_file, transcription_file))
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
For convenience at this point, python version doesn't include support for multi-tempo or chords, this repo is implemented for MIDI AMT's algorithms research, and the original repo doesn't extract this info from MIDI files. [ref.](https://github.com/apmcleod/MV2H/blame/master/README.md#L63)


## Next Step's

- [ ] Support for multi-tempo

- [ ] Reduce the number of dependencies

- [ ] Add support to chords

- [ ] MusicXML parser

- [ ] Write unit tests

- [ ] Refactor code to be more pythonic
