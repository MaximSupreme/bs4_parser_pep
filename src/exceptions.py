class ParserFindTagException(Exception):
    """Вызывается, когда парсер не может найти тег."""
    pass


class VersionListNotFoundError(Exception):
    """Вызывается, когда парсер не может найти список версий Python в документации."""
    pass