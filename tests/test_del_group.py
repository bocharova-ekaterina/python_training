from model.group import Group


def test_del_first_group(app):
    if app.group.count == 0:
        app.group.create(Group(name="test1", header="test1", footer="test1"))
    app.group.del_first_group()
