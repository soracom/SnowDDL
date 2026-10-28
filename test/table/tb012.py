def test_step1(helper):
    # Explicitly enabled on CREATE TABLE
    table = helper.show_table("db1", "sc1", "tb012_tb1")
    assert table["error_logging"] == "ON"

    table = helper.show_table("db1", "sc1", "tb012_tb2")
    assert table["error_logging"] == "ON"

    # Explicitly disabled on CREATE TABLE
    table = helper.show_table("db1", "sc1", "tb012_tb3")
    assert table["error_logging"] == "OFF"


def test_step2(helper):
    # Parameter was removed from config, existing value must be preserved
    table = helper.show_table("db1", "sc1", "tb012_tb1")
    assert table["error_logging"] == "ON"

    # Table was re-created due to NUMBER scale change, error logging must survive REPLACE
    table = helper.show_table("db1", "sc1", "tb012_tb2")
    cols = helper.desc_table("db1", "sc1", "tb012_tb2")

    assert cols["ID"]["type"] == "NUMBER(10,2)"
    assert table["error_logging"] == "ON"

    table = helper.show_table("db1", "sc1", "tb012_tb3")
    assert table["error_logging"] == "OFF"


def test_step3(helper):
    # Explicitly disabled
    table = helper.show_table("db1", "sc1", "tb012_tb1")
    assert table["error_logging"] == "OFF"

    # No changes
    table = helper.show_table("db1", "sc1", "tb012_tb2")
    assert table["error_logging"] == "ON"

    table = helper.show_table("db1", "sc1", "tb012_tb3")
    assert table["error_logging"] == "OFF"
