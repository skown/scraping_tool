import unittest
from unittest.mock import patch, MagicMock
from main import Post_mobile_data2


class TestPostMobileData(unittest.TestCase):

    @patch('main.client')
    def test_post_mobile_data2(self, mock_client):
        # Setup the mock to return a response when called
        mock_response = MagicMock()
        mock_client.post.return_value = mock_response

        # Call the function with some test data
        keywords = "who is napoleon bonaparte"
        Post_mobile_data2(keywords)

        # Check that the function called client.post with the correct arguments
        expected_post_data = {
            0: {
                'language_code': "en-US",
                'location_code': 2840,
                'device': 'mobile',
                'keyword': keywords
            }
        }
        mock_client.post.assert_called_once_with("/v3/serp/google/organic/task_post", expected_post_data)

        # Check that the function cleared the post_data dict
        self.assertEqual(len(post_data), 0)  # post_data should be empty

if __name__ == '__main__':
    unittest.main()
