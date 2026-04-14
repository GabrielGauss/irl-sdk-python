---
name: Bug report
about: Report a reproducible bug in the IRL Python SDK
title: "[BUG] "
labels: bug
assignees: ''
---

## Describe the bug

A clear and concise description of what the bug is.

## To reproduce

```python
# Minimal reproducer
from irl_sdk import IRLClient
async with IRLClient(base_url="…", api_token="…") as client:
    result = await client.authorize(…)
```

## Expected behavior

## Actual behavior

Include the full traceback if applicable.

## Environment

- SDK version: `pip show irl-sdk`
- Python version: `python --version`
- IRL Engine version: `v?`

## Additional context
