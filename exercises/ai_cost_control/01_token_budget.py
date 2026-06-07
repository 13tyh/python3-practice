"""AI利用時のtoken budgetを考える練習。"""

MODEL_LIMITS = {
    "gemini-2.5-flash": 8192,
    "gemini-2.5-pro": 32768,
}


def estimate_tokens(text: str) -> int:
    """ざっくり4文字で1tokenとして、最低1tokenで見積もる。"""
    # TODO
    raise NotImplementedError


def fits_budget(prompt: str, max_output_tokens: int, model_name: str) -> bool:
    """prompt見積もりと出力上限がmodel limit内ならTrue。"""
    # TODO
    raise NotImplementedError


def choose_model(prompt: str, deployment_to_model: dict[str, str]) -> str:
    """短いpromptはfast、長いpromptはlarge deploymentを選ぶ。"""
    # TODO
    raise NotImplementedError
