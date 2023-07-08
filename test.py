import unittest
import pandas as pd
import requests
import os


class TestCSVData(unittest.TestCase):
    def setUp(self):
        self.df = pd.read_csv('data/data.csv', sep=';')

    def test_unique_images(self):
        images = self.df['image']
        self.assertEqual(len(images), len(set(images)), "Not all images are unique")

    def test_unique_urls(self):
        urls = self.df['url']
        self.assertEqual(len(urls), len(set(urls)), "Not all URLs are unique")

    def test_urls_not_404(self):
        for url in self.df['url']:
            response = requests.get(url)
            self.assertNotEqual(response.status_code, 404, f"URL {url} returned a 404")

    def test_images_exist(self):
        for image in self.df['image']:
            self.assertTrue(os.path.exists('images/' + image), f"Image {image} does not exist")


if __name__ == "__main__":
    unittest.main()
