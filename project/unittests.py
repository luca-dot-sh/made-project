from unittest import TestCase,mock
import pipeline
import pandas as pd 
import datetime

class Tests(TestCase):
    def test_datasets_not_empty(self):
        self.assertTrue(len(pipeline.datasets)>0)

    @mock.patch('urllib.request.urlretrieve')
    @mock.patch('os.path.exists',return_value = False)
    def test_download_calls_urlretrieve(self, mocked_os_path_exists,mocked_urlretrieve):
        pipeline.download_datasets()
        mocked_os_path_exists.assert_called()
        mocked_urlretrieve.assert_called()
    

    @mock.patch('urllib.request.urlretrieve')
    @mock.patch('os.path.exists',return_value = True)
    def test_dont_download_if_exists(self, mocked_os_path_exists, mocked_urlretrieve):
        pipeline.download_datasets()
        mocked_os_path_exists.assert_called()
        mocked_urlretrieve.assert_not_called()
    
    
    @mock.patch('zipfile.ZipFile.extract')
    @mock.patch('pipeline.datasets', return_value = {"test":"test"})
    def test_only_unzip_dwd_data(self,mocked_datasets, mocked_extract):
        pipeline.unzip_dwd_data()
        mocked_extract.assert_not_called()

    def test_dataset_too_with_new_data(self):
        test_df = pd.DataFrame({"created_time":[datetime.datetime(2025,1,1)]})
        self.assertTrue(pipeline.dataset_too_new(test_df))
    
    def test_translate_yes_no(self):
        ja = ["ja","Ja","jA","JA"]
        nein =["nein","Nein","NEIN"]
        for item in ja:
            self.assertTrue(pipeline.translate_yes_no(item)=="yes")
        for item in nein:
            self.assertTrue(pipeline.translate_yes_no(item)=="no")