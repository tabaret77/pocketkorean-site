"""Kept for the Cloudflare Pages build command (python3 tools/blog.py). The builder is now tools/articles.py."""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
import articles
if __name__ == '__main__':
    articles.build()
