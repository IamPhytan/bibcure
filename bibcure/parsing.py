import bibtexparser

_MONTHS = (
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
)

_MONTH_ALIASES = {
    alias: month for month in _MONTHS for alias in (month.lower(), month[:3].lower())
}
_MONTH_ALIASES["sept"] = "September"

_MONTH_STRINGS = "\n".join(
    f'@string{{{alias} = "{month}"}}' for alias, month in _MONTH_ALIASES.items()
)


def loads_bibtex(text):
    """Lit du BibTeX en reconnaissant les noms et abréviations des mois."""
    return bibtexparser.loads(_MONTH_STRINGS + "\n" + text)
