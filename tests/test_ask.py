import app.ask as ask_module


def test_ask_prints_input_and_output_tokens(monkeypatch, capsys):
    class FakeUsage:
        prompt_token_count = 123
        candidates_token_count = 45

    class FakeResponse:
        text = "返答"
        usage_metadata = FakeUsage()

    class FakeModels:
        def generate_content(self, model, contents):
            assert model == ask_module.MODEL
            assert contents == "質問文"
            return FakeResponse()

    class FakeClient:
        def __init__(self, api_key):
            self.api_key = api_key
            self.models = FakeModels()

    monkeypatch.setattr(ask_module.genai, "Client", lambda api_key: FakeClient(api_key))
    monkeypatch.setattr(ask_module, "get_api_key", lambda: "dummy-key")

    result = ask_module.ask("質問文")

    assert result == "返答"
    captured = capsys.readouterr().out
    assert "[input tokens] 123" in captured
    assert "[output tokens] 45" in captured
