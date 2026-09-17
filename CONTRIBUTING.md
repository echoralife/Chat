# Contributing

Neural Lab favors small, inspectable experiments.

## Development

```bash
python -m unittest discover -s tests -v
```

New modules should remain dependency-light unless an experiment specifically requires an external package. Prefer deterministic examples and tests that do not require API credentials.

## Commit style

Use focused commits with conventional prefixes where practical:

- `feat:` new behavior
- `fix:` bug fixes
- `test:` test coverage
- `docs:` documentation
- `bench:` benchmarks
- `refactor:` internal restructuring
- `chore:` repository maintenance

## Experiment checklist

A useful experiment should state the behavior being explored, expose the important logic, include a runnable example, and provide at least one measurable outcome when appropriate.
