# CS336 Spring 2025 Assignment 1: Basics

For a full description of the assignment, see the assignment handout at
[cs336_spring2025_assignment1_basics.pdf](./cs336_spring2025_assignment1_basics.pdf)

If you see any issues with the assignment handout or code, please feel free to
raise a GitHub issue or open a pull request with a fix.

## Setup

### Environment
We manage our environments with `uv` to ensure reproducibility, portability, and ease of use.
Install `uv` [here](https://github.com/astral-sh/uv) (recommended), or run `pip install uv`/`brew install uv`.
We recommend reading a bit about managing projects in `uv` [here](https://docs.astral.sh/uv/guides/projects/#managing-dependencies) (you will not regret it!).

You can now run any code in the repo using
```sh
uv run <python_file_path>
```
and the environment will be automatically solved and activated when necessary.

### Run unit tests


```sh
uv run pytest
```

Initially, all tests should fail with `NotImplementedError`s.
To connect your implementation to the tests, complete the
functions in [./tests/adapters.py](./tests/adapters.py).

### Download data
Download the TinyStories data and a subsample of OpenWebText

``` sh
mkdir -p data
cd data

wget https://huggingface.co/datasets/roneneldan/TinyStories/resolve/main/TinyStoriesV2-GPT4-train.txt
wget https://huggingface.co/datasets/roneneldan/TinyStories/resolve/main/TinyStoriesV2-GPT4-valid.txt

wget https://huggingface.co/datasets/stanford-cs336/owt-sample/resolve/main/owt_train.txt.gz
gunzip owt_train.txt.gz
wget https://huggingface.co/datasets/stanford-cs336/owt-sample/resolve/main/owt_valid.txt.gz
gunzip owt_valid.txt.gz

cd ..
```

## BPE Implementation
See full implementation run_train_bpe() function under /tests/adapeters.py file. And Run this code to test: ```uv run pytest tests/test_train_bpe.py```
 - Step 1: In find_chunk_boundaries(), we initially split all texts into few chunks:
   - Step 1.1: first we need to make sure all tokens in split_special_tokens are byte type
   - step 1.2: let's calculate the size of file
   - step 1.3: split the file by num_chunk. target_chunk_size is the number of chunks
   - step 1.4: chunk_boundaries: Inital boundaries, not the ultimite one. Make sure the last element in chunk_boundaries is equal to the file size
   - step 1.5: we set mini_chunk_size = 4096, which is the mini chunk size we want to read. At this stage, we update chunk_boundaries according special tokens locations.
     - There are two breaks: the first break is when you reach the end of file. The second break is when you find there are special token(s) within range mini_chunk_size = 4096.
     - If you find special token(s) then accumulate current boundary with the minimum position (min_pos) — the earliest token found.
     - However, if you donot find any special token within the range, then read next 4KB.
- Step 2: Processing each chunks with parellel function to speedup
    - Decode and tokenize: Decode bytes with utf-8 and errors='ignore' (acknowledge that some split code points may be dropped).
    tokenize_chunk(chunk, special_tokens_as_str) must:
        - Build a regex alternation of escaped special tokens (longest first) to keep them intact.
        - Split into sub-chunks; preserve special tokens verbatim; non-special substrings are fed to gpt2_pre_tokenize.
    - Count frequencies
- Step 3: Initializing all data structures we need
- Step 4: updating and merging
    - After merging, delete old pairs and add new pairs