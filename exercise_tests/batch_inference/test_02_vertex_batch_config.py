from importlib import import_module

target = import_module("exercises.batch_inference.02_vertex_batch_config")


def test_validate_gcs_uri() -> None:
    assert target.validate_gcs_uri("gs://bucket/input.jsonl")
    assert not target.validate_gcs_uri("s3://bucket/input.jsonl")


def test_build_job_display_name() -> None:
    assert target.build_job_display_name("review batch", "20260607") == "review-batch-20260607"


def test_validate_batch_config() -> None:
    config = target.BatchJobConfig("", "global", "gemini-2.5-flash", "", "input", "output")
    assert target.validate_batch_config(config) == [
        "project is required",
        "job_display_name is required",
        "input_uri must start with gs://",
        "output_uri must start with gs://",
    ]


def test_to_vertex_batch_predict_kwargs() -> None:
    config = target.BatchJobConfig(
        project="demo",
        location="us-central1",
        model="projects/demo/locations/us-central1/models/123",
        job_display_name="job",
        input_uri="gs://bucket/input.jsonl",
        output_uri="gs://bucket/output",
    )
    assert target.to_vertex_batch_predict_kwargs(config) == {
        "job_display_name": "job",
        "gcs_source": ["gs://bucket/input.jsonl"],
        "gcs_destination_prefix": "gs://bucket/output",
        "instances_format": "jsonl",
        "predictions_format": "jsonl",
        "sync": False,
    }

