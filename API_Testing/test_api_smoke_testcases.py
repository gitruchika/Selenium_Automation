from api_method_call import APICall
from api_test_data import *


class TestAPIUseCase:

    def test_get_all_user(self):
        api_call = APICall(api_path=list_users_api_call)
        rep_data = api_call.get_api_call()
        assert rep_data.status_code == 200
        assert len(rep_data.json()['data']) == 6

    def test_create_new_user(self):
        api_call = APICall(api_path=create_user_api)
        rep_data = api_call.post_api_call(request_data=create_user_info)
        print(rep_data)
        assert rep_data.status_code == 200

    def test_update_information_with_put(self):
        api_call = APICall(api_path=put_api_uri)
        res_data = api_call.put_api_call(request_data=put_request_data)
        print(res_data.json())
        assert res_data.status_code == 200

    def test_update_information_with_patch(self):
        api_call = APICall(api_path=put_api_uri)
        res_data = api_call.patch_api_call(request_data=patch_request_data)
        print(res_data.json())
        assert res_data.status_code == 200

    def test_delete_information(self):
        api_call = APICall(api_path=delete_api_uri)
        res_data = api_call.delete_api_call()
        assert res_data.status_code == 204



