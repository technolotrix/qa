import requests
import nose


class TestApi():

    def setUp(self):
        self.baseurl = 'http://nicolesmith.nyc'
        #self.baseurl = 'http://127.0.0.1:4747'
        
    def tearDown(self):
        pass

    def test_home(self):

        url = self.baseurl + '/'

        for n in range(1000):
            # GET
            get = requests.get(url)
            assert get.status_code == 200
            # POST
            post = requests.post(url, data={})
            assert post.status_code == 405
            # PUT
            put = requests.put(url, data={})
            assert put.status_code == 405
            # DELETE
            delete = requests.delete(url, data={})
            assert delete.status_code == 405

    def test_about(self):

        url = self.baseurl + '/about'
        # GET
        for n in range(1000):
            get = requests.get(url)
            assert get.status_code == 200
            # POST
            post = requests.post(url, data={})
            assert post.status_code == 405
            # PUT
            put = requests.put(url, data={})
            assert put.status_code == 405
            # DELETE
            delete = requests.delete(url, data={})
            assert delete.status_code == 405

    def test_projects(self):

        url = self.baseurl + '/projects'
        # GET
        for n in range(1000):
            get = requests.get(url)
            assert get.status_code == 200
            # POST
            post = requests.post(url, data={})
            assert post.status_code == 405
            # PUT
            put = requests.put(url, data={})
            assert put.status_code == 405
            # DELETE
            delete = requests.delete(url, data={})
            assert delete.status_code == 405

    def test_services(self):

        url = self.baseurl + '/services'
        # GET
        for n in range(1000):
            get = requests.get(url)
            assert get.status_code == 200
            # POST
            post = requests.post(url, data={})
            assert post.status_code == 405
            # PUT
            put = requests.put(url, data={})
            assert put.status_code == 405
            # DELETE
            delete = requests.delete(url, data={})
            assert delete.status_code == 405

    def test_contact(self):

        url = self.baseurl + '/contact'
        # GET
        for n in range(1000):
            get = requests.get(url)
            assert get.status_code == 200
            # POST
            post = requests.post(url, data={})
            assert post.status_code == 405
            # PUT
            put = requests.put(url, data={})
            assert put.status_code == 405
            # DELETE
            delete = requests.delete(url, data={})
            assert delete.status_code == 405