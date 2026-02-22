# Contributing to Holidata

Thank you for considering contributing to Holidata!
This document outlines how you can help maintain and update holiday data.

## Maintaining Holiday Data

Help keep our holiday data accurate by:

1. Monitoring official government publications and legal documents
2. Identifying changes such as:
   - Newly established holidays
   - Abolished holidays
   - Date/observance rule changes
   - Regional observance pattern updates
   - Name/official designation changes

3. Verifying against primary sources (official government documents)
4. Updating relevant files in `src/holidata/holidays/`

## Updating Holidays

For guidance on how holidays are defined in the code, refer to [docs/how-tos/define-holidays.md](docs/how-tos/define-holidays.md).
This should help you when you want to make changes.

## Adding New Countries

If you want to add a new country to Holidata, please follow the detailed guide in [docs/how-tos/add-country.md](docs/how-tos/add-country.md).
Of course, we would be very happy if you could as well help to maintain this country afterward.

## Adding Languages

To add additional languages for a country, see [docs/how-tos/add-locales.md](docs/how-tos/add-locales.md).

## Submitting Your Contribution

Before you begin, make sure you have set up your development environment by following the instructions in [docs/how-tos/getting-started.md](docs/how-tos/getting-started.md).

Once you've made your changes, update the snapshot files such that they reflect the updated state of the data
```bash
pytest --snapshot-update
```

Before submitting a pull request, ensure that all code quality checks pass:

```bash
# Run linter and type checker
ruff check . && mypy src/
```

Finally, submit a pull request with a clear description of your changes and the sources you used for verification.

## Code Style and Best Practices

- Follow PEP 8 style guidelines (enforced by [ruff](https://docs.astral.sh/ruff/))
- Use type hints for all function signatures and variable declarations (checked by [mypy](https://mypy-lang.org/))
- Write clear, descriptive docstrings using Google-style format
- Keep your changes focused and well-documented

Thank you for helping to maintain accurate holiday data for Holidata!
