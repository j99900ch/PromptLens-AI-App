from flask import Blueprint, render_template, request

from app.pipeline.prompt_pipeline import PromptPipeline

bp = Blueprint("main", __name__)

pipeline = PromptPipeline()


@bp.route("/", methods=["GET", "POST"])
def home():

    if request.method == "POST":

        user_prompt = request.form.get("prompt", "").strip()

        if user_prompt:

            result = pipeline.run(user_prompt)

            print(result)

            return render_template(
                "index.html",
                prompt=user_prompt,
                generation=result["generation"],
                evaluation=result["evaluation"],
                redesign=result["redesign"],
            )

    return render_template("index.html")