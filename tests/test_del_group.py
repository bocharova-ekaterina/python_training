from model.group import Group
import random
import allure

def test_del_group(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test1", header="test1", footer="test1"))
    with allure.step('Given a group list'):
        old_groups = db.get_group_list()
    group = random.choice(old_groups)
    with allure.step('When I delete a group %s to the list' % group):
        app.group.del_group_by_id(group.id)
    with allure.step('Then the new group list is less to the old list without the deleted group'):
        new_groups = db.get_group_list()
    assert len(old_groups) - 1 == app.group.count()
    old_groups.remove(group)
    assert old_groups==new_groups
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)
