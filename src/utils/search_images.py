# image_search.py
from fastcore.all import L
from duckduckgo_search import DDGS
from exponential_backoff import exponential_backoff

def search_images(
    term: str,
    max_images: int = 200,
    retries: int = 3,
    initial_delay: float = 2,
    backoff_factor: float = 2,
    max_delay: float = 32,
    jitter_factor: float = 0.3,
    proxy: str = "socks5://127.0.0.1:9050"
) -> list:
    """
    Search images using DuckDuckGo with exponential backoff retry logic.

    Args:
        term (str): Search term.
        max_images (int): Maximum number of images to retrieve. Default is 200.
        retries (int): Maximum number of retries. Default is 3.
        initial_delay (float): Initial delay in seconds. Default is 2.
        backoff_factor (float): Factor by which delay increases. Default is 2.
        max_delay (float): Maximum delay in seconds. Default is 32.
        jitter_factor (float): Jitter range (0.3 = ±30%). Default is 0.3.
        proxy (str): Proxy to use for the search. Default is "socks5://127.0.0.1:9050".

    Returns:
        list: List of image results.
    """
    def _search():
        with DDGS(proxy=proxy) as ddgs:
            return L(ddgs.images(keywords=term, max_results=max_images)).itemgot('image')

    return exponential_backoff(
        _search,
        retries=retries,
        initial_delay=initial_delay,
        backoff_factor=backoff_factor,
        max_delay=max_delay,
        jitter_factor=jitter_factor
    )