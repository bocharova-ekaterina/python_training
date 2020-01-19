from model.group import Group
import random


def test_edit_some_group(app, db, check_ui):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="test1", header="test1", footer="test1"))
    old_groups = db.get_group_list()
    group_random = random.choice(old_groups)
    group = Group(name="New group")
    app.group.edit_group_by_id(group_random.id, group)
    assert len(old_groups) == app.group.count()
    new_groups = db.get_group_list()
    assert old_groups == new_groups
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)

