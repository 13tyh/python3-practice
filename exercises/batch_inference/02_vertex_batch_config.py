"""Vertex AI / Gemini バッチ推論の設定練習。"""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class BatchJobConfig:
    project: str
    location: str
    model: str
    job_display_name: str
    input_uri: str
    output_uri: str
    instances_format: str = "jsonl"
    predictions_format: str = "jsonl"


def validate_gcs_uri(uri: str) -> bool:
    """gs:// で始まる URI なら True。"""
    # TODO
    raise NotImplementedError


def build_job_display_name(prefix: str, date_text: str) -> str:
    """例: review-batch-20260607。"""
    # TODO
    raise NotImplementedError


def validate_batch_config(config: BatchJobConfig) -> list[str]:
    """不足や不正をエラーメッセージで返す。"""
    # TODO
    raise NotImplementedError


def to_vertex_batch_predict_kwargs(config: BatchJobConfig) -> dict[str, object]:
    """aiplatform.Model.batch_predict に渡す kwargs を作る。"""
    # TODO
    raise NotImplementedError
