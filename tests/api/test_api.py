import requests
import nose


class TestApi():

    def setUp(self):
    	self.baseurl = 'http://nicolesmith.nyc'
        
    def tearDown(self):
    	pass

    def test_home(self):

    	url = self.baseurl + '/'
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

    def test_google(self):

        url = self.baseurl + '/google9561f99e9bf3af0a.html'
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

    def test_sitemap(self):

        url = self.baseurl + '/sitemap.xml'
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

    def test_robots(self):

        url = self.baseurl + '/robots.txt'
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