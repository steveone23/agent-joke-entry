# agent-joke-entry

Entry for the make.fun bounty "Make the AI judge laugh" (ai-joke-03): `main.py` writes one joke about AI coding agents to `entry.txt`.
The output directory is `MAKEFUN_OUTPUT_DIR` when set, otherwise `/output`. Python 3.13, standard library only, no network.
Run it locally with `mkdir -p out && MAKEFUN_OUTPUT_DIR=out python main.py`, then read `out/entry.txt`.
