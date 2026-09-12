from pydantic import BaseModel, Field
from typing import Literal


class ListeningExerciseSchema(BaseModel):
    speaker_one: str = Field(..., description="Nama pembicara pertama, misalnya: 'Joe'")
    speaker_two: str = Field(..., description="Nama pembicara kedua, mislanya : 'jane'")
    script: str = Field(
        ...,
        description="Dialog yang dibacakan oleh TTS (Text-to_speech), format: Joe: ... \\nJane: ... (Berbicara bergantian)",
    )
    questions: list[str] = Field(
        ...,
        description="Daftar pertanyaan untuk menguji pemahaman peserta berdasarkan 'script'",
    )


class EvaluateUserIntentionShcema(BaseModel):
    skill_type: Literal["reading", "writing", "speaking", "listening"] = Field(
        ..., description="pilih salah satu skill_type yang dibutuhkan peserta"
    )


class LearningSkillTypeSchema(BaseModel):
    category: str = Field(
        ..., description="salah satu skill_type : reading, writing, listening, speaking"
    )
    title: str = Field(..., description="Judul Latihan")
    feedback: str = Field(..., description="Feedback latihan")
    score: int = Field(..., description="Nilai pembelajaran rentang 1-10")


class LearningReportSchema(BaseModel):
    strat_date: str = Field(..., description="Tanggal mulai belajar")
    end_date: str = Field(..., description="Tanggal berakhir belajar")
    username: str = Field(..., description="Username peserta")
    global_score: int = Field(
        ..., description="Nilai score secara global atau keseluruhan"
    )
    skill_types: list[LearningSkillTypeSchema]  # list of LeaningSkillTypeSchema
    markdown_content: str = Field(
        ..., description="Seluruh isi laporan dalam format markdown"
    )
