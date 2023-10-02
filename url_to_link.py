def get_url_text(url):
    if "github" or "codepen" in url:
        return "Source Code"
    else:
        return "Link"
