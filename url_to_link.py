def get_url_text(url):
    if "github" in url or "codepen" in url:
        return "Source Code"
    else:
        return "Link"
