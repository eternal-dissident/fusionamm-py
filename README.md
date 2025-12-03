# fusionamm-py
FusionAMM Python Client.

THIS IS AN INDEPENDENT CONTRIBUTION. AUTHOR IS **NOT** AFFILIATED WITH NEITHER [DefiTuna](https://defituna.com/) OR [FusionAMM](https://fusionamm.com)

# About
`fusionamm` client contained in this repository can be used to interact with FusionAMM on Solana and to parse transactions for analytics. [`ingest_parse.ipynb`](https://github.com/eternal-dissident/fusionamm-py/blob/main/ingest_parse.ipynb) contains an example of backfilling and parsing FusionAMM instructions.

# Setup
This repo was built with [`uv`](https://github.com/astral-sh/uv). To set up dependencies run `uv sync` after cloning the repo. If not using `uv`, all dependencies are listed in `pyproject.toml`.

You will need an `.env` file with `RPC_URL` to run sample notebook.