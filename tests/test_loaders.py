from cosmographi_datasets.loaders import load_rubin_throughput


def test_load_rubin_throughput(extract_data):
    data_path = extract_data("throughput/rubin/transmissions")
    res = load_rubin_throughput(data_path)
    assert res is not None
    assert len(res["bands"]) == 6
