# Generated by Django 3.1.12 on 2021-09-19 21:38
from django.db import migrations
from django.db import models


class Migration(migrations.Migration):

    dependencies = [
        ("puzzle_editing", "0003_auto_20210208_0427"),
    ]

    operations = [
        migrations.AlterField(
            model_name="puzzle",
            name="status",
            field=models.CharField(
                choices=[
                    ("II", "Concept"),
                    ("W", "Writing"),
                    ("T", "Testsolving"),
                    ("R", "Revising"),
                    ("NS", "Needs Solution & Hints"),
                    ("D", "Done"),
                    ("X", "Dead"),
                ],
                default="II",
                max_length=2,
            ),
        ),
        migrations.AlterField(
            model_name="puzzlecomment",
            name="status_change",
            field=models.CharField(
                blank=True,
                choices=[
                    ("II", "Concept"),
                    ("W", "Writing"),
                    ("T", "Testsolving"),
                    ("R", "Revising"),
                    ("NS", "Needs Solution & Hints"),
                    ("D", "Done"),
                    ("X", "Dead"),
                ],
                help_text="Any status change caused by this comment. Only used for recording history and computing statistics; not a source of truth (i.e. the puzzle will still store its current status, and this field's value on any comment doesn't directly imply anything about that in any technically enforced way).",
                max_length=2,
            ),
        ),
        migrations.AlterField(
            model_name="statussubscription",
            name="status",
            field=models.CharField(
                choices=[
                    ("II", "Concept"),
                    ("W", "Writing"),
                    ("T", "Testsolving"),
                    ("R", "Revising"),
                    ("NS", "Needs Solution & Hints"),
                    ("D", "Done"),
                    ("X", "Dead"),
                ],
                max_length=2,
            ),
        ),
    ]