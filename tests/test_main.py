from portnovapi import PortnovAPI
import json
from assertpy.assertpy import assert_that


with open("package.json") as file:
    data = json.load(file)
    connection = PortnovAPI(data["base_url"])


def test_first_login():
    x = connection.request_token(data["login_ep"], data["data"])
    assert_that(x).is_true()


def test_create_new_candidate():
    assert_that(connection.create_new_candidate(data["candidates_ep"], data["candidate"])).is_true()


def test_request_token():
    assert_that(connection.request_token(data["login_ep"], data["new_candidate_data"])).is_true()


def test_create_new_position():
    assert_that(connection.create_new_position(data["positions_ep"], data["position_data"])).is_true()


def test_get_pos_by_id():
    position = connection.get_position_by_id(data["positions_ep"], connection.company_id)
    assert_that(position).is_not_none()


def test_update_pos():
    position = connection.update_position_by_id(data["positions_ep"], connection.company_id, data["position_new_data"])
    assert_that(position).is_not_none()


def test_delete_pos():
    assert_that(connection.delete(data["positions_ep"], connection.company_id)).is_true()


def test_delete_cand():
    assert_that(connection.delete(data["candidates_ep"], connection.candidate_id)).is_true()


def test_return_all_positions():
    all_positions = connection.return_all(data["positions_ep"])
    assert_that(all_positions).is_not_none()


def test_return_all_candidates():
    all_candidates = connection.return_all(data["candidates_ep"])
    assert_that(all_candidates).is_not_none()
